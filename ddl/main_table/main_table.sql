%sql
CREATE TABLE IF NOT EXISTS employee_main (
    id INT,
    name STRING,
    department STRING,
    salary INT,
    city STRING,
    joining_date DATE,
    email STRING,
    phone STRING,
    annual_salary INT,
    grade STRING,
    bonus DOUBLE
)
USING DELTA;