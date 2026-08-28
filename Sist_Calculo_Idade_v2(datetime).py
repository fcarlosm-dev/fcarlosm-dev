from datetime import datetime

print("=" * 50)
print("           SISTEMA DE CÁLCULO DE IDADE")
print("=" * 50)

try:
    # Solicitando o nome completo do usuário
    nome_completo = input("\nDigite seu nome completo: ").strip()
    
    # Solicitando o ano de nascimento
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    
    # Obtendo o ano atual
    ano_atual = datetime.now().year
    
    # Validando se o ano informado é válido
    if ano_nascimento > ano_atual:
        print("Erro: O ano de nascimento não pode ser maior que o ano atual!")
    elif ano_nascimento < (ano_atual - 2000):
        print("Erro: O ano de nascimento parece estar incorreto!")
    else:
        # Calculando a idade atual
        idade_atual = ano_atual - ano_nascimento
        
        # Exibindo a mensagem personalizada
        print("\n" + "-" * 50)
        print("RESULTADO:")
        print(f"Olá, {nome_completo}!!! Você nasceu no ano {ano_nascimento} e atualmente está com {idade_atual} anos de vida.")
        print("-" * 50)
        
except ValueError:
    print("Erro: Por favor, digite apenas números para o ano de nascimento!")