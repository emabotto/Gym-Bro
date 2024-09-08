create table usuarios(
	id bigint unsigned auto_increment primary key,
	correo varchar(50),
    contrasenia varchar(50),
	nombre varchar(20),
    apellido varchar(20),
	telefono int,
    rango bool
);
