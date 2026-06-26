-- ==========================================================
-- ASSIGNMENT 1: TARUN (CREATE TABLE & WHERE Clause)
-- ==========================================================
CREATE TABLE IF NOT EXISTS DXC_Employees (
    Emp_ID TEXT PRIMARY KEY,
    Name TEXT,
    Company TEXT,
    Fraud_Status TEXT
);

INSERT INTO DXC_Employees (Emp_ID, Name, Company, Fraud_Status) VALUES
('101', 'John Doe', 'DXC Company', 'No'),
('102', 'Jane Smith', 'DXC Company', 'Yes'),
('103', 'Mike Ross', 'DXC Company', 'No'),
('104', 'Rachel Zane', 'DXC Company', 'Yes');

SELECT * FROM DXC_Employees 
WHERE Fraud_Status = 'Yes';


-- ==========================================================
-- ASSIGNMENT 2: RAMESH (SQL Operators - OR / AND)
-- ==========================================================
CREATE TABLE IF NOT EXISTS Ramesh_Customers (
    Cust_ID TEXT PRIMARY KEY,
    Name TEXT,
    City TEXT,
    Grade INTEGER
);

INSERT INTO Ramesh_Customers (Cust_ID, Name, City, Grade) VALUES
('C1', 'Amit', 'New York', 150),
('C2', 'Rahul', 'London', 200),
('C3', 'Neha', 'New York', 50),
('C4', 'Pooja', 'Paris', 120);

-- Solution 1: New York OR Grade > 100
SELECT * FROM Ramesh_Customers 
WHERE City = 'New York' OR Grade > 100;

-- Solution 2: New York AND Grade > 100
SELECT * FROM Ramesh_Customers 
WHERE City = 'New York' AND Grade > 100;


-- ==========================================================
-- ASSIGNMENT 3: RITA (Aggregate Functions)
-- ==========================================================
CREATE TABLE IF NOT EXISTS COMPANY (
    Employees_id TEXT,
    Employees_name TEXT,
    Employees_Age TEXT,
    Department TEXT,
    Employees_salary REAL
);

INSERT INTO COMPANY (Employees_id, Employees_name, Employees_Age, Department, Employees_salary) VALUES
('1001', 'Ramesh', '34', 'Sales', 46000),
('1002', 'Raju', '23', 'HR', 38500),
('1003', 'John Mohan', '19', 'IT', 13000),
('1004', 'Sunder', '50', 'Sales', 29000),
('1005', 'Musk', '44', 'IT', 250000);

-- Solutions for Rita
SELECT SUM(Employees_salary) AS Total_Salary FROM COMPANY;
SELECT AVG(Employees_salary) AS Average_Salary FROM COMPANY;
SELECT COUNT(Department) AS Department_Count FROM COMPANY;
SELECT MIN(Employees_salary) AS Minimum_Salary FROM COMPANY;
SELECT MAX(Employees_salary) AS Maximum_Salary FROM COMPANY;


-- ==========================================================
-- ASSIGNMENT 4: HARSH (Capstone Project)
-- ==========================================================
CREATE TABLE IF NOT EXISTS Capstone_Employees (
    Emp_ID TEXT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Age INTEGER,
    Salary REAL
);

INSERT INTO Capstone_Employees (Emp_ID, Name, Department, Age, Salary) VALUES
('E01', 'Aarav', 'IT', 28, 65000),
('E02', 'Priya', 'HR', 34, 52000),
('E03', 'Rohan', 'Sales', 41, 78000),
('E04', 'Sneha', 'IT', 26, 62000),
('E05', 'Karan', 'Finance', 38, 71000);

-- Capstone Solutions (Filtering, Sorting, Manipulating)
SELECT * FROM Capstone_Employees 
WHERE Salary > 50000 
ORDER BY Salary DESC;

SELECT Emp_ID, Name, Salary 
FROM Capstone_Employees 
WHERE Department = 'IT';

SELECT Name, Department, Salary, (Salary * 0.10) AS "Holiday_Bonus" 
FROM Capstone_Employees 
ORDER BY Name ASC;