from tkinter import *
import tkinter as tk
import threading
import pandas as pd
from datetime import date
import calendar
from tkinter import ttk
from gtts import gTTS
from playsound import playsound


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        tinicial = tk.Tk()
        tinicial.geometry("800x800+500+100")
        tinicial.title("Sua Agenda Eletrônica - ...")
        tinicial.resizable(width=False, height=False)
        tinicial['bg'] = 'black'
        tinicial.iconphoto(True, PhotoImage(file='./arquivos/robo1.png'))
        image=PhotoImage(file='./arquivos/robo1.png')
        win_width, win_height = 500, 800
        global robozinho
        global falinha
        global tabela
        robozinho = Label(tinicial, image = image,width=500, height=800,bg ='black')
        robozinho.grid(row=5,columnspan =9)
        falinha= Label(tinicial, wraplength=win_width, height=10,bg ='black',text= 'Olá Sou Sua Agenda Eletrônica',fg='white',font=('arial',14,'bold'))
        falinha.place(relx=0.5, rely = 0.08)        
        botao= Button(tinicial, width=20, height=2,bg ='black',command=tarefadodia, text= 'Tarefas',fg='white',font=('arial',14,'bold'))
        botao.place(relx=0.05, rely = 0.8)
        botsai= Button(tinicial, width=20, height=2,bg ='black',command=saindo, text= 'Sair',fg='white',font=('arial',14,'bold'))
        botsai.place(relx=0.5, rely = 0.8)
        #tabela = ttk.Treeview(tinicial,column=(''))
        #tampinha= Label(tinicial, width=10, height=20,bg ='black',fg='white',font=('arial',14,'bold'))
        #tampinha.place(relx=0.72, rely = 0.2) 


        #tabela.heading('preco', text='Nosso preço')
        
        #tabela.enable = False


        tinicial.mainloop()

        '''image=PhotoImage(file='./arquivos/robo3.png')
        robozinho.config(image=image)
        robozinho.image = image
        falinha.config(text=jegue)'''
def tarefadodia():
    dias_da_semana = {'Sunday':'Domingo','Monday':'Segunda','Tuesday':'Terça','Wednesday':'Quarta','Thursday':'Quinta','Friday':'Sexta','Saturday':'Sábado'}
    curr_date = date.today()
    dia_atual = dias_da_semana[str(calendar.day_name[curr_date.weekday()])]
    #print (dia_atual)
    image=PhotoImage(file='./arquivos/robo3.png')
    robozinho.config(image=image)
    robozinho.image = image
    

    path = '.\\arquivos'
    df = pd.DataFrame()
    filesarquivo =[path + '\\' + 'minha_agenda.xlsx']
    for f in filesarquivo:
        data=pd.read_excel(f) 
        df = df.append(data)
        
    ORDENADO = df[[dia_atual]]
    
    repetir= ORDENADO.shape
    repetir = repetir[0]
    cotes=0
    tarefinhas = ""
    while repetir > cotes:

        tarefinhas = tarefinhas + str(ORDENADO.loc[cotes, dia_atual])
        #tabela.insert('', 'end', text=(str(ORDENADO.loc[cotes, dia_atual]).upper()))
        #tabela.column(ORDENADO.loc[cotes, dia_atual],width=150, minwidth=150, stretch=tk.NO)
        cotes +=1
    #tabela.place(relx=0.5, rely = 0.2)
    aula_dia =  'Para hoje ' + dia_atual +  ", sua aula é de: " + '\n' +  '\n' +tarefinhas.upper() 
    falinha.config(text=aula_dia)
    falinha.place(relx=0.5, rely = 0.3) 


    aulas = gTTS(aula_dia, lang="pt")
    aulas.save("./conversas/aulas.mp3")
    aulas = "./conversas/aulas.mp3"
    playsound(aulas)

def saindo():
    exit(1)
        
app = App()

voz = gTTS("Seja bem vindo, clique para saber sua aula de hoje:  ", lang="pt")
voz.save("./conversas/voz.mp3")
falar = "./conversas/voz.mp3"
playsound(falar)

