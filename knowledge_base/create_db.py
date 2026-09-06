import sqlite3

conn = sqlite3.connect("employees.db")

conn.executescript("""
CREATE TABLE IF NOT EXISTS employees (
    id          INTEGER PRIMARY KEY,
    first_name  TEXT    NOT NULL,
    last_name   TEXT    NOT NULL,
    department  TEXT    NOT NULL,
    job_title   TEXT    NOT NULL,
    salary      INTEGER NOT NULL,
    hire_date   TEXT    NOT NULL,
    city        TEXT    NOT NULL,
    age         INTEGER NOT NULL,
    is_active   INTEGER NOT NULL DEFAULT 1
);

INSERT INTO employees (first_name, last_name, department, job_title, salary, hire_date, city, age, is_active) VALUES
    ('Alice',    'Novak',      'Engineering', 'Senior Developer',  95000, '2019-03-15', 'Prague',   34, 1),
    ('Martin',   'Horak',      'Engineering', 'Junior Developer',  52000, '2022-07-01', 'Brno',     26, 1),
    ('Jana',     'Krejci',     'Engineering', 'DevOps Engineer',   78000, '2020-11-20', 'Prague',   31, 1),
    ('Tomas',    'Blazek',     'Engineering', 'Senior Developer',  98000, '2018-01-10', 'Ostrava',  38, 1),
    ('Lucie',    'Dvorak',     'Marketing',   'Marketing Manager', 72000, '2017-05-22', 'Prague',   41, 1),
    ('Pavel',    'Cerny',      'Marketing',   'Content Specialist',45000, '2023-02-14', 'Brno',     28, 1),
    ('Eva',      'Mala',       'Marketing',   'SEO Analyst',       48000, '2021-09-30', 'Prague',   30, 0),
    ('Ondrej',   'Prochazka',  'HR',          'HR Manager',        68000, '2016-08-05', 'Prague',   45, 1),
    ('Katerina', 'Vesela',     'HR',          'HR Specialist',     51000, '2022-03-18', 'Olomouc',  29, 1),
    ('Jakub',    'Kolar',      'Finance',     'Financial Analyst', 63000, '2020-06-11', 'Prague',   33, 1),
    ('Petra',    'Ruzicka',    'Finance',     'Accountant',        57000, '2019-10-07', 'Brno',     36, 1),
    ('Radek',    'Novotny',    'Finance',     'CFO',              130000, '2015-04-01', 'Prague',   52, 1),
    ('Simona',   'Cerna',      'Sales',       'Sales Manager',     82000, '2018-12-03', 'Prague',   39, 1),
    ('Michal',   'Pokorny',    'Sales',       'Account Executive', 61000, '2021-01-25', 'Plzen',    27, 1),
    ('Veronika', 'Klimova',    'Sales',       'Account Executive', 59000, '2021-04-19', 'Prague',   31, 0),
    ('Jiri',     'Nemec',      'Engineering', 'QA Engineer',       60000, '2020-08-14', 'Brno',     35, 1),
    ('Marketa',  'Svoboda',    'Engineering', 'Tech Lead',        110000, '2016-02-28', 'Prague',   43, 1),
    ('David',    'Kratky',     'Marketing',   'Brand Manager',     67000, '2019-07-09', 'Ostrava',  37, 1),
    ('Lenka',    'Hajek',      'HR',          'Recruiter',         46000, '2023-05-02', 'Prague',   25, 1),
    ('Zdenek',   'Bartos',     'Sales',       'Sales Director',   115000, '2014-09-16', 'Prague',   50, 1);
""")

conn.commit()
conn.close()
print("employees.db created.")
