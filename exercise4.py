import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="1017", port="5432"
)

cur = conn.cursor()


# Tables:
cur.execute(""" CREATE TABLE IF NOT EXISTS department (
    id SERIAL PRIMARY KEY,
    code TEXT NOT NULL,
    name TEXT NOT NULL
);

                CREATE TABLE IF NOT EXISTS student (
                    id SERIAL PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    department_id INT,
                    CONSTRAINT fk_majors_in FOREIGN KEY(department_id)
                    REFERENCES department(id)
                );

                CREATE TABLE IF NOT EXISTS professor (
                    id SERIAL PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    department_id INT NOT NULL,
                    CONSTRAINT fk_teaches_in FOREIGN KEY(department_id)
                    REFERENCES department(id)

                );
""")
            

# Inserting data into the tables
cur.execute(""" INSERT INTO department (code, name) VALUES
    ('EECS', 'Electrical Engineering & Computer Science'),
    ('MATH', 'Mathematics'),
    ('CHEM', 'Chemistry'),
    ('PHYS', 'Physics'),
    ('PHIL', 'Philosophy'),
    ('ECON', 'Economics');


                INSERT INTO student (first_name, last_name, department_id) VALUES
                ('Alice', 'Dobbins', 1),
                ('Bob', 'Smith', NULL ),
                ('Carol', 'Williams', 2),
                ('Dan', 'Smith', 1),
                ('Eve', 'Potter', 1),
                ('Grace', 'Goldman', 3),
                ('Faythe', 'Fisher', NULL ),
                ('Hannah', 'Hope', 4),
                ('Ian', 'Ingalls', 6),
                ('John', 'Johnson', NULL ),
                ('Kelly', 'Kenier', NULL);


                INSERT INTO professor (first_name, last_name, department_id) VALUES
                ('Adele', 'Goldberg', 1),
                ('Ada', 'Lovelace', 1),
                ('Claude', 'Shannon', 2),
                ('Katherine', 'Johnson', 2),
                ('Marie', 'Curie', 3),
                ('John', 'Dalton', 3),
                ('Ahmed', 'Zewail', 3),
                ('Albert', 'Einstein', 4),
                ('Isaac', 'Newton', 4),
                ('Immanuel', 'Kant', 5),
                ('Adam', 'Smith', 6);




""")

#conn.commit()

cur.close()
conn.close()