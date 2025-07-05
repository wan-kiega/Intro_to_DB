-- task_5.sql: Insert a single row into the customers table

-- Use the current database passed as argument
USE alx_book_store;

-- Insert one customer record
INSERT INTO CUSTOMERS (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');