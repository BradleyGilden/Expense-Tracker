<h1 align="center">Expense-Tracker</h1>

<p align="center"><img src="images/mysql-official.svg" height=140><img src="images/plus-60.png" height=140><img src="images/1869px-Python-logo-notext.svg.png" height=140></p>

## Index:

* #### [Description](#description-1)
* #### [Dependencies](#dependencies-1)
* #### [Running The Program](#running-the-program-1)
* #### [Signup & Login](#signup--login-1)
* #### [Terminal Interaction Commands](#terminal-interaction-commands-1)
* #### [Description](#description)
* #### [Description](#description)
* #### [Description](#description)
* #### [Description](#description)


## Description
This Project is was created to make it convenient in order to track expenses made on a daily basis, encouraging people to be smarter when handling their finances.

The Expense Tracker is accessed via CLI, it's functionalities make it compatible with Unix-bases systems as well as Windows

## Dependencies

This project has the following prerequisites:

* Python3
  > Install (Linux):
  >> Ubuntu/Debian
  ```bash
    sudo apt install python3
  ```
  >> Fedora
  ```bash
    sudo apt install python3
  ```
  >> CentOS/RHEL
  ```bash
  sudo yum install epel-release
  sudo yum install python3
  ```
  >> Arch Linux
  ```bash
    sudo pacman -S python
  ```
  > Install(Windows):
    [here](https://www.python.org/downloads/)
* MySQL
  > Install (Linux):
  >> Ubuntu/Debian
  ```bash
    sudo apt install mysql-server
  ```
  >> Fedora
  ```bash
    sudo apt install mysql-server
  ```
  >> CentOS/RHEL
  ```bash
  sudo yum install mysql-server
  ```
  >> Arch Linux
  ```bash
    sudo pacman -S mysql-server
  ```
  > Install(Windows):
  [here](https://dev.mysql.com/downloads/mysql/)
* Python MySQL-connector
  > Install:
  ```
  pip3 install mysql-connector
  pip3 install --upgrade mysql-connector-python
  ```

## Running The Program

* Ensure mysql service is running: `sudo service mysql start`
* To run the program: `./console.py`
* Database login example:
  ```
  $ ./console
  
  ************* Mysql Login **************
  
  Enter hostname: localhost
  Enter user: root
  Enter password:
  ExpenseTracker<Connected...>$
  ```

## Signup & Login

This is an important step as you will not be able to make purchases or check your balance without loging in as a user. To signup as an user, use the command `signup`:
```
ExpenseTracker<>$ signup
************* User Signup *************

Username (letters only): Walter White
Card No. (16 digits): 8765 4321 2342 1267 
```
likewise to login use the command `login`:
```
ExpenseTracker<>$ login 
************* User Login *************

Username (letters only): Walter White
Card No. (16 digits): 8765 4321 2342 1267
ExpenseTracker<Walter White>$ 
```
To logut a user account, simply type `logout`:
```
ExpenseTracker<Walter White>$ logout
ExpenseTracker<>$ 
```
N.B allowed card formats:

* 0000-0000-0000-0000
* 0000 0000 0000 0000
* 0000000000000000

## Terminal Interaction Commands

* Shell Commands start with `sh`:
```
ExpenseTracker<>$ sh ls -l
total 52
-rw-r--r-- 1 nightlock nightlock  2895 Sep 20 19:07 README.md
drwxr-xr-x 2 nightlock nightlock  4096 Sep 19 10:33 __pycache__
-rwxr-xr-x 1 nightlock nightlock  4401 Sep 13 17:36 base-cmd.py
-rwxr-xr-x 1 nightlock nightlock 11295 Sep 18 21:08 console.py
-rwxr-xr-x 1 nightlock nightlock  5706 Sep 19 10:30 dbsetup.py
drwxr-xr-x 2 nightlock nightlock  4096 Sep 18 21:10 images
-rw-r--r-- 1 nightlock nightlock    53 Sep 19 10:34 raw.sql
-rw-r--r-- 1 nightlock nightlock  1644 Sep 10 20:28 store.txt
-rw-r--r-- 1 nightlock nightlock   249 Sep  9 09:55 testdata.txt
```

* To clear the interface just type `clear`
```
ExpenseTracker<>$ clear
```
* To cancel input enter CTRL+C
```
ExpenseTracker<>$ purcase^C
ExpenseTracker<>$ ^C
ExpenseTracker<>$ ^C
ExpenseTracker<>$ 
```
* To view database with raw SQL commands use the start command with `db`:
```
ExpenseTracker<>$ db select * from expenses;
(1, 'Lucy Greyhart', '1234567891011121', Decimal('455.35'))
```

* To exit the interface type `quit` or enter CTRL+D:
```
ExpenseTracker<>$ quit
$
```
* For any help with commands just type `help` or `help <cmd>`

```
ExpenseTracker<>$ help

Documented commands (type help <topic>):
========================================
EOF      clear  deposit  list   logout  purchase  receipt  sh    
balance  db     help     login  prompt  quit      reset    signup

ExpenseTracker<>$ help list
lists available stores and available items in specific stores
        Usage: list users | list stores | list store <name>
```

