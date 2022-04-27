from faulthandler import disable
from tkinter import *
from tkinter import ttk
import tkinter as tk  
from click import command
from analizador_Lexico import lexico


rojo="#A93226"
Font="Arial"
alto=3
largo=20




class Visual():


    def __init__(self) -> None:
        #encabzado para tkinter
        self.raiz = Tk()
        self.Ventana_Principal()
        self.analizador_lexico = lexico()

    def comp(self):
        #Sirve como parte final para tkinter
        self.raiz.mainloop()

    def Ventana_Principal(self):
        #Partes para el tkinter
        #nombre ventana y tamaño
        self.raiz.title("La Liga Bot")
        self.raiz.geometry("700x550")
        #Para hacerlo resposive
        self.raiz.rowconfigure(0, weight=1)
        self.raiz.columnconfigure(0 , weight=1)

        framemain= ttk.Frame(self.raiz)
        framemain.grid(row=0 , column=0, sticky=NSEW)
        framemain.rowconfigure(1, weight=1)
        #framemain.columnconfigure(0 , weight=1)
    #19.00
        frameCuerpo= ttk.Frame(framemain)
        frameCuerpo.grid(row=1 , column=1, sticky=NSEW)
        frameCuerpo.rowconfigure(1, weight=1)
        frameCuerpo.columnconfigure(1 , weight=2)
        #Cuerpo
        #Menu( para los Botones)
        
        menu=ttk.Frame(frameCuerpo, borderwidth=10 )
        menu.grid(row=1, column=2,sticky=EW)
        

        #Texto del tkinter
        self.texto =tk.Text(frameCuerpo, width=60, height=2, bg='pale green', fg=rojo ,Font=None, padx=5, pady=5)
        self.texto.grid(row=1,column=1,sticky=NSEW)
        self.texto.configure(cursor="arrow", state=DISABLED)

        # Pie de pagina
        framePie =ttk.Frame(framemain, borderwidth=5)
        framePie.grid(row=2, column=1,sticky=EW)
        framePie.columnconfigure(1,weight=1)


        self.msgEntry = tk.Entry(framePie, bg='green yellow',fg=None, font=Font)
        self.msgEntry.place(relwidth=0.74, relheight=0.06,rely=0.008, relx=0.011)
        self.msgEntry.focus()
        self.msgEntry.bind("<Return>")
        self.msgEntry.grid(row=1, column=1, sticky=NSEW)

        #Botones
        Button_Enviar= tk.Button(framePie,  text="Enviar", font=Font, bg="gold",command=lambda: self.boton_Enviar(None))
        Button_Enviar.grid(row=1, column=2, sticky=NSEW)
        
        bttn_Reporte_Errores= tk.Button(menu,width=largo, height=alto, text="Reporte de errores", font=Font, bg="khaki1",command=lambda: self.boton_Enviar(None))
        bttn_Reporte_Errores.grid(row=1, column=5, sticky=NSEW)

        bttn_limpiar_log_errores= tk.Button(menu,width=largo, height=alto, text="Limpiar log de errores", font=Font, bg="khaki1",command=lambda: self.boton_Enviar(None))
        bttn_limpiar_log_errores.grid(row=2, column=5, sticky=NSEW)

        bttn_Reporte_tokens= tk.Button(menu,width=largo, height=alto, text="Reporte de tokens", font=Font, bg="khaki1",command=lambda: self.reporte_de_tokens(None))
        bttn_Reporte_tokens.grid(row=3, column=5, sticky=NSEW)

        bttn_limpiar_log_tokens= tk.Button(menu,width=largo, height=alto, text="Limpiar log de tokens", font=Font, bg="khaki1",command=lambda: self.limpiar(None))
        bttn_limpiar_log_tokens.grid(row=4, column=5, sticky=NSEW)

        bttn_Manual_Usuario= tk.Button(menu,width=largo, height=alto, text="Manual de usuario", font=Font, bg="khaki1",command=lambda: self.boton_Enviar(None))
        bttn_Manual_Usuario.grid(row=5, column=5, sticky=NSEW)

        bttn_Manual_Tecnico= tk.Button(menu,width=largo, height=alto, text="Manual tecnico", font=Font, bg="khaki1",command=lambda: self.boton_Enviar(None))
        bttn_Manual_Tecnico.grid(row=6, column=5, sticky=NSEW)

        



        
    def boton_Enviar(self, event):
        msg = self.msgEntry.get()
        self.mensaje_usuario(msg, "Usuario")
    
    def reporte_de_tokens(self, event):
        self.analizador_lexico.analizar()
        self.analizador_lexico.genrarReporteToken()
        print("Se genero el reporte de tokens")

    def limpiar(self, event):
        self.analizador_lexico = lexico()

        

    def mensaje_usuario(self, msg, sender):
        if not msg:
            return

        self.msgEntry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.texto.configure(state=NORMAL)
        self.texto.insert(END, msg1)
        self.texto.configure(state=DISABLED)

        if msg == 'ADIOS':
            respuesta = 'ADIOS'
            bot_name = "Bot"
            msg2 = f"{bot_name}: {respuesta}\n\n"
            self.texto.configure(state=NORMAL)
            self.texto.insert(END, msg2)
            self.texto.configure(state=DISABLED)

            self.texto.see(END)
        else:
            bot_name = "Bot"
            respuesta = self.leer_mensaje(msg)
            msg2 = f"{bot_name}: {respuesta}\n\n"
            self.texto.configure(state=NORMAL)
            self.texto.insert(END, msg2)
            self.texto.configure(state=DISABLED)

            self.texto.see(END)

        if respuesta == 'ADIOS':
            self.raiz.destroy()

    def leer_mensaje(self,msg):
        self.analizador_lexico = lexico()
        self.analizador_lexico.analizar()
        if msg != '':
            cadena = anali_lexico.analizador(msg)
            return cadena

    








