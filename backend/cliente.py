from playlist import ListaPlaylist
Listap=ListaPlaylist()
class Cliente:
    def __init__(self,nit,nombre,usuario,clave,direccion,correo,idempresa) :
        self.nit=nit
        self.nombre=nombre
        self.usuario=usuario
        self.clave=clave
        self.direccion=direccion
        self.correo=correo
        self.idempresa=idempresa
        self.playlist=[]
    def dump(self): 
        return {
            "nit": self.nit,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "clave": self.clave,
            "direccion": self.direccion,
            "correo": self.correo,
            "idempresa":self.idempresa,
            "playlist":self.playlist
              }
class ListaCliente:
    
    def __init__(self) :
        self.Clientes=[]
        self.Playlist=[]
    def AgregarCliente(self,nity,nombrey,usuarioy,clavey,direcciony,correoy,idempresa):
        nuevo=Cliente(nity,nombrey,usuarioy,clavey,direcciony,correoy,idempresa)
        self.Clientes.append(nuevo)
        return nuevo.dump()
    def LeerCliente(self):
        ClienteJSON = []
        for producto in self.Clientes:
            ClienteJSON.append(producto.dump())
        return ClienteJSON
    def deleteCliente(self, id):
        for producto in self.Clientes:
            if producto.nit == id:
                self.Clientes.remove(producto)
                return True
    def BuscarCliente(self, id):
        for producto in self.Clientes:
            if producto.nit == id:
                return producto
        #return False
    def BuscarEmpresa(self, id):
        clientesarr=[]
        
        for cliente in self.Clientes:
            if cliente.idempresa == id:
                clientesarr.append(cliente)
        return clientesarr

    def Agregaplaylectura(self,objeto,idb):
     for cliente in self.Clientes:
            if cliente.nit == idb:
                cliente.playlist=objeto

    def ImprimirClientes(self):
        print("Clientes")
        print("------------------------")
        for clientes in self.Clientes:
            print(str(clientes.nit))
            #print("play "+str(clientes.playlist.categoria))

            for playlist in clientes.playlist:
                print(playlist.idP)
                print ("inicio play")
                print(playlist.canciones.ImprimirCancion())
                print ("fin play")
    """def AgregandoPlaylist(self,array, idplay):
        for playlist in array:"""

                

