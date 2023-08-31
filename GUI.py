from tkinter import *

class Gui():
    """ Classe de Interface Grafica"""
    x_pad = 5
    y_pad = 3
    width_entry = 30

    window = Tk()
    window.wm_title('PYSQL versão 1.0')

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    #Nomes dos campos
    lblNome = Label(window, text = 'Nome')
    lblSobrenome = Label(window, text = 'Sobrenome')
    lblEmail = Label(window, text = 'Email')
    lblCPF = Label(window, text = 'CPF')

    #Campos de entrada
    entNome = Entry(window, textvariable=txtNome,width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome,width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail,width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF,width=width_entry)

    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)

    #Botões de ação
    btnViewAll = Button(window, text='VER TODOS')
    btnBuscar = Button(window, text='BUSCAR')
    btnInserir = Button(window, text='INSERIR')
    btnUpdate = Button(window, text='ATUALIZAR')
    btnDel = Button(window, text='DELETAR')
    btnClose = Button(window, text='FECHAR')

    #Associaçao de objetos
    lblNome.grid(row=0,column=0)
    lblSobrenome.grid(row=1,column=0)
    lblEmail.grid(row=2,column=0)
    lblCPF.grid(row=3,column=0)
    
    entNome.grid(row=0,column=1,padx=50,pady=50)
    entSobrenome.grid(row=1,column=1)
    entEmail.grid(row=2,column=1)
    entCPF.grid(row=3,column=1)

    listClientes.grid(row=0,column=2,rowspan=10)
    scrollClientes.grid(row=0,column=6,rowspan=10)

    btnViewAll.grid(row=4,column=0,columnspan=2)
    btnBuscar.grid(row=5,column=0,columnspan=2)
    btnInserir.grid(row=6,column=0,columnspan=2)
    btnUpdate.grid(row=7,column=0,columnspan=2)
    btnDel.grid(row=8,column=0,columnspan=2)
    btnClose.grid(row=9,column=0,columnspan=2)

    #Unir scrollbar com a listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    #adicionar aparencia
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class=='Button':
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class=='Listbox':
            child.grid_configure(padx=0,pady=0, sticky='NS')
        elif widget_class=='Scrollbar':
            child.grid_configure(padx=0,pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    #def run (self):
       # Gui.window.mainloop()    
    