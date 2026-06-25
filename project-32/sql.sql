CREATE TABLE IF NOT EXISTS COMPANY (
    Employees_id TEXT,
    Employees_name TEXT,
    Employees_Age TEXT,
    Department TEXT,
    Employees_salary REAL
);

INSERT INTO COMPANY (Employees_id, Employees_name, Employees_Age, Department, Employees_salary)
VALUES
('1001', 'Ramesh', '34', 'Sales', 46000),
('1002', 'Raju', '23', 'HR', 38500),
('1003', 'John Mohan', '19', 'IT', 13000),
('1004', 'Sunder', '50', 'Sales', 29000),
('1005', 'Musk', '44', 'IT', 250000);


SELECT SUM(Employees_salary) AS Total_Salary 
FROM COMPANY;

SELECT AVG(Employees_salary) AS Average_Salary 
FROM COMPANY;


SELECT COUNT(Department) AS Department_Count 
FROM COMPANY;


SELECT MIN(Employees_salary) AS Minimum_Salary 
FROM COMPANY;


SELECT MAX(Employees_salary) AS Maximum_Salary 
FROM COMPANY;