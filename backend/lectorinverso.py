import xml.etree.cElementTree as ET
from playlist import ListaPlaylist
from cancion import ListaCancion
from cliente import ListaCliente
from empresa import ListaEmpresa
LisEmpresa=ListaEmpresa()
ListP=ListaPlaylist()
ListCliente=ListaCliente()
class Lectura():
     def cargarArchivo(self,ruta):
        Tree=ET.parse(ruta)
        raiz=Tree.getroot()
        for objeto in raiz:
            for listempresa in objeto.iter('listaEmpresas'):
                for empresa in listempresa:
                     idempresa=empresa.attrib["id"]
                     for ne in empresa.iter("nombre"):
                        nempresa=ne.text
                     cliententrontrado=ListCliente.BuscarEmpresa(idempresa)
                     LisEmpresa.AgregarEmpresa(idempresa,nempresa)
                     print("idempresa "+idempresa+" nombre empresa "+nempresa)
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
                    #print("PPlaylist "+play.attrib["id"]+nitC+vynilP+catP)
                    #objetoplay=ListP.BuscarPlaylist(play.attrib["id"])
                    
                    for canciones in play.iter("canciones"):

                        for cancion in canciones.iter("cancion"):
                            #print("cancion " +cancion.attrib["id"])
                            for nombrecancion in cancion.iter("nombre"):
                                namecancion=nombrecancion.text
                                #print(nombrecancion.text)
                            for anio in cancion.iter("anio"):
                                acancion=anio.text
                            for artista in cancion.iter("artista"):
                                artistC=artista.text
                            for genero in  cancion.iter("genero"):
                                generoC=genero.text
                            
                            
                            ListP.AgregarCancionP(play.attrib["id"],cancion.attrib["id"],namecancion,acancion,artistC,generoC)
                            #print(cancion.attrib["id"]+nombrecancion.text+acancion+artistC+generoC)
            Listaobtenida=ListP.Obtenerlista()        #print("PPlaylist "+play.attrib["id"]+nitC+vynilP+catP)

                    

            for listc in objeto.iter('listaClientes'):
                pclientes=[]
                for cliente in listc:
                    nit=cliente.attrib["nit"]
                    for nombrecliente in cliente.iter("nombre"):
                        namecliente=nombrecliente.text
                    for usuariocliente in cliente.iter("usuario"):
                        usuario=usuariocliente.text
                    for clavecliente in cliente.iter("clave"):
                        clave=clavecliente.text
                    for dircliente in cliente.iter("direccion"):
                        direccion=dircliente.text
                    for correocliente in cliente.iter("correoElectronico"):
                        correoc=correocliente.text
                    for empresacliente in  cliente.iter("empresa"):
                        empresacli=empresacliente.text
                    LisEmpresa.AgregarCliente(idempresa,nit,namecliente,usuario,clave,direccion,correoc,empresacli))
                    ListCliente.AgregarCliente(nit,namecliente,usuario,clave,direccion,correoc,empresacli)
                
                    for playlistcliente in cliente.iter("playlistsAsociadas"):
                        for playcl in playlistcliente.iter("playlist"):
                          
                            #ListCliente.AgregandoPlay()
                            playencontrada=ListP.BuscarPlaylists(playcl.text)                            
                            if playencontrada is not None: 
                                pclientes.append(playencontrada)
                        ListCliente.Agregaplaylectura(pclientes,nit)
                            
           
        #ListP.Imprimir()
        #ListCliente.ImprimirClientes()




