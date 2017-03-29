from flask import Flask, request, Response
from Utils import Matriz

app = Flask("EDD_Proyecto1")

usuarios = Matriz()

@app.route('/agregarUsuario', methods=['POST'])
def agregarUsuario():
    empresa = request.form['empresa']
    departamento = request.form['departamento']
    usuario = request.form['usuario']
    nombre = request.form['nombre']
    contrasenna = request.form['contrasenna']
    creado = usuarios.agregarUsuario(empresa, departamento, usuario, nombre, contrasenna)
    if creado is not None:
        print("Se ha agregado " + str(creado) + " con exito")
        return str(creado)
    else:
        return None

@app.route('/login', methods=['POST'])
def login():
    empresa = request.form['empresa']
    departamento = request.form['departamento']
    usuario = request.form['usuario']
    contrasenna = request.form['contrasenna']
    logueado = usuarios.login(empresa, departamento, usuario, contrasenna)
    if logueado is not None:
        print("Se ha logueado " + str(logueado) + " con exito")
        return "Existe"
    else:
        return "No existe"

@app.route('/agregarActivo', methods=['POST'])
def agregarActivo():
    def agregarActivo():
        empresa = request.form['empresa']
        departamento = request.form['departamento']
        usuario = request.form['usuario']
        id = request.form['id']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        activo = usuarios.agregarActivo(empresa, departamento, usuario, id, nombre, descripcion)
        if activo is not None:
            print("Se ha agregado " + str(activo) + " con exito")
            return str(activo)
        else:
            return None

@app.route('/modificarActivo', methods=['POST'])
def modificarActivo():
    def modificarActivo():
        empresa = request.form['empresa']
        departamento = request.form['departamento']
        usuario = request.form['usuario']
        id = request.form['id']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        activo = usuarios.modificarActivo(empresa, departamento, usuario, id, nombre, descripcion)
        if activo is not None:
            print("Se ha agregado " + str(activo) + " con exito")
            return str(activo)
        else:
            return None

@app.route('/activosUsuario', methods=['POST'])
def verActivosUsuario():
    empresa = request.form['empresa']
    departamento = request.form['departamento']
    usuario = request.form['usuario']
    data = usuarios.activosUsuario(empresa, departamento, usuario)
    if data is not None:
        return data
    else:
        return None

@app.route('/eliminarActivo', methods=['POST'])
def eliminarActivo():
    empresa = request.form['empresa']
    departamento = request.form['departamento']
    usuario = request.form['usuario']
    id = request.form['id']
    eliminado = usuarios.borrarActivo(empresa, departamento, usuario, id)
    if eliminado is not None:
        return eliminado
    else:
        return None

if __name__ == "__main__":
    app.run(host='0.0.0.0')
