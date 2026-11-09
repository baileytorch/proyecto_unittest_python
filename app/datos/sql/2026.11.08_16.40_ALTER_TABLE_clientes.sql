USE db_test;

ALTER TABLE clientes ADD UNIQUE(rut_cliente);

ALTER TABLE clientes ADD UNIQUE(correo_cliente);