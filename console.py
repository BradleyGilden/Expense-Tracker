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
        arglen = len(args)
        select = "SELECT name, vault FROM customers WHERE name='{}';"
        update = "UPDATE customers SET vault = {} WHERE name = '{}'"

        if arglen == 1:
            print('\033[31m Value property missing\033[0m')
            self.default('fail 0')
        elif arglen == 2:
            self.cursor.execute(select.format(args[0]))
            output = self.cursor.fetchone()
            condition = Console.valtype(args[1])
            if not condition:
                print(f"\033[31mIncorrect type: {args[1]}\033[0m")
                self.default("fail 0")
            elif output and condition:
                value = eval(args[1]) + output[1]
                self.cursor.execute(update.format(value, args[0]))
            else:
                print(f"\033[31mCustomer does not exist: {args[0]}\033[0m")
                self.default("fail 0")
        else:
            print("\033[31mUsage: deposit <user> <value>\033[0m")
            self.default("fail 0")

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
