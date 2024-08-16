# Crear clase (en Mayus)
class Equipo:
    #definir __init__, con un self, para hacer referencia a si mismo, y luego los atributos
    #definir tipo de dato (para ayudar luego en el main)
    def __init__(self, nombre:str, ciudad:str, campeonatos, sponsor):
        #self.__ (atributo privado) 
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__campeonatos = campeonatos
        self.__sponsor = sponsor
        self.__jugadores = []

    #set: asignar a un atributo. (depues de haber creado el objeto)
    #su función es actualizar o agregar un atributo (en caso de que no exista)
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad

    def set_campeonatos(self,campeonatos):
        self.__campeonatos = campeonatos

    def set_sponsor(self,sponsor):
        self.__sponsor = sponsor


    #Carga masiva inicial
    def set_jugadores(self,jugadores):
        self.__jugadores = jugadores
        

    #get: devolver valor
    def get_nombre(self):
        return self.__nombre
    
    def get_ciudad(self):
        return self.__ciudad
    
    def get_campeonatos(self):
        return self.__campeonatos
    
    def get_sponsor(self):
        return self.__sponsor
    
    def get_jugadores(self):
        return self.__jugadores
    
    #str
    def __str__(self):
        return "Nombre:"+self.__nombre
    
    def mostrar_datos(self):
        txt = ""
        txt += "Nombre:"+self.__nombre
        txt += "\nCiudad:"+self.__ciudad
        return txt
    
    #funciónes para la clase Jugador (objeto)
    def contratar_jugadores(self,jugador):
        if jugador in self.__jugadores:
            print("El jugador ya está contratado")
        else:
            self.__jugadores.append(jugador)

    def despedir_jugador(self,jugador):
        if jugador not in self.__jugadores:
            print("El jugador no está en el equipo")
        else:
            self.__jugadores.remove(jugador)