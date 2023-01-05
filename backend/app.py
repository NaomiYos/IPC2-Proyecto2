from flask  import Flask, json, request, jsonify
import xml.etree.cElementTree as ET
from flask_cors import CORS
from playlist import ListaPlaylist
from cliente import ListaCliente
from empresa import ListaEmpresa
from cancion import ListaCancion
ListP=ListaPlaylist()
ListC=ListaCliente()
ListE=ListaEmpresa()
Songlist=ListaCancion()

# inicializar servidor flask

app= Flask(__name__)

CORS(app)

@app.route('/playlist', methods=["POST"])
def crearPlaylist():
    idP= request.json["idP"]
    vynil = request.json["vynil"]
    compacto = request.json["compacto"] 
    categoria = request.json["categoria"] 
    canciones= request.json["canciones"]
    
    
    res = ListP.AgregarPlaylist(idP, vynil, compacto, categoria)
    ListP.AgregarCancionIndividual( idP,canciones)
    return jsonify({ "mensaje": "playlist creado con exito", "data": res}), 201
@app.route('/playlist', methods=["GET"])
def getplaylists():
    return jsonify({"data": ListP.LeerPlaylist()})

@app.route('/playlist', methods=["DELETE"])
def deletePlaylist():
    idP = request.json["idP"]

    resultado = ListP.deletePlaylist(idP)

    if resultado:
        return jsonify({ "mensaje": "Playlist con id " + str(idP) + " eliminado con éxito" }), 200
    else:
        return jsonify({ "mensaje": "Playlist no encontrado" }), 404
#--------------------------------------------------------------------------------
@app.route('/cancion', methods=["POST"])
def crearCancion():
    
    idP2= request.json["id"]
    idc = request.json["idc"]
    nombre=request.json["nombre"]
    anio = request.json["anio"] 
    artista = request.json["artista"] 
    genero= request.json["genero"]
    
    
    res = ListP.AgregarCancionP(idP2,idc,nombre,anio,artista,genero)
    
    return jsonify({ "mensaje": " creado con exito", "data": res}), 201
@app.route('/cancion', methods=["GET"])
def getcanciones():
    return jsonify({"data": Songlist.LeerCancion()})

@app.route('/cancion', methods=["DELETE"])
def deleteCancion():
    idP = request.json["id"]

    resultado = Songlist.deleteCancion(idP)

    if resultado:
        return jsonify({ "mensaje": "Cancion con id " + str(idP) + " eliminado con éxito" }), 200
    else:
        return jsonify({ "mensaje": "Cancion no encontrado" }), 404
#--------------------------------------------------------------------------------------------------------
@app.route('/cliente', methods=["POST"])
def crearCliente():
   
    
    nit= request.json["nit"]
    nombre=request.json["nombre"]
    usuario = request.json["usuario"] 
    clave = request.json["clave"] 
    direccion= request.json["direccion"]
    correo= request.json["correo"]
    empresa=request.json["empresa"]
    playlist=request.json["playlist"]

    
    
    res = ListC.AgregarCliente(nit,nombre,usuario,clave,direccion,correo,empresa)
    objetocliente=ListC.BuscarCliente(nit)
    ListE.AsignarClienteE(objetocliente,nit)
    for p in playlist:
        objetoplay=ListP.BuscarPlaylists(p)
        objetocliente.playlist.append(objetoplay)
    return jsonify({ "mensaje": " creado con exito", "data": res}), 201

@app.route('/cliente', methods=["GET"])
def getclientes():
    return jsonify({"data": ListC.LeerCliente()})

@app.route('/cliente', methods=["DELETE"])
def deleteCliente():
    idP = request.json["id"]

    resultado = ListC.deleteCliente(idP)

    if resultado:
        return jsonify({ "mensaje": "Cliente con id " + str(idP) + " eliminado con éxito" }), 200
    else:
        return jsonify({ "mensaje": "Cliente no encontrado" }), 404

#--------------------------------------------------------------------------------------------------------------      

@app.route('/empresa', methods=["POST"])
def crearEmpresa():
    
    
    idE= request.json["id"]
    nombre=request.json["nombre"]

    
    
    res = ListE.AgregarEmpresa(idE,nombre)
    return jsonify({ "mensaje": " creado con exito", "data": res}), 201

@app.route('/empresa', methods=["GET"])
def getempresa():
    return jsonify({"data": ListE.LeerEmpresa()})
@app.route('/empresa', methods=["DELETE"])
def deleteEmpresa():
    idP = request.json["id"]

    resultado = ListE.deleteEmpresa(idP)

    if resultado:
        return jsonify({ "mensaje": "Empresa con id " + str(idP) + " eliminado con éxito" }), 200
    else:
        return jsonify({ "mensaje": "Empresa no encontrado" }), 404


@app.route('/cargamasiva',methods=['POST'])
def CargaMasiva():
        xml=request.data.decode('utf-8')
        raiz=ET.XML(xml)
        for objeto in raiz:
            for playlist in objeto.iter('playListCs'):
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
                    ListP.AgregarPlaylist(play.attrib["id"],nitC,vynilP,catP,"")
                   # print("PPlaylist "+play.attrib["id"]+nitC+vynilP+catP)
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
                    #print("PPlaylist "+play.attrib["id"]+nitC+vynilP+catP)

                    

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
                    ListC.AgregarCliente(nit,namecliente,usuario,clave,direccion,correoc,empresacli)
                
                    for playListC in cliente.iter("playlistsAsociadas"):
                        for playcl in playListC.iter("playlist"):
                          
                            #ListC.AgregandoPlay()
                            playencontrada=ListP.BuscarPlaylists(playcl.text)                            
                            if playencontrada is not None: 
                                pclientes.append(playencontrada)
                        ListC.Agregaplaylectura(pclientes,nit)
                            
            for listempresa in objeto.iter('listaEmpresas'):
                for empresa in listempresa:
                     idempresa=empresa.attrib["id"]
                     for ne in empresa.iter("nombre"):
                        nempresa=ne.text
                     ListE.AgregarEmpresa(idempresa,nempresa)
                     cliententrontrado=ListC.BuscarEmpresa(idempresa)
                     for cliente in cliententrontrado:
                        ListE.AsignarClienteE(cliente,idempresa)
                     
                     print("idempresa "+idempresa+" nombre empresa "+nempresa)
        ListP.Imprimir()
        ListC.ImprimirClientes()
        respuesta=ListE.LeerEmpresa()
        if respuesta is not None:
            return jsonify({'ok':True,'message':'Canciones cargadas con exito'}),200
if __name__== '__main__':
    app.run(debug=True, port=3000)