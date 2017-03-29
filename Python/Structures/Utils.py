from Structures import SparseMatrix

class Matriz(object):
    def __init__(self):
        self.matriz = SparseMatrix()

    def login(self, empresa, departamento, usuario, contrasenna):
        sesion = self.matriz.search(empresa, departamento, usuario)
        if sesion is None:
            return None
        elif sesion.user.password == contrasenna:
            return sesion
        else:
            return None

    def agregarUsuario(self, empresa, departamento, usuario, nombre, contrasenna):
        self.matriz.insert(empresa, departamento, usuario, nombre, contrasenna)
        return self.matriz.search(empresa, departamento, usuario)

    def agregarActivo(self, empresa, departamento, usuario, id, nombre, descripcion):
        sesion =  self.matriz.search(empresa, departamento, usuario)
        if sesion is not None:
            activo = sesion.tree.insert(id, nombre, descripcion)
            if activo is not None:
                return activo
            else:
                return None
        else:
            return None

    def borrarActivo(self, empresa, departamento, usuario, id):
        sesion = self.matriz.search(empresa, departamento, usuario)
        if sesion is not None:
            activo = sesion.tree.delete(id)
            if activo is not None:
                return activo
            else:
                return None
        else:
            return None

    def modificarActivo(self, empresa, departamento, usuario, id, nombre, descripcion):
        sesion = self.matriz.search(empresa, departamento, usuario)
        if sesion is not None:
            activo = sesion.tree.search(id)
            if activo is not None:
                activo.asset.name = nombre
                activo.asset.desc = descripcion
                return activo
            else:
                return None
        else:
            return None

    def activosUsuario(self, empresa, departamento, usuario):
        sesion = self.matriz.search(empresa, departamento, usuario)
        if sesion is not None:
            if sesion.tree.head is not None:
                return sesion.tree.traversal(0)
            else:
                return None
        else:
            return None
