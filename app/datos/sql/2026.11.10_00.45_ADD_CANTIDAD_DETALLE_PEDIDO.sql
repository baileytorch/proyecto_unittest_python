USE db_test;

ALTER TABLE detalle_pedidos
    ADD cantidad INTEGER NOT NULL DEFAULT 1,
    ADD precio_unitario DECIMAL(10, 2) NULL;

UPDATE detalle_pedidos AS detalle
JOIN productos AS producto
    ON producto.id_producto = detalle.id_producto
SET detalle.precio_unitario = COALESCE(producto.precio_producto, 0.00);

ALTER TABLE detalle_pedidos
    MODIFY precio_unitario DECIMAL(10, 2) NOT NULL;
