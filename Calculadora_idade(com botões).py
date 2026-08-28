import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de Idade")
janela.geometry("500x400")
janela.configure(bg='#f0f0f0')

# Função para calcular idade
def calcular_idade():
    try:
        # Obtendo os valores dos campos
        nome = entrada_nome.get().strip()
        ano_nascimento = int(entrada_ano.get())
        
        # Validando campos vazios
        if not nome:
            messagebox.showerror("Erro", "Por favor, digite seu nome completo!")
            return
        
        # Validando ano de nascimento
        ano_atual = datetime.now().year
        if ano_nascimento > ano_atual:
            messagebox.showerror("Erro", "O ano de nascimento não pode ser maior que o ano atual!")
            return
        
        # Calculando idade
        idade = ano_atual - ano_nascimento
        
        # Exibindo resultado
        resultado = f"Olá, {nome}!!! Você nasceu no ano {ano_nascimento} e atualmente está com {idade} anos de vida."
        
        # Mostrando resultado na janela
        resultado_label.config(text=resultado, bg='#e8f5e8', fg='#27ae60')
        
        # Também mostrando em popup
        messagebox.showinfo("Resultado", resultado)
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números no campo ano de nascimento!")

# Função para limpar campos
def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_ano.delete(0, tk.END)
    resultado_label.config(text="", bg='#f0f0f0')
    entrada_nome.focus()

# Título
titulo = tk.Label(
    janela,
    text="SISTEMA DE CÁLCULO DE IDADE",
    font=("Arial", 16, "bold"),
    bg='#f0f0f0',
    fg='#2c3e50'
)
titulo.pack(pady=20)

# Frame para campos de entrada
frame_entrada = tk.Frame(janela, bg='#f0f0f0')
frame_entrada.pack(pady=20)

# Campo nome
tk.Label(
    frame_entrada,
    text="Nome Completo:",
    font=("Arial", 12),
    bg='#f0f0f0'
).grid(row=0, column=0, sticky='w', pady=10)

entrada_nome = tk.Entry(
    frame_entrada,
    width=30,
    font=("Arial", 12)
)
entrada_nome.grid(row=0, column=1, pady=10, padx=10)

# Campo ano
tk.Label(
    frame_entrada,
    text="Ano de Nascimento:",
    font=("Arial", 12),
    bg='#f0f0f0'
).grid(row=1, column=0, sticky='w', pady=10)

entrada_ano = tk.Entry(
    frame_entrada,
    width=30,
    font=("Arial", 12)
)
entrada_ano.grid(row=1, column=1, pady=10, padx=10)

# Frame para botões
frame_botoes = tk.Frame(janela, bg='#f0f0f0')
frame_botoes.pack(pady=20)

# Botão Calcular
botao_calcular = tk.Button(
    frame_botoes,
    text="CALCULAR IDADE",
    command=calcular_idade,
    font=("Arial", 12, "bold"),
    bg='#27ae60',
    fg='white',
    padx=20,
    pady=10,
    cursor='hand2'
)
botao_calcular.grid(row=0, column=0, padx=10)

# Botão Limpar
botao_limpar = tk.Button(
    frame_botoes,
    text="LIMPAR",
    command=limpar_campos,
    font=("Arial", 12, "bold"),
    bg='#e74c3c',
    fg='white',
    padx=20,
    pady=10,
    cursor='hand2'
)
botao_limpar.grid(row=0, column=1, padx=10)

# Área de resultado
resultado_label = tk.Label(
    janela,
    text="",
    font=("Arial", 11),
    bg='#f0f0f0',
    fg='#2c3e50',
    wraplength=400,
    justify='center',
    pady=20
)
resultado_label.pack(pady=20)

# Iniciar a aplicação
entrada_nome.focus()
janela.mainloop()
