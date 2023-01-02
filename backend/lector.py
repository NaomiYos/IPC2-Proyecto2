import xml.etree.cElementTree as ET
from playlist import ListaPlaylist
from cancion import ListaCancion
from cliente import ListaCliente
ListP=ListaPlaylist()
ListCliente=ListaCliente()
class Lectura():
    def cargarArchivo(self,ruta):
        Tree=ET.parse(ruta)
        raiz=Tree.getroot()
        for objeto in raiz:
            for playlist in objeto.iter('playlistClientes'):
                for play in playlist:
                    
                    #print(play.attrib["id"])
                    for nitcliente in play.iter("nitCliente"):
                        nitC=nitcliente.text
                        #print(nitcliente.text)
                    for vynil in play.iter("vinyl"):
                        vynilP=vynil.text
                        #print(vynil.text)
                    for categoria in play.iter("categoria"):
                        catP=categoria.text
                        #print(categoria.text)
                    ListP.AgregarPlaylist(play.attrib["id"],nitC,vynilP,catP)
                    print("PPlaylist "+play.attrib["id"]+nitC+vynilP+catP)
                    objetoplay=ListP.BuscarPlaylist(play.attrib["id"])
                    for canciones in play.iter("canciones"):

                        for cancion in canciones.iter("cancion"):
                            print("cancion " +cancion.attrib["id"])
                            for nombrecancion in cancion.iter("nombre"):
                                print(nombrecancion.text)
                            for anio in cancion.iter("anio"):
                                acancion=anio.text
                            for artista in cancion.iter("artista"):
                                artistC=artista.text
                            for genero in  cancion.iter("genero"):
                                generoC=genero.text
                            objetoplay.canciones.AgregarCancion(cancion.attrib["id"],nombrecancion.text,acancion,artistC,generoC)
                            print(cancion.attrib["id"]+nombrecancion.text+acancion+artistC+generoC)
                    #print("PPlaylist "+play.attrib["id"]+nitC+vynilP+catP)

                    

            for listc in objeto.iter('listaClientes'):
                for cliente in listc:
                    print("cliente"+cliente.attrib["nit"])
                    for nombrecliente in cliente.iter("nombre"):
                        namecliente=nombrecliente.text
                    for usuariocliente in cliente.iter("usuario"):
                        usuario=usuariocliente.text
                    for clavecliente in cliente.iter("clave"):
                        clave=clavecliente.text
                    for dircliente in cliente.iter("direccion"):
                        direccion=dircliente.text
                    for correocliente in cliente.iter("correo"):
                        correo=correocliente.text
                    for empresacliente in  cliente.iter("empresa"):
                        empresacli=empresacliente.text
                    ListCliente.AgregarCliente(cliente.attrib["nit"],namecliente,usuario,clave,direccion,correo,empresacli)
                    
                    for playlistcliente in cliente.iter("playlistsAsociadas"):
                        for playcl in playlistcliente.iter("playlist"):
                            playencontrada=ListP.BuscarPlaylist(playcl.text)
                            
                            print(playcl.text)
            for listempresa in objeto.iter('listaEmpresas'):
                for empresa in listempresa:
                     print("empresa id"+empresa.attrib["id"])
                     for ne in empresa.iter("nombre"):
                        
                        print(ne.text)
        ListP.Imprimir()




l=Lectura()
l.cargarArchivo("archivop.xml")