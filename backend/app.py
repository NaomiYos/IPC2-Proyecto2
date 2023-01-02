from flask  import Flask, json, request, jsonify
import xml.etree.cElementTree as ET
from flask_cors import CORS
from playlist import ListaPlaylist
ListP=ListaPlaylist()

# inicializar servidor flask

app= Flask(__name__)

CORS(app)

@app.route('/playlist', methods=["POST"])
def crearPlaylist():
    idP= request.json["idP"]
    vynil = request.json["vynil"]
    compacto = request.json["compacto"] 
    categoria = request.json["categoria"] 
    
    
    res = ListP.AgregarPlaylist(idP, vynil, compacto, categoria)
    return jsonify({ "mensaje": "playlist creado con exito", "data": res}), 201

@app.route('/playlist', methods=["GET"])
def getplaylists():
    return jsonify({"data": ListP.LeerPlaylist()})

@app.route('/playlist', methods=["DELETE"])
def deletePlaylist():
    idP = request.json["idP"]

    resultado = ListP.deletePlaylist(idP)

    if resultado:
        return jsonify({ "mensaje": "Usuario con id " + str(idP) + " eliminado con éxito" }), 200
    else:
        return jsonify({ "mensaje": "Usuario no encontrado" }), 404

@app.route('/agregarCanciones',methods=['POST'])
def agregarCanciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
    for elemento in raiz:
        gestor.agregar_cancion(elemento.attrib['name'],elemento.attrib['artist'],elemento.attrib['image'],elemento.text)
    return jsonify({'ok':True,'message':'Canciones cargadas con exito'}),200
if __name__== '__main__':
    app.run(debug=True, port=3000)