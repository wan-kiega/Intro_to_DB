-- task_6.sql: Insert multiple rows into the customers table

-- Use the database passed as argument
USE alx_book_store;

-- Insert multiple customer records
INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, ADDRESS)
VALUES 
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness  Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness  Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness  Ave.');