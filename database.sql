CREATE SCHEMA ;
'''Задания
Задача 1: Создание и заполнение таблиц
● Создайте таблицу authors с полями id, first_name и
last_name. Используйте PRIMARY KEY для поля id
● Создайте таблицу books с полями id, title, author_id и
publication_year. Используйте PRIMARY KEY для поля id и
FOREIGN KEY для поля author_id, ссылаясь на таблицу
authors
● Создайте таблицу sales с полями id, book_id и quantity.
Используйте PRIMARY KEY для поля id и FOREIGN KEY для
поля book_id, ссылаясь на таблицу books
● Добавьте несколько авторов в таблицу authors
● Добавьте несколько книг в таблицу books, указывая
авторов из таблицы authors
● Добавьте записи о продажах книг в таблицу sales
Задача 2: Использование JOIN
● Используйте INNER JOIN для получения списка всех книг и
их авторов.
● Используйте LEFT JOIN для получения списка всех авторов
и их книг (включая авторов, у которых нет книг).
● Используйте RIGHT JOIN для получения списка всех книг и
их авторов, включая книги, у которых автор не указан
Задача 3: Множественные JOIN
● Используйте INNER JOIN для связывания таблиц authors,
books и sales, чтобы получить список всех книг, их авторов
и продаж
● Используйте LEFT JOIN для связывания таблиц authors,
books и sales, чтобы получить список всех авторов, их книг
и продаж (включая авторов без книг и книги без продаж)'''


CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(200),
    last_name VARCHAR(200)
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    author_id INT REFERENCES authors(id),
    publication_year INT
);

CREATE TABLE sales(
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(id),
    quantity INT
);

INSERT INTO authors(first_name, last_name)
VALUES ('Брэм', 'Стокер'),
       ('Томас', 'Харрис'),
       ('Фрэнсис Скот', 'Фицджеральд'),
       ('Майкл', 'Коннели'),
       ('Деннис', 'Лихэйн');

INSERT INTO books(title, author_id, publication_year)
VALUES ('Остров проклятых', 5, 1998),
       ('Дракула', 1, 1956),
       ('Линкольн для адвоката', 4, 2001),
       ('Красный дракон', 2, 1975),
       ('Великий Гэтсби', 3, 1980);

INSERT INTO sales(book_id, quantity)
VALUES (1, 200),
       (2, 150),
       (3, 552),
       (4, 600),
       (5, 890);

SELECT books.title AS book_name,
    authors.first_name AS authors_name,
    authors.last_name AS authors_lastName
FROM books
INNER JOIN authors ON books.author_id = authors.id;

INSERT INTO authors (first_name, last_name)
VALUES ('Дейл', 'Карнеги')

SELECT books.title AS book_name,
    authors.first_name AS authors_name,
    authors.last_name AS authors_lastName
FROM books
LEFT JOIN authors ON books.author_id = authors.id;

SELECT books.title AS book_name,
    authors.first_name AS authors_name,
    authors.last_name AS authors_lastName
FROM books
RIGHT JOIN authors ON books.author_id = authors.id;


SELECT books.title AS book_name,
    authors.first_name AS authors_name,
    authors.last_name AS authors_lastName
FROM books
INNER JOIN authors ON books.author_id = authors.id
    INNER JOIN books ON sales.book_id = books.id;

SELECT books.title AS book_name,
    authors.first_name AS authors_name,
    authors.last_name AS authors_lastName
FROM books
LEFT JOIN authors ON books.author_id = authors.id
     LEFT JOIN books ON sales.book_id = books.id;