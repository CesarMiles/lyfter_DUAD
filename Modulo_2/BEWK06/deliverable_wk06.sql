-- Table creation 

create table deliverable_wk06_transactions.customers (
        customer_id SERIAL PRIMARY KEY,
        full_name VARCHAR(50),
        email VARCHAR(50),
        account_status VARCHAR(20),
        last_purchase DATE);

create table deliverable_wk06_transactions.products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(50),
        product_price INT,
        stock INT);

CREATE TABLE deliverable_wk06_transactions.invoice (
    invoice_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES deliverable_wk06_transactions.customers(customer_id),
    create_date DATE NOT NULL DEFAULT CURRENT_DATE,
    total INT,
    status VARCHAR(20) NOT NULL
);

create table deliverable_wk06_transactions.invoice_details (
        item_id SERIAL PRIMARY KEY,
        invoice_id INT NOT NULL references deliverable_wk06_transactions.invoice(invoice_id),
        product_id INT NOT NULL references deliverable_wk06_transactions.products(product_id),
		quantity SMALLINT, 
        unit_price INT);

-- Insertar customers
INSERT INTO deliverable_wk06_transactions.customers 
(full_name, email, account_status, last_purchase) 
VALUES 
('María González', 'maria.gonzalez@email.com', 'active', '2024-11-15'),
('Carlos Rodríguez', 'carlos.rodriguez@email.com', 'active', '2024-11-10'),
('Ana Martínez', 'ana.martinez@email.com', 'inactive', '2024-10-28'),
('Javier López', 'javier.lopez@email.com', 'premium', '2024-11-20'),
('Laura Sánchez', 'laura.sanchez@email.com', 'active', '2024-11-18');

-- Insertar products  
INSERT INTO deliverable_wk06_transactions.products 
(product_name, product_price, stock) 
VALUES 
('Laptop Gaming', 1200, 15),
('Smartphone Pro', 800, 25),
('Auriculares Bluetooth', 150, 40),
('Tablet 10 pulgadas', 450, 12),
('Smartwatch Deportivo', 299, 30);

-- Transaction to execute a purchase
BEGIN TRANSACTION;

-- 1. Confirm product stock
DO $$
BEGIN
IF NOT EXISTS (
    SELECT 1 FROM deliverable_wk06_transactions.products
    WHERE product_id IN (1, 3, 5)
    AND stock > 0
    ) THEN 
    RAISE EXCEPTION 'There is no stock';
END IF;

-- 2. confirm that user making the purchase exists
IF NOT EXISTS (
    SELECT 1 
    FROM deliverable_wk06_transactions.customers
    WHERE customer_id = 4
    ) THEN 
    RAISE EXCEPTION 'Invalid user';
END IF;
END $$;

-- 3. Create the invoice with the user id associated
INSERT INTO deliverable_wk06_transactions.invoice (customer_id, total)
VALUES (4, 1649);

-- 3.1 Create invoice detail to information on each product purchased
INSERT INTO deliverable_wk06_transactions.invoice_details (invoice_id, product_id, quantity, unit_price)
VALUES
(1, 1, 1, 1200), 
(1, 3, 1, 150),
(1, 5, 1, 299);

-- Savepoint now that order has been created
SAVEPOINT order_created;

-- 4. Reducing stock available
UPDATE deliverable_wk06_transactions.products 
SET stock = stock - 1 
WHERE product_id IN (1, 3, 5);

UPDATE deliverable_wk06_transactions.customers 
SET last_purchase = CURRENT_DATE
WHERE customer_id = 4;

COMMIT;


-- Transaction to return a purchase
BEGIN TRANSACTION;

-- 1. Validate invoice id 
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM deliverable_wk06_transactions.invoice 
        WHERE invoice_id = 1
    ) THEN
        RAISE EXCEPTION 'Invalid invoice';
    END IF;
END $$;

-- 2. Increase the stock from the return 
UPDATE deliverable_wk06_transactions.products 
SET stock = stock + 1 
WHERE product_id IN (1, 3, 5);

-- 3. Update the status of the invoice 
UPDATE deliverable_wk06_transactions.invoice 
SET status = 'refunded' 
WHERE invoice_id = 1;

COMMIT;