SHOW DATABASES; -- Mostrar las bases de datos

CREATE DATABASE mer_tablas; -- Crear una base de datos llamada mer_tablas

USE mer_tablas; -- Acceder a la base de datos mer_tablas

SHOW TABLES; -- Mostrar las tablas. TABLA=ENTIDAD

SELECT * -- * representa TODOS los atributos
FROM blog;

INSERT blog(nombre, url) VALUES("Django3", "https://capacitaciones.chaco.gob.ar/course/view.php?id=313");

CREATE TABLE colaborador(
    dni INT,
    nombre CHAR(20),
    apellido CHAR(20),
    estado CHAR(8) CHECK (estado = 'activo' OR estado = 'inactivo'),
    fecha_reg DATETIME DEFAULT CURRENT_TIMESTAMP,
    email CHAR(25) NOT NULL,
    telefono INT,
    avatar CHAR(255),
    contrasenia CHAR(30),
    PRIMARY KEY(dni)
);

INSERT INTO colaborador(
    dni,
    nombre,
    apellido,
    estado,
    email,
    telefono,
    avatar,
    contrasenia
) VALUES(
    45023203,
    "Yamil",
    "Nasir",
    "activo",
    "yamil.nasir@gmail.com",
    2353023,
    "link.avatar.com.ar",
    "as;kdjaks2"
);

CREATE TABLE categoria(
    nombre CHAR(20),
    estado CHAR(8) CHECK (estado = 'activo' OR estado = 'inactivo') DEFAULT 'activo',
    imagen CHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    jerarquia_nombre CHAR(20),
    PRIMARY KEY(nombre),
    FOREIGN KEY(jerarquia_nombre) REFERENCES categoria(nombre)
);

INSERT categoria(
    nombre,
    imagen,
    descripcion
) VALUES(
    "Ciencia",
    "URL",
    "Una descripcion"
);


CREATE TABLE sub_categoria(
    nombre CHAR(20),
    estado CHAR(8) CHECK (estado = 'activo' OR estado = 'inactivo') DEFAULT 'activo',
    imagen CHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    jerarquia_nombre CHAR(20),
    PRIMARY KEY(nombre),
    FOREIGN KEY(jerarquia_nombre) REFERENCES categoria(nombre)
);

CREATE TABLE usuario(
    email char(20),
    nombre char(20) NOT NULL,
    apellido char(20) NOT NULL,
    fecha_reg DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario char(20) NOT NULL UNIQUE,
    contrasenia char(30) NOT NULL,
    avatar char(255),
    estado CHAR(8) CHECK (estado = 'activo' OR estado = 'inactivo'),
    PRIMARY KEY(email)
);

CREATE TABLE blog(
    nombre CHAR(20),
    url CHAR(255),
    PRIMARY KEY(nombre)
);

CREATE TABLE articulo(
    id INT AUTO_INCREMENT,
    titulo CHAR(20),
    imagen CHAR(255),
    fecha_publicacion DATE,
    contenido TEXT,
    estado CHAR(20) CHECK (estado = 'activo' OR estado = 'inactivo'),
    resumen CHAR(250),
    nombre_blog CHAR(20) NOT NULL,
    nombre_categoria CHAR(20) NOT NULL,
    dni_escritor INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(nombre_blog) REFERENCES blog(nombre),
    FOREIGN KEY(nombre_categoria) REFERENCES categoria(nombre),
    FOREIGN KEY(dni_escritor) REFERENCES colaborador(dni)
);

INSERT articulo(
    titulo,
    imagen,
    fecha_publicacion,
    contenido,
    estado,
    resumen,
    nombre_blog
) VALUES(
    "Django",
    "ashdjklasjdjalksda",
    "2023-06-02",
    "aklhdsaklsjdklasjdklajskldj tex tex texto",
    "activo",
    "El resumen",
    "Django"
);

CREATE TABLE comentario(
    id INT AUTO_INCREMENT,
    texto TEXT,
    email_usuario char(20) NOT NULL,
    id_articulo INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(email_usuario) REFERENCES usuario(email),
    FOREIGN KEY(id_articulo) REFERENCES articulo(id)
);

CREATE TABLE articulo_leido(
    email_usuario char(20),
    id_articulo INT,
    PRIMARY KEY(email_usuario, id_articulo),
    FOREIGN KEY(email_usuario) REFERENCES usuario(email),
    FOREIGN KEY(id_articulo) REFERENCES articulo(id)
);
