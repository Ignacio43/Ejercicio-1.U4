from tkinter import * 
import tkinter as tk
from tkinter import ttk
class Aplicacion(tk.Tk):
    __ventana=None
    def __init__(self):
        self.__lista=[]
        
        #Ventana 
        self.__ventana=Tk()
        self.__ventana.geometry('600x270')
        self.__ventana.title("Calculadora IPC")
        
        
        #Atributos Label
        opts = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
        
        #Fila
        
        tk.Label(text="Item").grid(row=0,column=0,**opts)
        tk.Label(text="Vestimenta").grid(row=1,column=0,**opts)
        tk.Label(text="Alimentos").grid(row=2,column=0,**opts)
        tk.Label(text="Educacion").grid(row=3,column=0,**opts)
        
       #Columna
       
        tk.Label(text="Cantidad").grid(row=0,column=1,**opts)
        tk.Label(text="Precio Año Base").grid(row=0,column=2,**opts)
        tk.Label(text="Precio Año Actual").grid(row=0,column=3,**opts)

        #Entrys
        
        for i in range(3):
            fila=[]
            for j in range(3):
                dato = tk.StringVar()
                tk.Entry(textvariable=dato).grid(row=i+1,column=j+1,**opts)
                fila.append(dato)
            self.__lista.append(fila)
            
         #Atributos Botones 
        
        Boton = {"width":9, "height":1}
        
        #Botones
        
        tk.Button( text = "Calcular IPC", **Boton, command = self.calcula).grid(row = 4, column = 1)
        tk.Button( text = "Salir", **Boton, command = self.__ventana.destroy).grid(row = 4, column = 2)
        
        self.__ventana.mainloop()
        
    def calcula(self):
        band=True
        datoActual = 0
        datoBase = 0
        attributes = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
        for fila in  self.__lista:
            for dato in fila:
                if band:
                    multiplicador = int(dato.get())
                    band = False
                elif fila.index(dato) == 1:
                    datoBase += int(dato.get()) * multiplicador
                else:
                    datoActual += int(dato.get()) * multiplicador
            band = True
        tk.Label(text = "IPC " + str(int(datoBase)*100) + " % " + str(int(datoActual)*100) + " % ").grid(row = 7, column = 1, **attributes)
        
                          

if __name__=='__main__':
    aplicacion=Aplicacion()
  