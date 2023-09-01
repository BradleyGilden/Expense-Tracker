#!/usr/bin/python3
"""
This module contains the main interface of the Expense-Tracker
Author: Bradley Gilden
"""
import mysql.connector
BaseCmd = __import__("base-cmd").BaseCmd


class Console(BaseCmd):
    """Simple cmd interface to manage the expenses Database
    """

    def __init__(self):
        """Constructor for the console class"""
        super().__init__()

    def do_connect(self, line):
        """Establishes connection to database"""
        excpt = False
        try:
            self.db = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='Nanospartan@117'
            )
        except mysql.connector.Error as e:
            err = f"""\033[41m Database Connection Failed:\033[47m\033[30m{e} \
\033[0m\n"""
            print(err)
            self.default("connect fail")
            excpt = True
        if excpt is False:
            self.default("connect success")
            self.cursor = self.db.cursor()

    def do_setup(self, line):
        """sets up database
        """
        


if __name__ == '__main__':
    Console().cmdloop()
