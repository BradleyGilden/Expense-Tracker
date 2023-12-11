<h1 align="center">Expense-Tracker</h1>
<br>
<p align="center"><img src="images/mysql-official.svg" height=140><img src="images/plus-60.png" height=140><img src="images/1869px-Python-logo-notext.svg.png" height=140></p>

## Index:

* #### [Description](#description-1)
* #### [Dependencies](#dependencies-1)
* #### [Running The Program](#running-the-program-1)
* #### [Signup & Login](#signup--login-1)
* #### [Terminal Interaction Commands](#terminal-interaction-commands-1)
* #### [Global Commands](#global-commands-1)
* #### [>>> *Tracking Your Expenses* <<<](#tracking-your-expenses)
* #### [Authors & Licencing](#authors--licencing-1)


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

* Ensure MySQL service is running: `sudo service mysql start`
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

This is an important step as you will not be able to make purchases or check your balance without logging in as a user. To signup as an user, use the command `signup`:
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
To logout a user account, simply type `logout`:
```
ExpenseTracker<Walter White>$ logout
ExpenseTracker<>$ 
```
N.B allowed card formats:

* 0000-0000-0000-0000
* 0000 0000 0000 0000
* 0000000000000000

## Terminal Interaction Commands

These are commands that are used to navigate the shell or not part of the program's primary functionality

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

## Global Commands

Global Commands are commands that are not user specific, as you do not need
to be logged in as a user to execute these commands

* The command: `list` has many uses such as:
  * `list users` -> lists users that have accounts
  ```
  ExpenseTracker<>$ list users
  Turid Ozil
  Magne Lorrel
  James Dashner
  Ezio Auditore De Firenze
  ```
  * `list stores` -> list available stores in txt database
  ```
  ExpenseTracker<>$ list stores
  Spark Electronics
  Carlos Grocers
  Dripped Out
  ```
  * `list store <store name>` -> list items in a particular store
  ```
  ExpenseTracker<>$ list store Spark Electronics
  ITEMS:                 PRICE($):
  --------------------------------
  Raspberry Pi Pico      $8.00
  Arduino Uno            $12.99
  ESP8266 WiFi Module    $3.49
  16x2 LCD Display       $4.95
  Raspberry Pi 4         $45.00
  Arduino Nano           $6.75
  ESP32 Development Kit  $15.99
  OLED Display Module    $9.50
  Arduino Mega 2560      $19.95
  NodeMCU ESP8266        $5.99
  ```
  N.B listing a store will automatically refresh the stores contents if you were to add any rows

* The command `reset` will reset all data in database hence deleting all users and their transactions. `reset store` will refresh all the store items if any new entries were added or old ones were deleted

## Tracking Your Expenses

To track a Users expenses, you first have to [signup and/or login](#signup--login-1) as a user to execute commands to track a specific users expenses

All stores, their item list and their prices are stored in [store.txt](store.txt). The format for a store entry is: <br>
`"<store name>" "<store item>" "<store price>"`. You can add or delete entries in the store.txt file although make sure to refresh your edits by using:  `reset store` or `list stores`

### Commands:

* `balance` ->  Displays A users current balance
```
ExpenseTracker<Cedric Diggory>$ balance
Cedric Diggory  ************2983        $22,340.23
```
* `deposit` -> Allows user to deposit money in their account
```
ExpenseTracker<Cedric Diggory>$ deposit 10000
ExpenseTracker<Cedric Diggory>$ balance
Cedric Diggory  ************2983        $32,340.23
```

* `purchase` -> Allows user to make purchases. Note: if no quantity is entered it automatically assumes a quantity of 1
```
ExpenseTracker<Cedric Diggory>$ purchase
************* Purchase Menu *************

Enter Store Name: Spark Electronics
Enter Item Name: Raspberry Pi Pico 
Quantity: 8
Amount spent: $64.00
Balance: $32,276.23
```

* `receipt` -> prints out receipt of all the purchases of a user
```
ExpenseTracker<Cedric Diggory>$ receipt
************* Receipt of Cedric Diggory **************

 Merchant: Spark Electronics
 Items Purchased:
 Item: Raspberry Pi Pico
 Quantity: 8
 Unit Price: $8.00
 Subtotal: $64.00

 Item: Arduino Uno
 Quantity: 2
 Unit Price: $12.99
 Subtotal: $25.98

 Merchant: Dripped Out
 Items Purchased:
 Item: Baseball Cap
 Quantity: 3
 Unit Price: $14.50
 Subtotal: $43.50

 Item: Athletic Sneakers
 Quantity: 1
 Unit Price: $59.99
 Subtotal: $59.99

Total Amount: $193.47
Payment Method: Card ending in ************2983
```

<hr>

## Authors & Licencing

| Authors          | Licencing           |
|------------------|---------------------|
|[AUTHORS](./AUTHORS)| [Licence](./LICENSE)|
