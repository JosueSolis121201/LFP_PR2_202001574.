class clase_token:
    def __init__(self,valor,columna,tipo,tieneErrorLexico=False):
        self.valor = valor
        self.tipo = tipo
        self.columna = columna
        self.tieneErrorLexico = tieneErrorLexico

    def html(self):
        return "<tr>" + "<td>"+ str(self.valor)+"</td>" + "<td>"+ str(self.tipo)+"</td>" + "<td>"+ str(self.columna)+"</td>"+"</tr>"

    def string(self):
        return self.valor + "---" + str(self.tipo) + "---" + str(self.columna)

    

class lexico():
    def __init__(self) -> None:
        self.texto=""
        self.lista_tokens=[]
        
        self.linea = 1
        self.columna = 1
        

    def genrarReporteToken(self):
        inicio="<html><head></head><body>"
        cuerpo = "<table><tr><th>TOKEN</th><th>TIPO</th><th>COLUMNA</th></tr><tbody>"
        concatenar = ""
        for element in self.lista_tokens:
            concatenar = concatenar + element.html()
        final = inicio + cuerpo  +concatenar+ "</tbody></table></html></body>"
        f = open ('report_202001574.html','w')
        f.write(final)
        f.close()
    
    def analizar(self):
        self.analizador()#!msg
    
    def analizador(self):
        msg="RESULTADO \"Real Madrid\" VS \"Villarreal\" TEMPORADA <2019-2020>"

        self.texto = msg
        while self.texto != "":
            letra = self.leer_letra()
            if letra.isalpha() : 
                lectura = self.letras_s0()
                tieneErrorLexico = False
                if lectura.upper() != lectura:
                    tieneErrorLexico = True
                self.columna = self.columna + len(lectura)
                self.lista_tokens.append(clase_token(lectura,self.columna,"palabra_reservada",tieneErrorLexico))
            elif letra == "\n" or letra == "\t" or letra == " ":   
                self.quitar_primera_letra()
                self.columna = self.columna+1 #TODO 5
            elif letra == "\"" or letra == "“" or letra == "”":  #TODO 4
                lectura = self.comillas_s0()
                self.columna = self.columna + len(lectura)
                self.lista_tokens.append(clase_token(lectura,self.columna,"Cadena"))
            elif letra == "<":
                self.quitar_primera_letra()
                self.columna = self.columna+1 #TODO 1
                self.lista_tokens.append(clase_token("<",self.columna,"menor_que"))
            elif letra.isnumeric() :            
                lectura = self.numero_s0()#TODO 8
                self.columna = self.columna + len(lectura)
                self.lista_tokens.append(clase_token(lectura,self.columna,"numero"))
            elif letra =="-" :            
                self.quitar_primera_letra()
                self.columna = self.columna+1 #TODO 1
                self.lista_tokens.append(clase_token("-",self.columna,"guion_alto"))
            elif letra == ">":
                self.quitar_primera_letra()
                self.columna = self.columna+1 #TODO 1
                self.lista_tokens.append(clase_token(">",self.columna,"mayor_que"))
        



       





    
    def leer_letra(self):
        if(self.texto != ""):
            return self.texto[0]
        else:
            return ""
    def quitar_primera_letra(self):
        if(self.texto != ""):
            self.texto=self.texto[1:]

    def numero_s0(self):
        letra = self.leer_letra()
        if letra.isnumeric():
            self.quitar_primera_letra()
            return letra + self.numero_s1()
    def numero_s1(self):
        letra = self.leer_letra()
        if letra.isnumeric():
            self.quitar_primera_letra()
            return letra + self.numero_s1()
        else:
            return "" 
    
    def letras_s0(self):
        letra = self.leer_letra()
        if letra.isalpha():                
            self.quitar_primera_letra()
            return letra + self.letras_s1()

    def letras_s1(self):
        letra = self.leer_letra()
        if letra.isalpha():
            self.quitar_primera_letra()
            return letra + self.letras_s1()
        else:
            return ""

    def comillas_s0(self):
        letra = self.leer_letra()
        if letra == '\"' or letra == "“" or letra == "”":
            self.quitar_primera_letra()
            
            return letra +  self.comillas_s1()

    
    def comillas_s1(self):
        letra = self.leer_letra()
        if letra != '\"'and letra != "“" and letra != "”":
            self.quitar_primera_letra()
            

            return letra + self.comillas_s1()
        else:
            self.quitar_primera_letra()
            return letra

    
a=lexico()
a.analizar()
a.genrarReporteToken()








        