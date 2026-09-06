# RootMates
A smart tool that recommends which vegetables to plant together based on root compatibility and natural synergy.

sql course: <br>
https://www.w3schools.com/sql/sql_intro.asp <br>
https://www.sqltutorial.org/

sqlite3 course: <br>
https://realpython.com/ref/stdlib/sqlite3/ <br>
https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-objects

### CREATE commands: <br>

1)  CREATE TABLE "partners" (
	"ID"	INTEGER,
	"ID_A"	INTEGER,
	"ID_B"	INTEGER,
	"NAME_B"	TEXT,
	"RELATION"	TEXT,
	"REASON"	TEXT
)

2) CREATE TABLE "plantanamo" (
    "ID"	INTEGER,
    "NAME"	TEXT
)