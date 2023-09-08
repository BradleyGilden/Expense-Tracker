#!/usr/bin/env python3
"""
This module contains the main interface of the Expense-Tracker
Author: Bradley Gilden
"""
from dbsetup import DBSetup
from re import split as resplit
from dbsetup import search as research


class Console(DBSetup):
    """Creates an interface to easily calculate expenses of users
    """

    def do_signup(self, line):
        """adds user to customer database
        """
        insert = "INSERT INTO customers (name, card) VALUES ('{}', '{}');"
        title = """\033[1m\033[46m\033[30m************* User Signup \
*************\033[0m\n"""
        userin = """\033[36mUsername (\033[3mletters only\033[0m\033[36m): \
\033[0m"""
        cardin = "\033[36mCard No. (\033[3m16 digits\033[0m\033[36m): \033[0m"
        select = "SELECT name FROM customers where name = '{}'"
        invalid_user = "\033[31m Please Enter Valid Username [letters only]"
        invalid_card = "\033[31mPlease Enter a Valid Card Number\033[0m"
        exists = True

        print(title)
        try:
            while exists:
                user = input(userin).strip()
                self.cursor.execute(select.format(user))
                output = self.cursor.fetchone()
                if output:
                    print(f"\033[31mUsername taken: {user}\033[0m")
                elif not research(r'[a-zA-Z ]+', user):
                    print(invalid_user)
                else:
                    exists = False
            if not exists:
                exists = True
                while exists:
                    card = input(cardin).strip()
                    card = resplit(r'[- ]', card)
                    card = ''.join(card)
                    if not card.isdigit() or len(card) != 16:
                        print(invalid_card)
                    else:
                        self.cursor.execute(insert.format(user, card))
                        self.db.commit()
                        exists = False
        except KeyboardInterrupt:
            print()
            self.default('')

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
        select = "SELECT name, card FROM customers WHERE name = '{}';"
        invalid_card = "\033[31mCard Format Invalid\033[0m"
    # bad_entry = "\033[31mPlease add correct card number or username\033[0m"
        title = """\033[1m\033[46m\033[30m************* User Login \
*************\033[0m\n"""
        userin = """\033[36mUsername (\033[3mletters only\033[0m\033[36m): \
\033[0m"""
        cardin = "\033[36mCard No. (\033[3m16 digits\033[0m\033[36m): \033[0m"
        exists = True

        print(title)
        try:
            while exists:
                user = input(userin).strip()
                self.cursor.execute(select.format(user))
                output = self.cursor.fetchone()
                if not output:
                    print(f"\033[31mUsername does not exist: {user}\033[0m")
                else:
                    exists = False
            if not exists:
                exists = True
                while exists:
                    card = input(cardin).strip()
                    card = resplit(r'[- ]', card)
                    card = ''.join(card)
                    self.cursor.execute(select.format(user))
                    output = self.cursor.fetchone()
                    if not card.isdigit() or len(card) != 16:
                        print(invalid_card)
                    elif card != output[1]:
                        print("\033[31mCard does not match username\033[0m")
                    else:
                        self.active_user = user
                        self.default(f"user {self.active_user.split()[0]}")
                        exists = False
        except KeyboardInterrupt:
            print()
            self.default('')

    def do_logout(self, line):
        """logouts currently logged in user
        """
        self.active_user = ""
        # reset prompt
        self.default("")

    def do_balance(self, line):
        """checks user balance
        """
        user = self.active_user
        select = f"SELECT card, vault FROM customers where name = '{user}'"
        if user == "":
            print("\033[31mPlease login first before checking balance\033[0m")
        else:
            self.cursor.execute(select)
            output = self.cursor.fetchone()
            print(f"{user}\t************{output[0][12:]}\t${output[1]}")

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
