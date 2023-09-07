#!/usr/bin/env python3
"""
This module contains the main interface of the Expense-Tracker
Author: Bradley Gilden
"""
from dbsetup import DBSetup


class Console(DBSetup):
    """Creates an interface to easily calculate expenses of users
    """

    def do_signup(self, line):
        """adds user to customer database
        """
        insert = "INSERT INTO customers (name, card) VALUES ('{}', '{}');"
        title = """\033[1m\033[46m\033[30m************* User Signup \
*************\033[0m"""
        userin = """\033[36mUsername (\033[3mletters only\033[0m\033[36): \
\033[0m"""
        cardin = "\033[36mCard No. (\033[3mpassword\033[0m\033[36): \033[0m"
        select = "SELECT name FROM customers where name = '{}'"
        exists = True

        user = input(userin).strip()
        if not user.isalpha():
            print("\033[31m Please Enter Valid Username [letters only]")
        else:
            while exists:
                self.cursor.execute(select.format(user))
                output = self.cursor.fetchone()
                if output:
                    print(f"\033[31mUsername taken: {user}\033[0m")
                else:
                    exists = False
        card = input(cardin).strip()
        



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
