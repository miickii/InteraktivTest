import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("custom.db")
        self.cursor = self.conn.cursor()
    
    def get_user(self, name):
        self.cursor.execute("SELECT * FROM USER WHERE name='{}'".format(name))

        return self.cursor.fetchone()
    
    def add_user(self, name, password):
        query = 'INSERT INTO USER (name, password) VALUES (?, ?)'
        self.cursor.execute(query, (name, password))
        self.conn.commit()
    
    def get_all_tests(self):
        self.cursor.execute("SELECT * FROM TEST")

        return self.cursor.fetchall()
    
    def get_test(self, name):
        self.cursor.execute("SELECT * FROM TEST WHERE name='{}'".format(name))

        return self.cursor.fetchone()
    
    def get_test_data(self, id):
        self.cursor.execute("SELECT * FROM TEST WHERE id='{}'".format(id))
        test_name = self.cursor.fetchone()[1]

        self.cursor.execute("SELECT * FROM QUESTION WHERE test_id='{}'".format(id))
        questions = self.cursor.fetchall()

        choices = []
        for question in questions:
            self.cursor.execute("SELECT * FROM CHOICE WHERE question_id='{}'".format(question[0]))
            question_choices = self.cursor.fetchall()
            choices.append([(c[2], c[3]) for c in question_choices]) # Only add "name" and "correct" columns to choices array
        
        # change each question to only contain id and name
        questions = [(q[0], q[2]) for q in questions]

        return test_name, questions, choices
    
    def add_test(self, name):
        query = "INSERT INTO TEST (name) VALUES (?)"
        self.cursor.execute(query, (name,))
        self.conn.commit()
    
    def add_question(self, test_id, question, choices, correct_choices):
        query = "INSERT INTO QUESTION (test_id, name) VALUES (?, ?)"
        self.cursor.execute(query, (test_id, question))

        self.cursor.execute("SELECT * FROM QUESTION WHERE name='{}'".format(question))
        question_id = self.cursor.fetchone()[0]
        for i, choice in enumerate(choices):
            query = "INSERT INTO CHOICE (question_id, name, correct) VALUES (?, ?, ?)"
            self.cursor.execute(query, (question_id, choice, correct_choices[i]))

        self.conn.commit()
    
    def add_completed(self, test_name, result, date, time, user_id):
        query = "INSERT INTO COMPLETED (test_name, result, date, time, user_id) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (test_name, result, date, time, user_id))
        self.conn.commit()
    
    def get_completed(self, user_id):
        self.cursor.execute("SELECT * FROM COMPLETED WHERE user_id='{}'".format(user_id))
        completed = self.cursor.fetchall()
        print(len(completed))
        return completed
    
    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS USER (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        password TEXT
                    )""")

        # Create the test table with a unique id and name column
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TEST (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE
                        )''')

        # Create the question table with name and correct columns
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS QUESTION (
                        id INTEGER PRIMARY KEY,
                        test_id INTEGER,
                        name TEXT,
                        FOREIGN KEY(test_id) REFERENCES TEST(id)
                        )''')

        # Create the choice table with name column
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS CHOICE (
                        id INTEGER PRIMARY KEY,
                        question_id INTEGER,
                        name TEXT,
                        correct INTEGER,
                        FOREIGN KEY(question_id) REFERENCES QUESTION(id)
                        )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS COMPLETED (
                        id INTEGER PRIMARY KEY,
                        test_name TEXT,
                        result INTEGER,
                        date TEXT,
                        time TEXT,
                        user_id INTEGER,
                        FOREIGN KEY(user_id) REFERENCES USER(id)
                        )''')

        self.conn.commit()

# m = DBManager()
# m.create_db()