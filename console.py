#!/usr/bin/python3
import cmd
import os


class Interpreter(cmd.Cmd):
    """Simple cmd interface to manage the expenses Database
    """

    fsprompt = "\033[34mMyCoin\033[33m<{}>\033[32m$\033[0m "
    fdprompt = "\033[34mMyCoin\033[33m<{}>\n\033[32m$\033[0m "
    prompt = "\033[34mMyCoin\033[33m<>\033[32m$\033[0m "
    dprompt = "\033[34mMyCoin\033[33m<>\n\033[32m$\033[0m "
    sprompt = "\033[34mMyCoin\033[33m<>\033[32m$\033[0m "

    def default(self, line):
        """Handles default processing of errors"""
        invalid = f"""\033[41mInvalid prompt: \
\033[47m\033[30m{line.split()[0]}\033[0m\n"""
        print(invalid)
        if '\n' in Interpreter.prompt:
            fmt = Interpreter.fdprompt.format("\033[31mError\033[33m")
        else:
            fmt = Interpreter.fsprompt.format("\033[31mError\033[33m")
        Interpreter.prompt = fmt

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
                Interpreter.prompt = Interpreter.sprompt
            else:
                Interpreter.prompt = Interpreter.dprompt

    def precmd(self, line):
        """Ensures default prompt is constant after error detection
        """
        if '\n' in Interpreter.prompt:
            Interpreter.prompt = Interpreter.dprompt
        else:
            Interpreter.prompt = Interpreter.sprompt
        return line


if __name__ == '__main__':
    Interpreter().cmdloop()
