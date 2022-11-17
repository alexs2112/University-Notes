### CREATE TABLES
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
```

### Test Data
```
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

Person owns exactly one house in neighbour to Canada
INSERT INTO House VALUES (0, 2, 1, "A");

Person owns two houses in two neighbours to Canada
INSERT INTO House VALUES (1, 3, 1, "B");
INSERT INTO House VALUES (2, 4, 7, "B");

Person owns one house in Canada, one house in neighbour to Canada
INSERT INTO House VALUES (3, 2, 2, "C");
INSERT INTO House VALUES (4, 3, 10, "C");

Person owns one house in Canada, one house not neighbouring Canada
INSERT INTO House VALUES (5, 2, 5, "D");
INSERT INTO House VALUES (6, 3, 11, "D");

Person who owns 2 houses in USA but none in Canada
INSERT INTO House VALUES (7, 4, 6, "E");
INSERT INTO House VALUES (8, 2, 10, "E");

Person who owns 1 house in USA
INSERT INTO House VALUES (9, 3, 8, "F");

Person who owns 2 houses in USA, 1 house in Canada
INSERT INTO House VALUES (10, 4, 7, "G");
INSERT INTO House VALUES (11, 2, 9, "G");
INSERT INTO House VALUES (12, 3, 5, "G");

Person who owns 2 houses in USA, 1 house in Mexico
INSERT INTO House VALUES (13, 1, 8, "H");
INSERT INTO House VALUES (14, 2, 9, "H");
INSERT INTO House VALUES (15, 3, 11, "H");

Streets with no houses: 0, 3, 4
```

### Questions
**Find the names of persons who own at least one house in at least one city of at least one country that has a border with Canada.**
```
SELECT DISTINCT ownerName 
FROM HOUSE 
WHERE stno IN 
	(SELECT stno 
	FROM Street 
	WHERE cityName IN 
		(SELECT cityName 
		FROM City 
		WHERE countryName!="Canada" 
		AND countryName IN 
			(SELECT countryName1 
			FROM Border 
			WHERE countryName2 = "Canada") 
		OR countryName IN 
			(SELECT countryName2 
			FROM Border 
			WHERE countryName1 = "Canada") 
		)
	);
```

**Find street number and city name of the shortest street in each city in every country that has border with Canada.**
```
SELECT stno, cityName 
FROM Street AS S 
WHERE cityName IN 
	(SELECT cityName 
	FROM City 
	WHERE countryName != "Canada" 
	AND countryName IN 
		(SELECT countryName1 
		FROM Border 
		WHERE countryName2 = "Canada") 
	OR countryName IN 
		(SELECT countryName2 
		FROM Border 
		WHERE countryName1 = "Canada") 
	)
AND NOT EXISTS (
	SELECT * 
	FROM Street AS T 
	WHERE T.length < S.length 
	AND T.cityName = S.cityName 
);
```

**Find the names and population sizes of all countries that have a border with the USA.**
```
SELECT name, population 
FROM Country 
WHERE name != "USA" 
AND name IN 
	(SELECT countryName1 
	FROM Border 
	WHERE countryName2 = "USA") 
OR name IN 
	(SELECT countryName2 
	FROM Border 
	WHERE countryName1 = "USA");
```

**Find the names of persons who do not own any houses in Canada but own more than one house in the USA.**
```
SELECT DISTINCT H.ownerName 
FROM House AS H 
WHERE H.stno IN 
	(SELECT stno 
	FROM Street 
	WHERE cityName IN 
		(SELECT cityName 
		FROM City 
		WHERE countryName="USA")
	) 
AND EXISTS (
	SELECT * FROM House AS H2 
	WHERE H2.ownerName = H.ownerName 
	AND H2.stno IN 
		(SELECT stno 
		FROM Street 
		WHERE cityName IN 
			(SELECT cityName 
			FROM City 
			WHERE countryName="USA")
		) 
	AND H.hno != H2.hno
) 

EXCEPT 

(SELECT ownerName 
FROM House 
WHERE stno IN 
	(SELECT stno 
	FROM Street 
	WHERE cityName IN 
		(SELECT cityName 
		FROM City 
		WHERE countryName="Canada")
	)
);
```
 - Might be able to use `AND H.ownerName NOT IN`  instead of `EXCEPT`, MySQL does not support EXCEPT

**Find the names and areas of cities with at least one street where no house is located.**
```
SELECT cityName, area 
FROM City 
WHERE cityName IN 
	(SELECT cityName 
	FROM Street AS S 
	WHERE NOT EXISTS (
		SELECT * 
		FROM House AS H 
		WHERE H.stno = S.stno)
	);
```