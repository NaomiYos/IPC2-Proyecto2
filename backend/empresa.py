from cliente import ListaCliente
class Empresa:
    def __init__(self,idE,nombre):
        self.idE=idE
        self.nombre=nombre
        self.trabajadores=[]
        #self.factura=0
    def dump(self): 
        return {
            "idE": self.idE,
            "nombre": self.nombre,
            "Trabajadores": self.trabajadores,
            #"factura": self.factura,
              }
class ListaEmpresa:
    def __init__(self):
        self.Empresas=[]
    def AgregarEmpresa(self,idEx,nombrex):
        nuevo=Empresa(idEx,nombrex)
        self.Empresas.append(nuevo)
        return nuevo.dump()
    def LeerEmpresa(self):
        EmpresaJSON = []
        for producto in self.Empresas:
            EmpresaJSON.append(producto.dump())
        return EmpresaJSON
    def deleteEmpresa(self, id):
        for producto in self.Empresas:
            if producto.idc == id:
                self.Empresas.remove(producto)
                return True
        return False
    def AsignarClienteE(self,objeto,empresaid):
        for empresa in self.Empresas:
            if empresa.idE==empresaid:
                empresa.trabajadores.append(objeto)
    def ImprimirEmpresa(self):
        print("Empresa")
        print("------------------------")
        for empresas in self.Empresas:
            print(str(empresas.idE))
            #print("play "+str(Empresas.playlist.categoria))

            for cliente in empresas.trabajadores:
                print("cliente nit "+cliente.nit)
                for playlist in cliente.playlist:
                    print("playlist id "+playlist.idP)
                    print(playlist.canciones.ImprimirCancion())

