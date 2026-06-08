class usuario:
    def __init__(self, id_usuario, nombre, emaill, carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.emaill = emaill
        self.carrera = carrera
        self.activo = True
        
    def activar (self):
        self.activo = True 
    def desactivar(self):
        self.activo = False

    def mostrar_info(self):
        return f"Usuario ID: {self.id_usuario}, Nombre: {self.nombre}, Emaill: {self.emaill}, Carrera: {self.carrera}"     