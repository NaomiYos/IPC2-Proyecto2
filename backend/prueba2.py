from playlist import ListaPlaylist
from lectorinverso import Lectura
listp=ListaPlaylist()
lectorin=Lectura()

lectorin.cargarArchivo(r"C:\Users\Naomi Rashel\Documents\2dosemestre20222\vacas\ipc2\Proyecto2\backend\ArchivoP2.xml")
print("Imprimiendo lo que quiero")
listp.Imprimir()