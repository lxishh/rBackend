#Importar
# from ARCHIVO import CLASE
from Equipo import Equipo

# Equipo() está llamando al __init__; por eso nos pide atributos
# Deben existir variables para almacenar la clase (en memoria)
e1 = Equipo("Lakers", "Angeles", 16,"Nike")

print(e1)
#se usa la función creada en el archivo Equipo (mostrar_datos)
print(e1.mostrar_datos())