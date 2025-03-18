'''1. Представим, что у нас есть таблица "Employees" с
полями "Name", "Position", "Department", "Salary".
● Создайте таблицу "Employees" с указанными полями.
● Вставьте в таблицу несколько записей с информацией о
сотрудниках вашей компании.
● Измените данные в таблице для каких-то сотрудников.
Например, изменим должность одного из сотрудников на
более высокую.
● Добавьте новое поле "HireDate" (дата приема на работу) в
таблицу "Employees".
Продолжение ->
● Добавьте записи о дате приема на работу для всех
сотрудников.
● Найдите всех сотрудников, чья должность "Manager".
● Найдите всех сотрудников, у которых зарплата больше
5000 долларов.
● Найдите всех сотрудников, которые работают в отделе
"Sales".
● Найдите среднюю зарплату по всем сотрудникам.
● Удалите таблицу "Employees".'''

CREATE DATABASE my_database;
CREATE TABLE employees
(
    id INT PRIMARY KEY,
    name VARCHAR,
    departament VARCHAR,
    position VARCHAR,
    salary INT
);

INSERT INTO employees (id, name, departament, position, salary)
VALUES(1, 'Alex Pereira', 'закупки' , 'manager', 5000);

INSERT INTO employees (id, name, departament, position, salary)
VALUES(2, 'Logan Paul', 'продажи' , 'manager', 4000);

INSERT INTO employees (id, name, departament, position, salary)
VALUES(3, 'Brice Mitchel', 'продажи' , 'consultant', 3000);

INSERT INTO employees (id, name, departament, position, salary)
VALUES(4, 'Joe Cole', 'продажи' , 'director', 8000);

UPDATE employees
SET position = 'Assistant Director'
WHERE id = 1;

ALTER TABLE employees
ADD COLUMN HireDate FLOAT;

UPDATE employees
SET hiredate = 24.04
WHERE id = 1;

UPDATE employees
SET hiredate = 20.01
WHERE id = 2;

UPDATE employees
SET hiredate = 15.03
WHERE id = 3;

UPDATE employees
SET hiredate = 09.04
WHERE id = 4;

SELECT name
FROM employees
WHERE position = 'manager';

SELECT name
FROM employees
WHERE salary >= 5000;

SELECT name
FROM employees
WHERE departament = 'продажи';

SELECT AVG(salary) as AvgSalary
FROM employees;

DROP DATABASE my_database