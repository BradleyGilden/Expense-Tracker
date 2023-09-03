#!/usr/bin/python3
"""
This module contains the main interface of the Expense-Tracker
Author: Bradley Gilden
"""
import mysql.connector
import getpass
BaseCmd = __import__("base-cmd").BaseCmd


class Console(BaseCmd):
    """Simple cmd interface to manage the expenses Database
    """

    def __init__(self):
        """Constructor for the console class"""
        super().__init__()
        excpt = False
        login_details = Console.generate_login()
        try:
            self.db = mysql.connector.connect(
                host=login_details[0],
                user=login_details[1],
                passwd=login_details[2]
            )
        except (Exception, mysql.connector.Error) as e:
            err = f"""\033[41m Database Connection Failed:\033[47m\033[30m{e} \
\033[0m\n\033[31mPlease check password, hostname, username and most
imporatantly if mysql service is running e.g sudo service mysql status"""
            print(err)
            self.default("connect fail")
            excpt = True
            exit()
        if excpt is False:
            self.default("connect success")
            self.cursor = self.db.cursor()
        Console.setup(self)

    def do_db(self, line):
        """directly manipulate database
        """
        try:
            self.cursor.execute(line)
            output = self.cursor.fetchall()
            for row in output:
                print(row[0])
        except mysql.connector.errors.Error as e:
            print(f"\033[31m{e}\033[0m")

    @staticmethod
    def generate_login() -> list:
        """accepts user login details for mysql database
        """
        login = []

        print("\n\033[42m************* Mysql Login **************\033[0m\n")
        login.append(input("\033[32mEnter hostname: "))
        login.append(input("\033[32mEnter user: "))
        # Nanospartan@117
        login.append(getpass.getpass("\033[32mEnter password: "))
        return login

    def setup(self):
        """creates necessary table and database
        """
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS expenses")
        self.cursor.execute("USE expenses")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    vault DECIMAL(9, 2) DEFAULT 0.00
);""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(
    id INT PRIMARY KEY AUTO_INCREMENT,
    store VARCHAR(25) DEFAULT 'General Store',
    item VARCHAR(25) NOT NULL,
    price DECIMAL(6, 2) DEFAULT 0.00,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);""")

    @staticmethod
    def store_init():
        """initializes stores and store items
        """

    def do_reset(self, line):
        """deletes all table entries in a database
        """
        self.cursor.execute("DROP TABLE transactions;")
        self.cursor.execute("DROP TABLE customers;")
        self.db.commit()
        Console.setup(self)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        self.cursor.close()
        self.db.close()
        return True


if __name__ == '__main__':
    Console().cmdloop()
