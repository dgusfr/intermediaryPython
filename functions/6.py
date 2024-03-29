def data_por_extenso(data):
    try:
        # Separar dia, mês e ano
        dia, mes, ano = map(int, data.split('/'))

        # Validar a data
        if not (1 <= dia <= 31 and 1 <= mes <= 12):
            raise ValueError("Data inválida")

        # Lista com os nomes dos meses
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto",
            "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        # Formatar a data
        formato_final = f"{dia} de {meses[mes - 1]} de {ano}"

        return formato_final
    except (ValueError, IndexError):
        # Tratar erro de data inválida
        return None

# Solicitar entrada do usuário
data_input = input("Informe a data no formato DD/MM/AAAA: ")

# Chamar a função e imprimir o resultado
resultado = data_por_extenso(data_input)
if resultado is not None:
    print(f"A data por extenso é: {resultado}")
else:
    print("Data inválida. Retornando NULL.")

# OU IMPORTANDO DATETIME
    
from datetime import datetime

def data_por_extenso(data):
    try:
        # Converter a string de data para um objeto datetime
        data_formatada = datetime.strptime(data, '%d/%m/%Y')

        # Obter o formato desejado
        formato_final = data_formatada.strftime('%d de %B de %Y')

        return formato_final
    except ValueError:
        # Tratar erro de data inválida
        return None

# Solicitar entrada do usuário
data_input = input("Informe a data no formato DD/MM/AAAA: ")

# Chamar a função e imprimir o resultado
resultado = data_por_extenso(data_input)
if resultado is not None:
    print(f"A data por extenso é: {resultado}")
else:
    print("Data inválida. Retornando NULL.")

