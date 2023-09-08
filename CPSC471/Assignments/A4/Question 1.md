### CREATE TABLES
```
CREATE TABLE Publisher
	(name VARCHAR(255), 
	phone INT, 
	city VARCHAR(255), 
	PRIMARY KEY (name));

CREATE TABLE School
	(name VARCHAR(255),
	phone INT,
	city VARCHAR(255),
	director VARCHAR(255),
	PRIMARY KEY (name));

CREATE TABLE Book
	(ISBN INT,
	title VARCHAR(255),
	color VARCHAR(255),
	pages INT,
	PRIMARY KEY (ISBN));

CREATE TABLE Distribute
	(pname VARCHAR(255),
	sname VARCHAR(255),
	ISBN INT,
	quantity INT,
	FOREIGN KEY (pname) REFERENCES Publisher(name) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (sname) REFERENCES School(name) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (ISBN) REFERENCES Book(ISBN) ON DELETE CASCADE ON UPDATE CASCADE);
```

### Test Data
```
Yellow book published in Vancouver, distributed to Toronto
INSERT INTO Publisher VALUES ("PubA", 0, "Vancouver");
INSERT INTO Book VALUES (0, "BookA", "Yellow", 10);
INSERT INTO School VALUES ("SchoolA", 0, "Toronto", "DirA");
INSERT INTO Distribute VALUES ("PubA", "SchoolA", 0, 10);

Yellow book published in Vancouver, distributed to Toronto, Edmonton, Vancouver
INSERT INTO Book VALUES (1, "BookB", "Yellow", 10);
INSERT INTO School VALUES ("SchoolB", 1, "Edmonton", "DirB");
INSERT INTO School VALUES ("SchoolC", 2, "Vancouver", "DirC");
INSERT INTO Distribute VALUES ("PubA", "SchoolA", 1, 10);
INSERT INTO Distribute VALUES ("PubA", "SchoolB", 1, 10);

"The Lost Tribe" published in Montreal and distributed to Edmonton
INSERT INTO Book VALUES (2, "The Lost Tribe", "Red", 25);
INSERT INTO Publisher VALUES ("PubB", 1, "Montreal");
INSERT INTO Distribute VALUES ("PubB", "SchoolB", 2, 100);

"The Lost Tribe" published in Edmonton and distributed to Edmonton
INSERT INTO Publisher VALUES ("PubG", 6, "Edmonton");
INSERT INTO School VALUES ("SchoolI", 8, "Edmonton", "DirI");
INSERT INTO Distribute VALUES ("PubG", "SchoolI", 2, 100);

Yellow book published in Vancouver, distributed to Vancouver
INSERT INTO Book VALUES (3, "BookC", "Yellow", 50);
INSERT INTO Distribute VALUES ("PubA", "SchoolC", 3, 75);

Book published in Edmonton, distributed to Edmonton
INSERT INTO Book VALUES (4, "BookD", "Green", 35);
INSERT INTO Publisher VALUES ("PubC", 2, "Edmonton");
INSERT INTO Distribute VALUES ("PubC", "SchoolB", 4, 25);

Publisher that only distributes to Calgary
INSERT INTO Publisher VALUES ("PubD", 3, "Calgary");
INSERT INTO Book VALUES (5, "BookE", "Red", 25);
INSERT INTO School VALUES ("SchoolD", 3, "Calgary", "DirD");
INSERT INTO School VALUES ("SchoolE", 4, "Calgary", "DirE");
INSERT INTO School VALUES ("SchoolF", 5, "Calgary", "DirF");
INSERT INTO Distribute VALUES ("PubD", "SchoolD", 5, 30);
INSERT INTO Distribute VALUES ("PubD", "SchoolE", 5, 40);

Publisher that distributes to every school in Calgary
INSERT INTO Publisher VALUES ("PubE", 4, "Calgary");
INSERT INTO Book VALUES (6, "BookF", "Blue", 55);
INSERT INTO Distribute VALUES ("PubE", "SchoolD", 6, 30);
INSERT INTO Distribute VALUES ("PubE", "SchoolE", 6, 30);
INSERT INTO Distribute VALUES ("PubE", "SchoolF", 6, 30);
INSERT INTO Distribute VALUES ("PubE", "SchoolB", 6, 30);

Publisher that distributes only to every school in calgary
INSERT INTO Publisher VALUES ("PubH", 4, "Calgary");
INSERT INTO Book VALUES (9, "BookI", "Yellow", 5);
INSERT INTO Distribute VALUES ("PubH", "SchoolD", 9, 30);
INSERT INTO Distribute VALUES ("PubH", "SchoolE", 9, 30);
INSERT INTO Distribute VALUES ("PubH", "SchoolF", 9, 30);

Books distributed only to Ottawa
INSERT INTO Publisher VALUES ("PubF", 5, "The Moon");
INSERT INTO Book VALUES (7, "BookG", "Pink", 1005);
INSERT INTO School VALUES ("SchoolG", 6, "Ottawa", "DirG");
INSERT INTO Distribute VALUES ("PubF", "SchoolG", 7, 105);

Books distributed to Ottawa and Windsor
INSERT INTO Book VALUES (8, "BookH", "Teal", 5);
INSERT INTO School VALUES ("SchoolH", 7, "Windsor", "DirH");
INSERT INTO Distribute VALUES ("PubF", "SchoolG", 8, 1);
INSERT INTO Distribute VALUES ("PubF", "SchoolH", 8, 2);
```

**Find the ISBN, title and total quantity of yellow books that are published by publishers located in Vancouver and distributed only to schools located in Toronto.**
```
SELECT Book.ISBN, Book.title, Distribute.quantity 
FROM Book, Distribute 
WHERE color="Yellow" 
AND Distribute.ISBN=Book.ISBN 
AND Distribute.pname IN 
	(SELECT name FROM Publisher 
	WHERE city="Vancouver") 
AND Book.ISBN NOT IN 
	(SELECT ISBN FROM Distribute, School 
	WHERE sname=name 
	AND city!="Toronto");
```

**Find the names and directors of schools located in Edmonton and receive books titled 'The Lost Tribe' from publishers located in Montreal.**
```
SELECT name, director 
FROM School 
WHERE city="Edmonton" 
AND name IN 
	(SELECT sname FROM Distribute JOIN Publisher 
	WHERE pname=Publisher.name 
	AND sname=School.name 
	AND city="Montreal");
```

**Find the title and total quantity of each book distributed to all schools located in the same city as the publisher.**
```
SELECT title, SUM(quantity) 
FROM Book AS B, Distribute AS D, Publisher AS P, School AS S 
WHERE B.ISBN = D.ISBN 
AND D.pname = P.name 
AND D.sname = S.name 
AND P.city = S.city 
GROUP BY B.ISBN;
```

**Find the names and cities of the publishers who distribute books only to schools located in Calgary and distribute books to every school in Calgary.**
```
SELECT name, city 
FROM Publisher AS P 
WHERE NOT EXISTS (
	SELECT * FROM Distribute AS D, School AS S 
	WHERE D.pname = P.name 
	AND D.sname = S.name 
	AND S.city != "Calgary"
)

INTERSECT

SELECT name, city 
FROM Publisher AS P 
WHERE NOT EXISTS (
	SELECT * FROM School AS S 
	WHERE S.city = "Calgary" 
	AND NOT EXISTS (
		SELECT * FROM Distribute AS D 
		WHERE D.sname = S.name 
		AND D.pname = P.name 
	)
);
```

**Find the ISBN and title of books distributed to schools located in Ottawa and never distributed to schools located in Windsor.**
```
SELECT ISBN, title 
FROM Book 
WHERE ISBN IN 
	(SELECT ISBN 
	FROM Distribute JOIN School 
	WHERE sname=name 
	AND city="Ottawa") 
AND ISBN NOT IN 
	(SELECT ISBN 
	FROM Distribute JOIN School 
	WHERE sname=name 
	AND city="Windsor");
```