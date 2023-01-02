from playlist import ListaPlaylist
class Cliente:
    def __init__(self,nit,nombre,usuario,clave,direccion,correo,empresa) :
        self.nit=nit
        self.nombre=nombre
        self.usuario=usuario
        self.clave=clave
        self.direccion=direccion
        self.correo=correo
        self.empresa=empresa
        self.playlist=ListaPlaylist()
class ListaCliente:
    def __init__(self) -> None:
        self.Clientes=[]
    def AgregarCliente(self,nity,nombrey,usuarioy,clavey,direcciony,correoy,empresay):
        nuevo=Cliente(nity,nombrey,usuarioy,clavey,direcciony,correoy,empresay)
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
        return False