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
            "categoria": self.categoria,
            "canciones":self.canciones.LeerCancion()
        }
   
class ListaPlaylist:
    def __init__(self) :
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
            
        
    def BuscarPlaylists(self, id):
        
        for play in self.Playlist:            
            if play.idP == id:
                return play
                
    def Imprimir(self):
        print("------------------------")
        for play in self.Playlist:
            print(str(play.idP))
            play.canciones.ImprimirCancion()
    
    def AgregarCancionIndividual(self,idplay,canciones):
      
        
            for play in self.Playlist:            
                if play.idP == idplay:
                #play.canciones.AgregarCancion(idplay,cancion)
                    for cancion in canciones:
                        play.canciones.AgregarCancion( cancion['id'], cancion['nombre'], cancion['anio'], cancion['artista'],cancion['genero'])
                #return self.readProductos()
    def AgregarCancionP(self,idplay,idc,namecancion,acancion,artistC,generoC):
      
        
            for play in self.Playlist:            
                if play.idP == idplay:
                #play.canciones.AgregarCancion(idplay,cancion)
                
                    play.canciones.AgregarCancion( idc,namecancion,acancion,artistC,generoC)
                #return self.readProductos()
    def Obtenerlista(self):
        return self.Playlist     
        