"""main.py"""

import tkinter as tk
from tkinter import messagebox

class MeuApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Minha Aplicação")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Digite seu nome:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Enviar", command=self.clique_botao)
        self.button.pack()

        self.var_checkbutton = tk.BooleanVar()
        self.checkbutton = tk.Checkbutton(self, text="Opção",
                                          variable=self.var_checkbutton)
        self.checkbutton.pack()

        self.var_radiobutton = tk.StringVar()
        self.radiobutton1 = tk.Radiobutton(self, text="Opção 1",
                                           variable=self.var_radiobutton,
                                           value="opcao1")
        self.radiobutton1.pack()
        self.radiobutton2 = tk.Radiobutton(self, text="Opção 2",
                                           variable=self.var_radiobutton,
                                           value="opcao2")
        self.radiobutton2.pack()

        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Novo", command=self.novo_arquivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.sair)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.config(menu=self.menu_bar)

        self.frame = tk.Frame(self, relief=tk.SOLID, borderwidth=1)
        self.frame.pack(pady=10)

        self.status_label = tk.Label(self.frame, text="Status:")
        self.status_label.pack(side=tk.LEFT)
        self.status_text = tk.StringVar()
        self.status_text.set("Pronto")
        self.status = tk.Label(self.frame, textvariable=self.status_text)
        self.status.pack(side=tk.LEFT)

    def clique_botao(self):
        nome = self.entry.get()
        messagebox.showinfo("Informação", f"Olá, {nome}!")

    def novo_arquivo(self):
        self.status_text.set("Novo arquivo criado.")

    def abrir_arquivo(self):
        self.status_text.set("Arquivo aberto.")

    def sair(self):
        if messagebox.askokcancel("Sair", "Deseja sair da aplicação?"):
            self.destroy()

app = MeuApp()
app.mainloop()
