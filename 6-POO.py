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

# class Colaborador(models.Models):
#     def __init__(self, dni, nombre, apellido, estado, fecha_reg, email, telefono, avatar, contrasenia): # __ se llama dunder
#         self.dni = dni
#         self.nombre = nombre
#         self.apellido = apellido
#         self.estado = estado
#         self.fecha_reg = fecha_reg
#         self.email = email
#         self.telefono = telefono
#         self.avatar = avatar
#         self.contrasenia = contrasenia
    
#     def get_dni(dni):
#         pass

#     def set_dni(dni_old, dni_new):
#         pass

#     def delete_row_dni(dni):
#         pass

#     def suma():
#         pass

# Clase Usuario
# -atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de 
# registro, avatar, estado, online
# -métodos: login(), registrar()

# Clase Publico(Usuario)
# -atributo: es_publico
# -métodos: registrar(), comentar()
#####################################################
#####################################################
#####################################################

class Usuario:
    def __init__(self, id=None, nombre=None, apellido=None, telefono=None, username=None, email=None, contrasenia=None, fecha_de_registro=None, avatar=None, estado=None, online=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasenia = contrasenia
        self.fecha_de_registro = fecha_de_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
    
    def login(self):
        if (input("Ingrese su username: ") == self.username and input("Ingrese su contraseña: ") == self.contrasenia):
            print("Bienvenido", self.username)
            self.estado = "logueado"
            self.online = True
        else:
            print("Usuario o contraseña invalido")
    
    def registrar(self):
        self.nombre = input(f'Ingrese su nombre: ')
        self.apellido = input(f'Ingrese su apellido: ')
        self.telefono = input(f'Ingrese su telefono: ')
        self.username = input(f'Ingrese su username: ')
        self.email = input(f'Ingrese su email: ')
        self.contrasenia = input(f'Ingrese su contrasenia: ')
    
    def get_username(self):
        return self.username
    
    def get_estado(self):
        return self.estado
    
    def get_online(self):
        return self.online

# persona = Usuario()
# persona.registrar()
# usr = persona.get_username()
# print('Usuario', usr)

# persona.login()
# estado_persona = persona.get_estado()
# online_persona = persona.get_online()
# print(f'Estado {estado_persona}, Online {online_persona}')

# clase Articulo
# id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id 
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen 
        self.estado = estado

# clase Comentario
# id, id_articulo, id_usuario, contenido, fecha_hora, estado  
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado

# clase Colaborador(Usuario)
# atributos: es_colaborador
# métodos: registrar(POR HERENCIA), comentar(), publicar()
class Colaborador(Usuario):
    es_colaborador = True

    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online)

    def comentar(self):
        return Comentario(
            id=input("Ingrese id: "), 
            id_articulo=input("Ingrese id_articulo: "), 
            id_usuario=self.id,
            contenido=input("Ingrese contenido: "), 
            fecha_hora=input("Ingrese fecha_hora: "), 
            estado=input("Ingrese estado: "))

    def publicar(self):
        return Articulo(
            id=input("Ingrese id: "),
            id_usuario=self.id,
            titulo=input("Ingrese titulo: "),
            resumen=input("Ingrese resumen: "),
            contenido=input("Ingrese contenido: "),
            fecha_publicacion=input("Ingrese fecha_publicacion: "),
            imagen=input("Ingrese imagen: "),
            estado=input("Ingrese estado: "))
    
###
class Publico(Usuario):
    es_publico = True

    def __init__(self, id=None, nombre=None, apellido=None, telefono=None, username=None, email=None, contrasenia=None, fecha_de_registro=None, avatar=None, estado=None, online=None):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online)
    
    def get_es_publico(self):
        return self.es_publico

# obj_publico = Publico()
# obj_publico.registrar()
# var_pub = obj_publico.get_es_publico()
# print(f'Mediante metodo: {var_pub}, mediante acceso al atrib {obj_publico.es_publico}')
# print(f'Obtener username {obj_publico.get_username()}')


