
CREATE TABLE users (
    user_id INT PRIMARY KEY, 
    username VARCHAR(100) NOT NULL 
);



CREATE TABLE product_orders (
    order_id INT PRIMARY KEY,
	user_id INT,
    customer_name VARCHAR(100),
    order_date DATE,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES product_orders(order_id)
);

ALTER TABLE items
ADD COLUMN quantity INT;

--Create a function that returns the total price for a given order of a given user.
CREATE OR REPLACE FUNCTION get_total_order_price(user_id INT, order_id INT)
RETURNS DECIMAL(10, 2) AS
$$
DECLARE
    total_price DECIMAL(10, 2);
BEGIN
    -- Суммируем стоимость всех товаров в заказе с правильным именем столбца
    SELECT SUM(items.item_quantity * items.price)
    INTO total_price
    FROM items 
    JOIN product_orders po ON items.order_id = po.order_id
    WHERE po.user_id = user_id AND po.order_id = order_id;
    
    -- Возвращаем общую стоимость
    RETURN total_price;
END;
$$ LANGUAGE plpgsql;




SELECT get_total_order_price(1, 101) AS total_price;
