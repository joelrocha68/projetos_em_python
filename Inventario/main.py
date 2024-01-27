
from tkinter import *
from tkinter import ttk
from tkinter import StringVar
from tkinter import Tk
import tkinter

# Importando Pillow
from PIL import Image, ImageTk

# Importando TKcalendar
from tkcalendar import DateEntry
from datetime import date

# Cores

co0 = "#2e2d2d" # preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # azul
co4 = "#403d3d" # preto
co5 = "#e06636" # vermelho claro
co6 = "#038cfc" # azul escuro
co7 = "#3fbfb9" # azul claro
co8 = "#263238" # preto
co9 = "#e9edf5" # branco


# Criando janela
janela = Tk()
janela.title('Inventario')
janela.geometry('900x600')
janela.configure(background=co4)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Abrindo imagem
app_img = Image.open('inventario.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

# trabalhando no frame de cima
app_logo = Label(frameCima, image=app_img, text='Inventário Doméstico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# trabalhando no frame do meio

# Criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text='Local', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_modelo = Label(frameMeio, text='Marca/Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_modelo.place(x=10, y=100)
e_modelo = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_modelo.place(x=130, y=101)

l_cal = Label(frameMeio, text='Data', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background='darkblue', bordewidth=2, year=2024)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text='Valor', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio, text='Série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.place(x=130, y=191)

# Criando botoes

# Botao carregar
l_carregar = Label(frameMeio, text='Imagem', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, width=31, text='Carregar'.upper(),compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)

# botao inserir
img_add = Image.open('botao_add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, image=img_add, width=95, text='  Adicionar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=400, y=10)

# botao atualizar
img_update = Image.open('atualizar.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

b_atualizar = Button(frameMeio, image=img_update, width=95, text='  Atualizar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_atualizar.place(x=400, y=50)

# botao deletar
img_delete = Image.open('Deletar.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, image=img_delete, width=95, text='  Excluir'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=400, y=90)

# botao ver item
img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio, image=img_item, width=95, text='  Ver item'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=400, y=130)

# Labels quantidade total e valores
l_total = Label(frameMeio, text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=550, y=17)
l_total = Label(frameMeio, text=' Valor total de todos os itens ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total.place(x=620, y=50)

l_qtd = Label(frameMeio, text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd.place(x=550, y=90)
l_qtd = Label(frameMeio, text='   Quantidade total de itens', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd.place(x=660, y=120)

# Tabela

# creating a treeview with dual scrollbars
tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

lista_itens = []

global tree

tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

# vertical scrollbar
vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frameBaixo.grid_rowconfigure(0, weight=12)

hd=["center","center","center","center","center","center","center", 'center']
h=[60,70,100,90,130,140,140, 140]
n=0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
# adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1


# inserindo os itens dentro da tabela
for item in lista_itens:
    tree.insert('', 'end', values=item)


quantidade = [8888,88]

# Inserir os itens dentro da tabela
for iten in lista_itens:
    quantidade.append(iten[6])

Total_valor = sum(quantidade)
Total_itens = len(quantidade)

l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
l_qtd['text'] = Total_itens


janela.mainloop()
