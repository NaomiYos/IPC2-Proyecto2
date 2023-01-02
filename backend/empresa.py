from cliente import ListaCliente
class Empresa:
    def __init__(self,idE,nombre) -> None:
        self.idE=idE
        self.nombre=nombre
        self.trabajadores=ListaCliente()
class ListaEmpresa:
    def __init__(self) -> None:
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