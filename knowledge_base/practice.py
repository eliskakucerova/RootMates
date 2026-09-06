import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

salary_plus = "salary*1.01"
cursor.execute("SELECT first_name, last_name, salary, salary*1.01 AS new_salary FROM employees ORDER BY new_salary DESC LIMIT 5 OFFSET 3")
command = cursor.fetchall()

for row in command:
    print(row)

conn.close()
