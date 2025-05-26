from tkinter import *
#from PIL import image, imageTk


class Jogo:
    def __init__(self):
        
        self.tela = Tk()
       
        self.tela.geometry("800x600")
        self.tela.title("Jogo da Forca")
        self.tela['bg']='black'
        self.tela.resizable(False,False)
        
        
        #carrega todas as imagens 
        '''
        self.fundo = image.open("/imagens/telainicial-fundo.png")
        self.fundo = self.fundo.resize((700,500))
        self.fundo_tk = ImageTk.PhotoImage(self.fundo)

'''
        self.fundo = PhotoImage(file="imagens/telainicial-fundo.png")
        
        
        #construo todos os botões e textos 
        self.imagem = Label(self.tela,image = self.fundo)
        self.titulo = Label(self.tela, text="Jogo da Forca", fg="black",font=('Tahoma',14,'bold'))
        
        self.btn_iniciar = Button(self.tela,text="INICIAR JOGO",fg='grey')
        
        
        #desenho todos botões e textos
        self.imagem.place(x=0,y=0,relwidth=1,relheight=1)
        self.titulo.pack(pady=(80,10))
        self.btn_iniciar.pack(pady=(350,10))

        self.tela.mainloop()
        
    def iniciarjogo(self):
        pass
        
        
    def apaga_tudo(self):
        pass
        
        
        
app = Jogo()