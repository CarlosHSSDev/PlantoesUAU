import calendar
import holidays
import json
from datetime import datetime


# Mapeamento manual dos dias da semana para português
DIAS_DA_SEMANA = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

# Tradução manual para feriados brasileiros
FERIADOS_TRADUZIDOS = {
    "Universal Fraternization Day": "Ano Novo",
    "Good Friday": "Sexta-feira Santa",
    "Tiradentes' Day": "Dia de Tiradentes",
    "Worker's Day": "Dia do Trabalhador",
    "Independence Day": "Dia da Independência",
    "Our Lady of Aparecida": "Nossa Senhora Aparecida",
    "All Souls' Day": "Dia de Finados",
    "Republic Proclamation Day": "Proclamação da República",
    "National Day of Zumbi and Black Awareness": "Dia Nacional da Consciência Negra",
    "Christmas Day": "Natal",
}


class GerenciadorPlantoes:
    def __init__(self, ano_atual, ano_futuro, equipes):
        self.ano_atual = ano_atual
        self.ano_futuro = ano_futuro
        self.equipes = equipes

    def listar_domingos(self, ano):
        domingos = []
        for mes in range(1, 13):
            semanas = calendar.monthcalendar(ano, mes)
            for semana in semanas:
                if semana[calendar.SUNDAY] != 0:
                    domingos.append(f"{ano}-{mes:02d}-{semana[calendar.SUNDAY]:02d}")
        return domingos

    def obter_datas_unicas(self, ano):
        domingos = self.listar_domingos(ano)
        feriados = holidays.Brazil(years=ano)
        feriados_lista = [str(data) for data in feriados.keys()]
        todas_as_datas = set(domingos + feriados_lista)
        return sorted(todas_as_datas)

    def filtrar_dezembro(self, datas, ano):
        return [data for data in datas if data.startswith(f"{ano}-12")]

    def filtrar_ano(self, datas, ano):
        return [data for data in datas if data.startswith(str(ano))]

    def distribuir_trabalho(self, datas):
        distribuicao = []
        equipes_lista = list(self.equipes.keys())
        num_equipes = len(equipes_lista)

        for i, data in enumerate(datas):
            equipe = equipes_lista[i % num_equipes]
            distribuicao.append((data, equipe))

        return distribuicao

    def filtrar_por_usuario(self, nome_usuario):
        # Obter a data atual
        hoje = datetime.now()

        # Obter as datas únicas para os dois anos
        datas_unicas_atual = self.obter_datas_unicas(self.ano_atual)
        datas_unicas_futuro = self.obter_datas_unicas(self.ano_futuro)

        # Combinar as datas de dezembro do ano atual com todas do ano futuro
        datas_dezembro_atual = self.filtrar_dezembro(datas_unicas_atual, self.ano_atual)
        datas_futuro = self.filtrar_ano(datas_unicas_futuro, self.ano_futuro)
        datas_combinadas = sorted(datas_dezembro_atual + datas_futuro)

        # Distribuir as datas entre as equipes
        distribuicao = self.distribuir_trabalho(datas_combinadas)

        # Filtrar os plantões do usuário
        plantao_usuario = []
        feriados = holidays.Brazil(years=[self.ano_atual, self.ano_futuro])
        for data, equipe in distribuicao:
            data_obj = datetime.strptime(data, "%Y-%m-%d")  # Converter a data para objeto datetime
            if data_obj > hoje and nome_usuario in self.equipes[equipe]:  # Filtro para datas futuras
                data_formatada = "/".join(reversed(data.split("-")))
                observacao = feriados.get(data)
                if observacao:
                    observacao = FERIADOS_TRADUZIDOS.get(observacao, observacao)
                else:
                    ano, mes, dia = map(int, data.split("-"))
                    dia_semana_en = calendar.day_name[calendar.weekday(ano, mes, dia)]
                    observacao = DIAS_DA_SEMANA[dia_semana_en]

                plantao_usuario.append({"data": data_formatada, "descricao": observacao})

        return json.dumps(plantao_usuario, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    equipes = {
        "Equipe 1": ["Marcos Vinicius", "Filipe", "Carlos", "Rafael (NOC)"],
        "Equipe 2": ["Valdemir", "Hicaro", "Rodrigo Santana", "Gabriel (NOC)"],
        "Equipe 3": ["Caio", "Josiel", "Gisnei", "Daniel (NOC)"],
        "Equipe 4": ["Henrique", "Genisson", "Ayrton", "Romário (NOC)"],
        "Equipe 5": ["Uelio", "Davi", "Valdenilson", "Rafael (NOC)"],
        "Equipe 6": ["Wesley", "Moises", "José Leoni", "Gabriel (NOC)"],
        "Equipe 7": ["Jardel", "Ailton", "José Williams", "Daniel (NOC)"]
    }

    gerenciador = GerenciadorPlantoes(2024, 2025, equipes)
    nome_usuario = "Jardel"
    plantao_usuario_json = gerenciador.filtrar_por_usuario(nome_usuario)
    print(plantao_usuario_json)