from tkinter import*
from random import randint
from tkinter import messagebox

gen = Tk()
gen.title('Gerador de Senhas')
gen.geometry('400x500')

var_letras_min = IntVar()
var_letras_mai = IntVar()
var_numeros = IntVar()
var_caracteres = IntVar()

letras_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

caracateres = ['@','!','#','$','%','&','*', '(',')','-','+','=','{','}','[',']','~',"<",'>','.',';','/',':',',']

l1 = Label(gen, text='Digite o tamanho da senha', font='Arial 12')
l1.place(x=108,y=15)

tamanho = Entry(gen, justify='center', font='Arial 18')
tamanho.place(x=150,width=100,y=50, height=50)

l2 = Label(gen, text='Tipos de caracteres', font='Arial 12')
l2.place(x=124,y=130)

let_min = Checkbutton(gen, text='Letras minúsculas', variable=var_letras_min)
let_min.place(x=130,y=160)

let_mai = Checkbutton(gen, text='Letras maiúsculas', variable=var_letras_mai)
let_mai.place(x=130, y=190)

num_ = Checkbutton(gen, text='Números',variable=var_numeros)
num_.place(x=130,y=220)

car_ = Checkbutton(gen, text='Símbolos', variable=var_caracteres)
car_.place(x=130, y=250)


def gerar():
    senha = []

    if var_letras_mai.get() == False and var_numeros.get() == False and var_letras_min.get() == False and var_caracteres.get() == False:
        saida.delete(0, END)
        saida.insert(0, 'Nenhum tipo de caracteres foi especificado')



    tamanho_senha = int(tamanho.get())


    while True:
        le_mi = randint(0, 25)
        car = randint(0, 23)
        num = randint(0, 9)
        le_ma = randint(0, 25)
        alea = randint(0, 3)
        if len(senha) == tamanho_senha:
            break


        if alea == 0 and var_letras_min.get() == True:
            senha.append(letras_min[le_mi])

            if len(senha) == tamanho_senha:
                break

        elif alea == 1 and var_caracteres.get() == True:
            senha.append(caracateres[car])

            if len(senha) == tamanho_senha:
                break

        elif alea == 2 and var_numeros.get() == True:
            senha.append(str(numeros[num]))

            if len(senha) == tamanho_senha:
                break

        elif alea == 3 and var_letras_mai.get() == True:
            senha.append(letras_mai[le_ma])
            if len(senha) == tamanho_senha:
                break

    if len(senha) > 39:
        saida['fg'] = 'red'
        saida.delete(0,END)
        saida.insert(0, ''.join(senha))
        messagebox.showwarning('Mensagem grande demais', 'Tamanho da mensagem muito grande \n Cuidado ao copiar')

    else:
        saida.delete(0, END)
        saida.insert(0, ''.join(senha))




b = Button(gen, text='Gerar senha', command=gerar)
b.place(x=150,y=300, width=100)

saida = Entry(gen, font='Arial 12', justify='center')
saida.place(x=20, width=360, height=100, y=360)


gen.mainloop()