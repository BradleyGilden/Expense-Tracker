#!/usr/bin/python3
"""
This module contains the setup of the file and mysql database that interacts
with the Expense-Tracker
Author: Bradley Gilden
"""
import mysql.connector
import getpass
from re import search, findall

BaseCmd = __import__("base-cmd").BaseCmd


class DBSetup(BaseCmd):
    """Simple cmd interface to manage the expenses Database"""

    store_dict = {}

    def __init__(self):
        """Constructor for the DBSetup class"""
        super().__init__()
        excpt = False
        login_details = DBSetup.generate_login()
        try:
            self.db = mysql.connector.connect(
                host=login_details[0],
                user=login_details[1],
                passwd=login_details[2],
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
        DBSetup.setup(self)
        DBSetup.store_init()

    def do_db(self, line):
        """directly manipulate database
        Usage: db <query>
        """
        try:
            self.cursor.execute(line)
            output = self.cursor.fetchall()
            if output:
                for row in output:
                    print(row)
            self.db.commit()
        except mysql.connector.errors.Error as e:
            print(f"\033[31m{e}\033[0m")

    @staticmethod
    def generate_login() -> list:
        """accepts user login details for mysql database"""
        login = []

        try:
            print(
                """\n\033[1m\033[42m\033[30m************* Mysql Login \
**************\033[0m\n"""
            )
            login.append(input("\033[32mEnter hostname: "))
            login.append(input("\033[32mEnter user: "))
            login.append(getpass.getpass("\033[32mEnter password: "))
        except KeyboardInterrupt:
            print()
            exit()
        return login

    def setup(self):
        """creates necessary table and database"""
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS expenses")
        self.cursor.execute("USE expenses")
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS customers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    card CHAR(16) NOT NULL,
    vault DECIMAL(9, 2) DEFAULT 0.00
) ENGINE=InnoDB;"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS transactions(
    id INT PRIMARY KEY AUTO_INCREMENT,
    store VARCHAR(25) NOT NULL,
    item VARCHAR(25) NOT NULL,
    price DECIMAL(6, 2) DEFAULT 0.00,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;"""
        )

    @classmethod
    def store_init(cls):
        """initializes store values in the store file"""
        store_dict = {}
        line = ""
        try:
            with open("store.txt", "r") as file:
                for line in file:
                    line = search(r'"[^"]+"', line)
                    if line is not None:
                        line = eval(line.group())
                        store_dict[line] = {}

            with open("store.txt", "r") as file:
                for line in file:
                    line = findall(r'"[^"]+"', line)
                    store_dict[eval(line[0])][eval(line[1])] = eval(line[2])
            cls.store_dict = store_dict
        except FileNotFoundError:
            print("\033[31mWarning: Store file not found\033[0m")
            exit()

    def do_list(self, line):
        """lists available stores and available items in specific stores"""
        args = line.split()
        arglen = len(args)
        select = "SELECT name FROM customers;"
        message = """\033[31mUsage: list users | list stores | list store \
<name>\033[0m"""
        if arglen > 2:
            args[1] = " ".join(args[1:])

        DBSetup.store_init()
        if arglen == 1 and args[0] == "stores":
            for keys in DBSetup.store_dict.keys():
                print(keys)
        elif arglen == 1 and args[0] == "users":
            self.cursor.execute(select)
            output = self.cursor.fetchall()
            for row in output:
                print(row[0])
        elif arglen >= 2 and args[0] == "store":
            if args[1] not in DBSetup.store_dict.keys():
                print(f"\033[31mInvalid store name: {args[1]}\033[0m")
                self.default("fail 0")
            else:
                itm = "ITEMS:"
                maxw = max(len(i) for i in DBSetup.store_dict[args[1]].keys())
                print(f"{itm:<{maxw}}  PRICE($):")
                print("-" * (maxw + 11))
                for key, value in DBSetup.store_dict[args[1]].items():
                    print(f"{key:<{maxw}}  ${value}")
        else:
            print(message)
            self.default("fail 0")

    def do_reset(self, line):
        """deletes all table entries in a database
        Usage: reset | reset store
        """
        self.cursor.execute("DROP TABLE transactions;")
        self.cursor.execute("DROP TABLE customers;")
        self.db.commit()
        DBSetup.setup(self)
        DBSetup.store_init()

    def do_quit(self, line):
        """Quit command to exit the program"""
        self.cursor.close()
        self.db.close()
        return True


if __name__ == "__main__":
    DBSetup().cmdloop()
