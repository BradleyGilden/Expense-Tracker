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
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS expenses")
        self.cursor.execute("USE expenses")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    vault DECIMAL(9, 2) DEFAULT 0.00
);""")

    def do_show(self, line):
        """Display database information
        """
        args = line.split()
        commands = {"tables", "databases"}
        fetch = True

        if args[0] not in commands:
            print("Usage: show <tables|databases>")
        else:
            if args[0] == "databases":
                self.cursor.execute("SHOW DATABASES;")
            else:
                try:
                    self.cursor.execute("SHOW TABLES;")
                except mysql.connector.Error:
                    print("please enter valid database name to view tables")
                    fetch = False
            if fetch:
                output = self.cursor.fetchall()
                for rows in output:
                    print(rows[0])

    @staticmethod
    def generate_login() -> list:
        """accepts user login details for mysql database
        """
        login = []

        print("\n\033[42m************* Mysql Login **************\033[0m\n")
        login.append(input("\033[32mEnter hostname: "))
        login.append(input("\033[32mEnter user: "))
        login.append(getpass.getpass("\033[32mEnter password: "))
        return login

    def do_quit(self, line):
        """Quit command to exit the program
        """
        self.cursor.close()
        self.db.close()
        return True


if __name__ == '__main__':
    Console().cmdloop()
