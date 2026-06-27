CREATE TABLE IF NOT EXISTS Customers (
    Customer_ID TEXT PRIMARY KEY,
    Customer_Name TEXT,
    Product_Name TEXT,
    Export_Country TEXT
);

INSERT INTO Customers (Customer_ID, Customer_Name, Product_Name, Export_Country) VALUES
('C01', 'Aaron', 'Laptops', 'USA'),
('C02', 'Morgan', 'Keyboards', 'Canada'),
('C03', 'Aurora', 'Monitors', 'UK'),
('C04', 'David', 'Laptops', 'USA'),
('C05', 'Amanda', 'Mice', 'Germany');

SELECT * FROM Customers
WHERE Customer_Name LIKE 'a%';

SELECT * FROM Customers
WHERE Customer_Name LIKE '%or%';

SELECT DISTINCT Export_Country 
FROM Customers;