#!/usr/bin/env python3
"""
This module contains the main interface of the Expense-Tracker
Author: Bradley Gilden
"""
from dbsetup import DBSetup


class Console(DBSetup):
    """Creates an interface to easily calculate expenses of users
    """

    def do_add(self, line):
        """adds user to customer database
        """
        args = line.split()
        arglen = len(args)
        insert = "INSERT INTO customers (name) VALUES ('{}');"
        insert2 = "INSERT INTO customers (name, vault) VALUES ('{}', {});"
        select = "SELECT name FROM customers WHERE name='{}';"
        update = "UPDATE customers SET vault = {} WHERE name = '{}'"

        if arglen == 1:
            self.cursor.execute(select.format(args[0]))
            output = self.cursor.fetchall()
            if not output:
                self.cursor.execute(insert.format(args[0]))
            else:
                print(f"\033[31mUser {args[0]} already exists")
                self.default("fail 0")
        elif arglen == 2:
            self.cursor.execute(select.format(args[0]))
            output = self.cursor.fetchall()
            condition = Console.valtype(args[1])
            if not output and condition:
                self.cursor.execute(insert2.format(args[0], args[1]))
                self.db.commit()
            elif output and condition:
                self.cursor.execute(update.format(args[1], args[0]))
                self.db.commit()
            else:
                print(f"\033[31mIncorrect type: {args[1]}\033[0m")
                self.default("fail 0")
        else:
            print("\033[31mUsage: add <user> | add <user> <value>\033[0m")
            self.default("fail 0")

    def do_deposit(self, line):
        """used to adjust current amount someone has stored in their vault
        """
        args = line.split()
        user = self.active_user
        arglen = len(args)
        update = "UPDATE customers SET vault = {} WHERE name = '{}'"
        select = f"SELECT vault FROM customers WHERE name = '{user}'"

        if user != "" and arglen == 1:
            self.cursor.execute(select)
            output = self.cursor.fetchone()
            condition = Console.valtype(args[0])
            if not condition:
                print(f"\033[31mIncorrect type: {args[0]}\033[0m")
                self.default("fail 0")
            else:
                value = eval(args[0]) + output[0]
                self.cursor.execute(update.format(value, user))
        else:
            print("""\033[31mPlease login as a user before depositing or \
use the correct format: deposit <value>\033[0m""")
            self.default("fail 0")

    def do_login(self, line):
        """login as a user in order to make transactions for that user
        """
        user = line.strip()
        select = "SELECT name FROM customers WHERE name='{}';"

        if (len(user) == 0):
            print("\033[31mUsage: login <user>\033[0m")
        else:
            self.cursor.execute(select.format(user))
            output = self.cursor.fetchone()
            if not output:
                print(f"\033[31mUser does not exist: {user}\033[0m")
                self.default("fail 0")
            else:
                self.active_user = user
                self.default(f"user {self.active_user.split()[0]}")

    def do_logout(self, line):
        """logouts currently logged in user"""
        self.active_user = ""
        # reset prompt
        self.default("")

    @staticmethod
    def valtype(string):
        """confirms datatype inside string
        """
        if type(string) != str:
            False
        try:
            value = eval(string)
            return (type(value) == int or type(value) == float)
        except (SyntaxError, ValueError, NameError, TypeError):
            return False


if __name__ == '__main__':
    Console().cmdloop()
