SHOW DATABASES; -- Mostrar las bases de datos

CREATE DATABASE mer_tablas; -- Crear una base de datos llamada mer_tablas

USE mer_tablas; -- Acceder a la base de datos mer_tablas

SHOW TABLES; -- Mostrar las tablas. TABLA=ENTIDAD

CREATE TABLE blog(
    nombre CHAR(20),
    url CHAR(255),
    PRIMARY KEY(nombre)
);

SELECT * -- * representa TODOS los atributos
FROM blog;

INSERT blog(nombre, url) VALUES("Django3", "https://capacitaciones.chaco.gob.ar/course/view.php?id=313");

CREATE TABLE articulo(
    id INT AUTO_INCREMENT,
    titulo CHAR(20),
    imagen CHAR(255),
    fecha_publicacion DATE,
    contenido TEXT,
    estado CHAR(20) CHECK (estado = 'activo' OR estado = 'inactivo'),
    resumen CHAR(250),
    nombre_blog CHAR(20),
    PRIMARY KEY(id),
    FOREIGN KEY(nombre_blog) REFERENCES blog(nombre)
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