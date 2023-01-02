from cancion import  ListaCancion
class Playlist:
    def __init__(self,idP,vynil,compacto,categoria) :
        self.idP=idP
        self.vynil=vynil
        self.compacto=compacto
        self.categoria=categoria
        self.canciones=ListaCancion()
    
    def dump(self): 
        return {
            "idP": self.idP,
            "vynil": self.vynil,
            "compacto": self.compacto,
            "categoria": self.categoria
        }
    def __repr__(self):
        return str(self.__dict__)
class ListaPlaylist:
    def __init__(self) -> None:
        self.Playlist=[]
    def AgregarPlaylist(self,id,vy,com,cat):
        nuevo=Playlist(id,vy,com,cat)
        self.Playlist.append(nuevo)
        return nuevo.dump()
    def LeerPlaylist(self):
        PlaylistJSON = []
        for producto in self.Playlist:
            PlaylistJSON.append(producto.dump())
        return PlaylistJSON
    def deletePlaylist(self, id):
        for producto in self.Playlist:
            if producto.idP == id:
                self.Playlist.remove(producto)
                return True
            else:
                return False
        
    def BuscarPlaylist(self, id):
        for play in self.Playlist:
            print(str(id))
            if play.idP == id:
                
                return play
    def Imprimir(self):
        print("------------------------")
        for play in self.Playlist:
            print(str(play.idP))
            play.canciones.ImprimirCancion()
           
            
        