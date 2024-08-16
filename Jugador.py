class Jugador:
    def __init__(self,nombre,nacionalidad,estatura):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__estatura = estatura

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_nacionalidad(self,nacionalidad):
        self.__nacionalidad = nacionalidad

    def set_estatura(self,estatura):
        self.__estatura = estatura

    def get_nombre(self):
        return self.__nombre
    
    def get_nacionalidad(self):
        return self.__nacionalidad
    
    def get_estatura(self):
        return self.__estatura
    
    def __str__(self):
        return "Nombre:"+self.__nombre
    