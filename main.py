from tkinter import *
#from PIL import image, imageTk


class Jogo:
    def __init__(self):
        
        self.tela = Tk()
       
        self.tela.geometry("800x600")
        self.tela.title("Jogo da Forca")
        self.tela['bg']="white"
        self.tela.resizable(False,False)
        
        
        #carrega todas as imagens 
        '''
        self.fundo = image.open("/imagens/telainicial-fundo.png")
        self.fundo = self.fundo.resize((700,500))
        self.fundo_tk = ImageTk.PhotoImage(self.fundo)
        
'''
        self.palavra = "Python"
        self.descoberta = ["_"] * len(self.palavra)
        self.palavras_errada = []
        self.chances = 6

        self.fundo = PhotoImage(file="imagens/telainicial-fundo.png")
        
        
        #construo todos os botões e textos 
        self.imagem = Label(self.tela,image = self.fundo)
        self.titulo = Label(self.tela, text="Jogo da Forca", fg="black",font=('Tahoma',12,'bold'))
        
        self.btn_iniciar = Button(self.tela,text="INICIAR JOGO",fg='black',command=self.iniciarjogo,relief="flat")
        
        
        
        
        #desenho todos botões e textos
        self.imagem.place(x=0,y=0,relwidth=1,relheight=1)
        self.titulo.pack(pady=(80,10))
        self.btn_iniciar.pack(pady=(350,20))

        self.tela.mainloop() # faz o código rodar
        
    def iniciarjogo(self):
      self.apaga_tudo() #apaga tudo da tela 
      
      self.palavra = Label(self.tela,text=" ".join(self.descoberta),font=("Arial",14,"bold"),bg="white")
      self.chute = Entry(self.tela,width=10)
      self.lbl_tentativas = Label(self.tela, text= f"Tentativas: {self.chances}",font=("Arial",6))
      self.btn_chutar = Button(self.tela, text="Chutar",font=("Arial",6),relief="flat")
      
      
      
      #manda desenha na tela 
      self.palavra.place(x=400-100,y=300)
      self.chute.place(x=300,y=480)
      self.lbl_tentativas.place(x=10, y=370)
      self.btn_chutar.place(x=480,y=470)
   
    def apaga_tudo(self):
        self.titulo. destroy()
        self.btn_iniciar.destroy()
        self.imagem.place_forget()
        
        
        
app = Jogo()