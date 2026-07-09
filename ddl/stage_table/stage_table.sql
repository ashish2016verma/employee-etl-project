%sql
CREATE TABLE IF NOT EXISTS employee_stage (
    id INT,
    name STRING,
    department STRING,
    salary INT,
    city STRING,
    joining_date DATE,
    email STRING,
    phone STRING
)
USING DELTA;