class Cancion:
    def __init__(self,idc,nombre,anio,artista,genero) :
        self.idc=idc
        self.nombre=nombre
        self.anio=anio
        self.artista=artista
        self.genero=genero
    def dump(self): 
        return {
            "idc": self.idc,
            "nombre": self.nombre,
            "anio": self.anio,
            "artista": self.artista,
            "genero": self.genero,
            

        }
    def __str__(self):
        return f'Name: {self.nombre}'
   
class ListaCancion:
    def __init__(self) -> None:
        self.Canciones=[]
    def AgregarCancion(self,idcr,nombrer,anior,artistar,generor):
        nuevo=Cancion(idcr,nombrer,anior,artistar,generor)
        self.Canciones.append(nuevo)
        return nuevo.dump()
    def LeerCancion(self):
        CancionJSON = []
        for producto in self.Canciones:
            CancionJSON.append(producto.dump())
        return CancionJSON
    def deleteCancion(self, id):
        for producto in self.Canciones:
            if producto.idc == id:
                self.Canciones.remove(producto)
                return True
        return False
    def ImprimirCancion(self):
        for cancion in self.Canciones:
        
           print("cancion "+str(cancion.idc)+str(cancion.nombre))