import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
def criar_arquivo_excel(arquivo_excel):
    df = pd.DataFrame(columns=['DATA', 'VEICULO', 'QTD ABASTECIDA', 'KM', 'LITROS RESTANTE', 'SITUAÇÃO DO PEDIDO'])
    df.to_excel(arquivo_excel, sheet_name='Dados', index=False)
def adicionar_dados(data, placa, combustivel, km, L_restantes, situ_pedido, arquivo_excel):

    
    try:                  #Se a planilha não existir, vai criar uma nova
        if not os.path.isfile(arquivo_excel):
            criar_arquivo_excel(arquivo_excel)
               
        novo_dado = pd.DataFrame({
            'DATA': [data],
            'VEICULO': [placa],
            'QTD ABASTECIDA': [combustivel],
            'KM': [km],
            'LITROS RESTANTE': [L_restantes],
            'SITUAÇÃO DO PEDIDO': [situ_pedido],
        })
              
        with pd.ExcelWriter(arquivo_excel, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df_existing = pd.read_excel(arquivo_excel, sheet_name='Dados')
            df_updated = pd.concat([df_existing, novo_dado], ignore_index=True)
            df_updated.to_excel(writer, sheet_name='Dados', index=False)
        
        messagebox.showinfo("Sucesso", "Dados adicionados com sucesso!")
    
    except Exception as e:
        messagebox.showerror("Erro!", f"Erro ao adicionar dados: {e}")
def enviar_dados():
    placa = entry_placa.get()
    combustivel = entry_combustivel.get()
    data = entry_data.get()
    km = entry_km.get()
    L_restantes = entry_L_restantes.get()
    situ_pedido = entry_situ_pedido.get()
    
    if not placa or not combustivel or not data:
        messagebox.showwarning("Erro!", "Todos os campos obrigatórios devem ser preenchidos!")
        return    
    adicionar_dados(data, placa, combustivel, km, L_restantes, situ_pedido, 'PLANILHA_DE_COMBUSTIVEL.xlsx')
    
    entry_placa.delete(0, tk.END)
    entry_combustivel.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_km.delete(0, tk.END)
    entry_L_restantes.delete(0, tk.END)
    entry_situ_pedido.delete(0, tk.END)
#Config  da interface gráfica
root = tk.Tk()
root.title("Abastecimento TDM")

#Config estilo
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12, 'bold'))
style.configure('TEntry', font=('Arial', 12,'bold', )) 
style.configure('TButton', font=('Arial', 12), padding=10)

#Criar widgets do sistema, altere do jeito que achar melhor.
ttk.Label(root, text="Placa do Veículo:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_placa = ttk.Entry(root)
entry_placa.grid(row=0, column=1, padx=10, pady=5)
ttk.Label(root, text="Quantidade Abastecida:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_combustivel = ttk.Entry(root)
entry_combustivel.grid(row=1, column=1, padx=10, pady=5)
ttk.Label(root, text="Data:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_data = ttk.Entry(root)
entry_data.grid(row=2, column=1, padx=10, pady=5)
ttk.Label(root, text="Km:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_km = ttk.Entry(root)
entry_km.grid(row=3, column=1, padx=10, pady=5)
ttk.Label(root, text="Litros Restantes:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
entry_L_restantes = ttk.Entry(root)
entry_L_restantes.grid(row=4, column=1, padx=10, pady=5)
ttk.Label(root, text="Situação Pedido:").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
entry_situ_pedido = ttk.Entry(root)
entry_situ_pedido.grid(row=5, column=1, padx=10, pady=5)
ttk.Button(root, text="Enviar", command=enviar_dados).grid(row=6, columnspan=2, pady=10)
root.mainloop()