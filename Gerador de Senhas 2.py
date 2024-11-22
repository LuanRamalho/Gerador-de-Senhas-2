import tkinter as tk
from tkinter import messagebox
import random
import string

# Função para gerar a senha
def gerar_senha():
    try:
        qtd_caracteres = int(entry_qtd.get())
        if qtd_caracteres <= 0:
            raise ValueError("A quantidade de caracteres deve ser maior que zero.")
        
        # Verifica qual opção foi selecionada
        if var_opcao.get() == 1:  # Apenas letras minúsculas
            caracteres = string.ascii_lowercase
        elif var_opcao.get() == 2:  # Apenas letras maiúsculas
            caracteres = string.ascii_uppercase
        elif var_opcao.get() == 3:  # Apenas números
            caracteres = string.digits
        elif var_opcao.get() == 4:  # Letras e caracteres especiais
            caracteres = string.ascii_letters + string.punctuation
        elif var_opcao.get() == 5:  # Números e caracteres especiais
            caracteres = string.digits + string.punctuation
        elif var_opcao.get() == 6:  # Letras, números e caracteres especiais
            caracteres = string.ascii_letters + string.digits + string.punctuation
        else:
            raise ValueError("Selecione uma opção válida.")
        
        # Gera a senha
        senha = ''.join(random.choice(caracteres) for _ in range(qtd_caracteres))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.configure(bg="#2E2E2E")
root.geometry("750x450")

# Título
titulo = tk.Label(root, text="Gerador de Senhas", font=("Arial", 18, "bold"), fg="white", bg="#2E2E2E")
titulo.pack(pady=10)

# Caixa de texto para quantidade de caracteres
frame_qtd = tk.Frame(root, bg="#2E2E2E")
frame_qtd.pack(pady=5)
label_qtd = tk.Label(frame_qtd, text="Quantidade de caracteres:", font=("Arial", 14), fg="white", bg="#2E2E2E")
label_qtd.pack(side=tk.LEFT, padx=5)
entry_qtd = tk.Entry(frame_qtd, font=("Arial", 14), width=5)
entry_qtd.pack(side=tk.LEFT)

# Opções de tipo de senha
var_opcao = tk.IntVar()
frame_opcoes = tk.Frame(root, bg="#2E2E2E")
frame_opcoes.pack(pady=10)
opcoes = [
    ("Somente letras minúsculas", 1),
    ("Somente letras maiúsculas", 2),
    ("Somente números", 3),
    ("Letras e caracteres especiais", 4),
    ("Números e caracteres especiais", 5),
    ("Letras, números e caracteres especiais", 6)
]
for texto, valor in opcoes:
    rb = tk.Radiobutton(
        frame_opcoes, text=texto, variable=var_opcao, value=valor,
        font=("Arial", 14), fg="white", bg="#2E2E2E", selectcolor="#4C4C4C"
    )
    rb.pack(anchor=tk.W)

# Botão para gerar senha
btn_gerar = tk.Button(root, text="Gerar Senha", font=("Arial", 14, "bold"), bg="#1C86EE", fg="white", command=gerar_senha)
btn_gerar.pack(pady=10)

# Caixa de texto para exibir a senha gerada
frame_senha = tk.Frame(root, bg="#2E2E2E")
frame_senha.pack(pady=5)
label_senha = tk.Label(frame_senha, text="Senha gerada:", font=("Arial", 14), fg="white", bg="#2E2E2E")
label_senha.pack(side=tk.LEFT, padx=5)
entry_senha = tk.Entry(frame_senha, font=("Arial", 14), width=50)
entry_senha.pack(side=tk.LEFT)

# Executar o programa
root.mainloop()
