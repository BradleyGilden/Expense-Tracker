#!/usr/bin/python3
"""
This module is the foundation of the Expense-Tracker command interface
Author: Bradley Gilden
"""
import cmd
import os


class BaseCmd(cmd.Cmd):
    """Simple cmd interface to manage the expenses Database
    """
    prompt = "\033[34mExpenseTracker\033[33m<>\033[32m$\033[0m "

    def __init__(self):
        """constructor for cmd class
        """
        super().__init__()
        self.fsprompt = "\033[34mExpenseTracker\033[33m<{}>\033[32m$\033[0m "
        self.fdprompt = "\033[34mExpenseTracker\033[33m<{}>\n\033[32m$\033[0m "
        self.dprompt = "\033[34mExpenseTracker\033[33m<>\n\033[32m$\033[0m "
        self.sprompt = "\033[34mExpenseTracker\033[33m<>\033[32m$\033[0m "

    def default(self, line):
        """Handles default processing of errors"""
        args = line.split()
        invalid = f"""\033[41mInvalid prompt: \
\033[47m\033[30m{args[0]}\033[0m\n"""

        if args[0] == "connect":
            if args[1] == "fail" and '\n' in BaseCmd.prompt:
                fmt = self.fdprompt.format("\033[31m\
Connection Failed\033[33m")
            elif args[1] == "fail":
                fmt = self.fsprompt.format("\033[31m\
Connection Failed\033[33m")
            else:
                fmt = self.fsprompt.format("\033[32mConnected...\033[33m")
        elif '\n' in BaseCmd.prompt:
            print(invalid)
            fmt = self.fdprompt.format("\033[31mError\033[33m")
        else:
            print(invalid)
            fmt = self.fsprompt.format("\033[31mError\033[33m")
        BaseCmd.prompt = fmt

    def emptyline(self):
        """Behaviour when an emptyline is encountered
        """
        pass

    def do_clear(self, line):
        """clears terminal screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_EOF(self, line):
        """Handles EOF signal by exiting the Shell
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_prompt(self, line):
        """Changes prompt orientation
        """
        args = line.split()
        arglen = len(args)

        if arglen < 1 or args[0] not in {"double", "single"}:
            print("Usage: prompt <double|single>")
        else:
            if args[0] == "single":
                BaseCmd.prompt = self.sprompt
            else:
                BaseCmd.prompt = self.dprompt

    def precmd(self, line):
        """Ensures default prompt is constant after error detection
        """
        if '\n' in BaseCmd.prompt:
            BaseCmd.prompt = self.dprompt
        else:
            BaseCmd.prompt = self.sprompt
        return line

    def do_sh(self, line):
        """Enables user to execute shell commands without exiting the console
        """
        if (len(line) == 0):
            print("Usage: sh <shell cmd>")
        else:
            os.system(line)


if __name__ == '__main__':
    BaseCmd().cmdloop()
