<h1 align="center">Expense-Tracker</h1>

<p align="center"><img src="images/mysql-official.svg" height=140><img src="images/plus-60.png" height=140><img src="images/1869px-Python-logo-notext.svg.png" height=140></p>

## Index:

* #### [Description](#description-1)
* #### [Dependencies](#dependencies-1)
* #### [Running The Program](#running-the-program-1)
* #### [Signup & Login](#signup--login-1)
* #### [Basic Commands](#description)
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
N.B allowed card formats:

* 0000-0000-0000-0000
* 0000 0000 0000 0000
* 0000000000000000
