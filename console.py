#!/usr/bin/python3
"""
This module contains the main interface of the Expense-Tracker
Author: Bradley Gilden
"""
BaseCmd = __import__("base-cmd").BaseCmd


class Console(BaseCmd):
    """Simple cmd interface to manage the expenses Database
    """

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    Console().cmdloop()
