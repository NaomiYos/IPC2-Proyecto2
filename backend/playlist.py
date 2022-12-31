from cancion import  Cancion
class Playlist:
    def __init__(self,idP,vynil,compacto,categoria) :
        self.idP=idP
        self.vynil=vynil
        self.compacto=compacto
        self.categoria=categoria
    def dump(self): 
        return {
            "idP": self.idP,
            "vynil": self.vynil,
            "compacto": self.compacto,
            "categoria": self.categoria
        }
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
        return False