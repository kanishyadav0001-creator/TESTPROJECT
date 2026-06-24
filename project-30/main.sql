CREATE TABLE IF NOT EXISTS Employees (
    Emp_ID TEXT PRIMARY KEY,
    Name TEXT,
    Company TEXT,
    Fraud_Status TEXT
);


INSERT INTO Employees (Emp_ID, Name, Company, Fraud_Status) VALUES
('101', 'John ', 'DXC Company', 'No'),
('102', 'Jane ', 'DXC Company', 'Yes'),
('103', 'Mike Boss', 'DXC Company', 'No'),
('104', 'Anikan Zane', 'DXC Company', 'Yes'),
('105', 'Harvey ', 'DXC Company', 'No');


SELECT * FROM Employees 
WHERE Fraud_Status = 'Yes';