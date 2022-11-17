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
INSERT INTO Publisher VALUES ("PubA", 0, "Vancouver");
INSERT INTO Book VALUES (0, "BookA", "Yellow", 10);
INSERT INTO School VALUES ("SchoolA", 0, "Toronto", "DirA");
INSERT INTO Distribute VALUES ("PubA", "SchoolA", 0, 10);
INSERT INTO Book VALUES (1, "BookB", "Yellow", 10);
INSERT INTO School VALUES ("SchoolB", 1, "Edmonton", "DirB");
INSERT INTO School VALUES ("SchoolC", 2, "Vancouver", "DirC");
INSERT INTO Distribute VALUES ("PubA", "SchoolA", 1, 10);
INSERT INTO Distribute VALUES ("PubA", "SchoolB", 1, 10);
INSERT INTO Book VALUES (2, "The Lost Tribe", "Red", 25);
INSERT INTO Publisher VALUES ("PubB", 1, "Montreal");
INSERT INTO Distribute VALUES ("PubB", "SchoolB", 2, 100);
INSERT INTO Book VALUES (3, "BookC", "Yellow", 50);
INSERT INTO Distribute VALUES ("PubA", "SchoolC", 3, 75);
INSERT INTO Book VALUES (4, "BookD", "Green", 35);
INSERT INTO Publisher VALUES ("PubC", 2, "Edmonton");
INSERT INTO Distribute VALUES ("PubC", "SchoolB", 4, 25);
INSERT INTO Publisher VALUES ("PubD", 3, "Calgary");
INSERT INTO Book VALUES (5, "BookE", "Red", 25);
INSERT INTO School VALUES ("SchoolD", 3, "Calgary", "DirD");
INSERT INTO School VALUES ("SchoolE", 4, "Calgary", "DirE");
INSERT INTO School VALUES ("SchoolF", 5, "Calgary", "DirF");
INSERT INTO Distribute VALUES ("PubD", "SchoolD", 5, 30);
INSERT INTO Distribute VALUES ("PubD", "SchoolE", 5, 40);
INSERT INTO Publisher VALUES ("PubE", 4, "Calgary");
INSERT INTO Book VALUES (6, "BookF", "Blue", 55);
INSERT INTO Distribute VALUES ("PubE", "SchoolD", 6, 30);
INSERT INTO Distribute VALUES ("PubE", "SchoolE", 6, 30);
INSERT INTO Distribute VALUES ("PubE", "SchoolF", 6, 30);
INSERT INTO Distribute VALUES ("PubE", "SchoolB", 6, 30);
INSERT INTO Publisher VALUES ("PubF", 5, "The Moon");
INSERT INTO Book VALUES (7, "BookG", "Pink", 1005);
INSERT INTO School VALUES ("SchoolG", 6, "Ottawa", "DirG");
INSERT INTO Distribute VALUES ("PubF", "SchoolG", 7, 105);
INSERT INTO Book VALUES (8, "BookH", "Teal", 5);
INSERT INTO School VALUES ("SchoolH", 7, "Windsor", "DirH");
INSERT INTO Distribute VALUES ("PubF", "SchoolG", 8, 1);
INSERT INTO Distribute VALUES ("PubF", "SchoolH", 8, 2);
INSERT INTO Publisher VALUES ("PubG", 6, "Edmonton");
INSERT INTO School VALUES ("SchoolI", 8, "Edmonton", "DirI");
INSERT INTO Distribute VALUES ("PubG", "SchoolI", 2, 100);
```

```
CREATE TABLE Country 
	(name VARCHAR(255), 
	area INT, 
	population INT, 
	PRIMARY KEY (name)); 
CREATE TABLE City 
	(cityName VARCHAR(255), 
	countryName VARCHAR(255), 
	area INT, 
	population INT, 
	PRIMARY KEY (cityName)); 
CREATE TABLE House 
	(hno INT, 
	rooms INT, 
	stno INT, 
	ownerName VARCHAR(255), 
	PRIMARY KEY (hno)); 
CREATE TABLE Border 
	(countryName1 VARCHAR(255), 
	countryName2 VARCHAR(255), 
	FOREIGN KEY (countryName1) REFERENCES Country(name) ON DELETE CASCADE ON UPDATE CASCADE, 
	FOREIGN KEY (countryName2) REFERENCES Country(name) ON DELETE CASCADE ON UPDATE CASCADE);
CREATE TABLE Street 
	(stno INT, 
	cityName VARCHAR(255), 
	length INT, 
	PRIMARY KEY (stno)); 
INSERT INTO Country VALUES ("North Pole", 3, 2);
INSERT INTO Country VALUES ("Canada", 5, 10);
INSERT INTO Country VALUES ("USA", 8, 25);
INSERT INTO Country VALUES ("Mexico", 4, 15);
INSERT INTO Border VALUES ("North Pole", "Canada");
INSERT INTO Border VALUES ("Canada", "USA");
INSERT INTO Border VALUES ("USA", "Mexico");
INSERT INTO City VALUES ("Polecity", "North Pole", 2, 4);
INSERT INTO City VALUES ("Calgary", "Canada", 5, 7);
INSERT INTO City VALUES ("Edmonton", "Canada", 6, 8);
INSERT INTO City VALUES ("Anaheim", "USA", 6, 12);
INSERT INTO City VALUES ("Chicago", "USA", 8, 15);
INSERT INTO City VALUES ("Boston", "USA", 7, 13);
INSERT INTO City VALUES ("Mexico City", "Mexico", 8, 15);
INSERT INTO Street VALUES (0, "Polecity", 5);
INSERT INTO Street VALUES (1, "Polecity", 1);
INSERT INTO Street VALUES (2, "Calgary", 6);
INSERT INTO Street VALUES (3, "Calgary", 4);
INSERT INTO Street VALUES (4, "Edmonton", 8);
INSERT INTO Street VALUES (5, "Edmonton", 3);
INSERT INTO Street VALUES (6, "Anaheim", 6);
INSERT INTO Street VALUES (7, "Anaheim", 3);
INSERT INTO Street VALUES (8, "Chicago", 4);
INSERT INTO Street VALUES (9, "Chicago", 8);
INSERT INTO Street VALUES (10, "Boston", 7);
INSERT INTO Street VALUES (11, "Mexico City", 3);
INSERT INTO House VALUES (0, 2, 1, "A");
INSERT INTO House VALUES (1, 3, 1, "B");
INSERT INTO House VALUES (2, 4, 7, "B");
INSERT INTO House VALUES (3, 2, 2, "C");
INSERT INTO House VALUES (4, 3, 10, "C");
INSERT INTO House VALUES (5, 2, 5, "D");
INSERT INTO House VALUES (6, 3, 11, "D");
INSERT INTO House VALUES (7, 4, 6, "E");
INSERT INTO House VALUES (8, 2, 10, "E");
INSERT INTO House VALUES (9, 3, 8, "F");
INSERT INTO House VALUES (10, 4, 7, "G");
INSERT INTO House VALUES (11, 2, 9, "G");
INSERT INTO House VALUES (12, 3, 5, "G");
INSERT INTO House VALUES (13, 1, 8, "H");
INSERT INTO House VALUES (14, 2, 9, "H");
INSERT INTO House VALUES (15, 3, 11, "H");
```