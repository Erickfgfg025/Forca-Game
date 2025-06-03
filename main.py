from tkinter import *
from PIL import Image, ImageTk
import pygame
from gerador_palavra import palavra_sortear


class Jogo:
    def __init__(self):
        
        self.tela = Tk()
        self.cor_fundo = "#DABCA1"
        self.tela.geometry("800x600")
        self.tela.title("Jogo da Forca")
        self.tela['bg']=self.cor_fundo
        self.tela.resizable(False,False)
        
        
        #inicila som
        pygame.init()
        pygame.mixer.init()
        self.acerto = pygame.mixer.Sound("som/acerto.mp3")
        self.trilha = pygame.mixer.Sound("som/trilha-sonora.mp3")
        self.trilha.play(-1)
        self.trilha.set_volume(0.2)
        self.acerto.set_volume(0.2)


        self.frame1 = Frame(self.tela)
        #self.frame2 = Frame(self.tela)
        self.frame1.pack(fill="both",expand=True)
        #self.frame2.pack(fill="both")
        
        
        self.cor_texto = "#E0D9C8"
        #carrega todas as imagens 
       
        self.fundo = Image.open("imagens/telainicial-fundo.png")
        self.fundo = self.fundo.resize((800,600))
        self.fundo_tk = ImageTk.PhotoImage(self.fundo)
        

        self.palavra = palavra_sortear().upper()
        self.descoberta = ["_"] * len(self.palavra)
        self.palavras_errada = []
        self.chances = 6

        
        
        #construo todos os botões e textos 
        
        self.imagem = Label(self.frame1,image = self.fundo_tk)
        self.titulo = Label(self.frame1, text="Jogo da Forca", fg="black",font=('Verdana',25,'bold'))
        self.btn_iniciar = Button(self.frame1,text="Iniciar Jogo",font=("Verdana",16),fg="black", bd=5, bg=self.cor_texto,command=self.iniciarjogo,relief="flat")
        
        
        
        
        #desenho todos botões e textos
        
        self.imagem.place(x=0,y=0,relwidth=1,relheight=1)
        self.titulo.pack(pady=(80,10))
        self.btn_iniciar.pack(pady=(350,20))

        self.tela.mainloop() # faz o código rodar
        
    def iniciarjogo(self):
        self.tela.bind("<Return>", lambda event: self.tentar())
        self.frame1.pack_forget()
        
        #self.imagem2 = Label(self.tela,image=self.fundo_tk)
        self.lbl_palavra = Label(self.tela,text=" ".join(self.descoberta),font=("Arial",30,"bold"),bg=self.cor_fundo,bd=1)
        self.chute = Entry(self.tela,width=10,bd=5)
        self.lbl_tentativas = Label(self.tela, text= f"Tentativas: {self.chances}",font=("Arial",12),bg=self.cor_fundo)

        self.resultado = Label(self.tela, text = " ", fg= "green", font=("Verdana", 12),bg=self.cor_fundo)

        self.btn_chutar = Button(self.tela, text="Chutar",command=self.tentar,font=("Verdana",12,"bold"),relief="flat",bg="grey",fg="white",width=10)
      
      
      
      #manda desenha na tela 
        #self.imagem2.place(x=0,y=0,relwidth=1,relheight=1)
        self.lbl_palavra.place(x=420-100,y=300)
        self.chute.place(x=380,y=470)
        self.resultado.place(x=320,y=200)
        self.lbl_tentativas.place(x=10, y=370)
        self.btn_chutar.place(x=380,y=500)


    def tentar(self):
        
        self.letra = self.chute.get().upper()
        self.chute.delete(0,END)
        if self.letra in self.palavra:
            for i,l in enumerate(self.palavra):
                if l==self.letra:
                    self.descoberta[i]= self.letra
            self.acerto.play()
        else:
            self.chances -= 1


        self.update()

        if "_" not in self.descoberta:
            self.resultado["text"] = "Você venceu! "
            self.btn_chutar["state"] = "disabled"
        
        elif self.chances == 0:
            self.resultado["text"] = f"Voce perdeu! Palavra: {self.palavra}"
            self.btn_chutar["state"] = "disabled"

    def update(self):
        self.lbl_palavra["text"]=" ".join(self.descoberta)
        self.lbl_tentativas["text"] = f"Tentativas restantes: {self.chances}"
        
        

app = Jogo()

app = Jogo()

