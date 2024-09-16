CREATE DATABASE gymbro;
USE gymbro;

create table usuarios(
	id_usuario bigint unsigned auto_increment primary key,
	correo varchar(50) not null,
    contrasenia varchar(50) not null,
	nombre varchar(20),
    apellido varchar(20),
	telefono varchar(15),
    rango bool
);
CREATE TABLE clase (
	id_clase INT AUTO_INCREMENT PRIMARY KEY,
    nombre_clase VARCHAR(20) NOT NULL,
    dia_clase date,
    cupo int,
    descripcion TEXT,
	INDEX (nombre_clase)
);
CREATE TABLE usuario_clase (
    id_usuario BIGINT UNSIGNED,
    id_clase INT,
    PRIMARY KEY (id_usuario, id_clase),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_clase) REFERENCES clase(id_clase) ON DELETE CASCADE
);

INSERT INTO usuarios (correo, contrasenia, nombre, apellido, telefono, rango) VALUES
('emanuelbotto13@gmail.com', '42204994', 'emanuel', 'botto', '3496413383', 1),
('juanperez01@gmail.com', '12345678', 'Juan', 'Pérez', '3512345678', 0),
('maria.garcia22@gmail.com', 'abcd1234', 'María', 'García', '3518765432', 1),
('luis.martinez33@gmail.com', 'password1', 'Luis', 'Martínez', '3498765432', 0),
('laura.fernandez44@gmail.com', 'mypassword', 'Laura', 'Fernández', '3476543210', 1),
('pablo.rodriguez55@gmail.com', '1234abcd', 'Pablo', 'Rodríguez', '3497654321', 0),
('sofia.lopez66@gmail.com', 'password12', 'Sofía', 'López', '3487654321', 1),
('carlos.morales77@gmail.com', 'mypassword1', 'Carlos', 'Morales', '3471234567', 0),
('valeria.santos88@gmail.com', 'securepass', 'Valeria', 'Santos', '3512340987', 1),
('jorge.mendez99@gmail.com', 'qwerty123', 'Jorge', 'Méndez', '3498760987', 0),
('andrea.rivera00@gmail.com', 'letmein123', 'Andrea', 'Rivera', '3482340987', 1);

INSERT INTO clase (nombre_clase, dia_clase, cupo) VALUES

('Funcional', '2024-09-10', 30),
('Funcional', '2024-09-11', 25),
('Funcional', '2024-09-12', 20),
('Funcional', '2024-09-13', 15),
('Funcional', '2024-09-14', 20),
('Funcional', '2024-09-15', 25),
('Funcional', '2024-09-16', 30),
('Funcional', '2024-09-17', 20),
('Funcional', '2024-09-18', 10),
('Funcional', '2024-09-19', 30);
INSERT INTO usuario_clase (id_usuario, id_clase) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6), 
(7, 7), 
(8, 8), 
(9, 9),  
(10, 10), 
(11, 1),
(1, 2), 
(2, 3);  

