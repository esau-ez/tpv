use tpv;
CREATE TABLE IF NOT EXISTS Productos (
	ID_Producto INTEGER AUTO_INCREMENT NOT NULL,
	Código TEXT,
	Nombre TEXT,
	Precio float,
	Stock INTEGER,
    Oferta INTEGER,
    PRIMARY KEY(ID_Producto)
);
CREATE TABLE IF NOT EXISTS Ticket (
	ID_Ticket INTEGER AUTO_INCREMENT NOT NULL,
    Fecha date,
    Hora time,
    SUBTOTAL float,
    TOTAL float,
    PRIMARY KEY(ID_Ticket)
);
CREATE TABLE IF NOT EXISTS Venta(
	ID INTEGER AUTO_INCREMENT NOT NULL,
    Fecha date,
    NumeroVentas integer,
    Total float,
    PRIMARY KEY(ID)
);
CREATE TABLE IF NOT EXISTS users(
	ID INTEGER AUTO_INCREMENT NOT NULL,
    email TEXT,
    username TEXT,
    password TEXT,
    rol TEXT,
    PRIMARY KEY(ID)
);