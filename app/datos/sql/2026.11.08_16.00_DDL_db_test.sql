USE db_test;

CREATE TABLE clientes(
    id_cliente INTEGER AUTO_INCREMENT,
    rut_cliente VARCHAR(12) NOT NULL,
    nombre_cliente VARCHAR(25) NOT NULL,
    apellido_cliente VARCHAR(25) NOT NULL,
    correo_cliente VARCHAR(255) NOT NULL,
    fecha_nacimiento_cliente DATE NULL,
    fecha_incorporacion_cliente DATE NOT NULL,
    cliente_habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_clientes PRIMARY KEY (id_cliente)
) ENGINE = InnoDB COMMENT = 'Tabla de clientes de la empresa.';

CREATE TABLE productos(
    id_producto INTEGER AUTO_INCREMENT,
    sku_producto VARCHAR(50) NOT NULL,
    nombre_producto VARCHAR(255) NOT NULL,
    descripcion_producto TEXT NULL,
    precio_producto DECIMAL(10, 2) NULL DEFAULT 0.00,
    producto_habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_productos PRIMARY KEY (id_producto)
) ENGINE = InnoDB COMMENT = 'Tabla de productos comercializados por la empresa.';

CREATE TABLE pedidos(
    id_pedido INTEGER AUTO_INCREMENT,
    cliente_pedido INTEGER NOT NULL,
    fecha_pedido DATETIME NOT NULL,
    total_pedido DECIMAL(10, 2) NULL DEFAULT 0.00,
    estado_pedido ENUM('pendiente', 'procesando', 'enviado', 'entregado', 'cancelado') NOT NULL DEFAULT 'pendiente',
    pedido_habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_pedidos PRIMARY KEY (id_pedido),
    CONSTRAINT fk_pedidos_clientes FOREIGN KEY (cliente_pedido) REFERENCES clientes(id_cliente)
) ENGINE = InnoDB COMMENT = 'Tabla de pedidos realizados por clientes a la empresa.';

CREATE TABLE detalle_pedidos(
    id_detalle_pedido INTEGER AUTO_INCREMENT,
    id_pedido INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL DEFAULT 1,
    precio_unitario DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_detalle_pedidos PRIMARY KEY (id_detalle_pedido),
    CONSTRAINT fk_detalle_pedidos_pedidos FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    CONSTRAINT fk_detalle_pedidos_productos FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
) ENGINE = InnoDB COMMENT = 'Tabla auxiliar de detalle de pedidos, uniendo productos con pedidos.';