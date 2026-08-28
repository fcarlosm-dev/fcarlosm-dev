# Importando a biblioteca datetime para obter o ano atual
from datetime import datetime

# Solicitando o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# Solicitando o ano de nascimento
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Obtendo o ano atual
ano_atual = datetime.now().year

# Calculando a idade atual
idade_atual = ano_atual - ano_nascimento

# Exibindo a mensagem personalizada
print(f"Olá, {nome_completo}!!! Você nasceu no ano {ano_nascimento} e atualmente está com {idade_atual} anos de vida.")