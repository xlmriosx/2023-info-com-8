# CREATE TABLE colaborador(
#     dni INT,
#     nombre CHAR(20),
#     apellido CHAR(20),
#     estado CHAR(8) CHECK (estado = 'activo' OR estado = 'inactivo'),
#     fecha_reg DATETIME DEFAULT CURRENT_TIMESTAMP,
#     email CHAR(25) NOT NULL,
#     telefono INT,
#     avatar CHAR(255),
#     contrasenia CHAR(30),
#     PRIMARY KEY(dni)
# );

class Colaborador(models.Models):
    def __init__(self, dni, nombre, apellido, estado, fecha_reg, email, telefono, avatar, contrasenia): # __ se llama dunder
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.estado = estado
        self.fecha_reg = fecha_reg
        self.email = email
        self.telefono = telefono
        self.avatar = avatar
        self.contrasenia = contrasenia
    
    def get_dni(dni):
        pass

    def set_dni(dni_old, dni_new):
        pass

    def delete_row_dni(dni):
        pass

    def suma():
        pass