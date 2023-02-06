# AirBnB_clone
AirBnB clone - The console

##### DESCRIPTION ####
This project is the first step towards building a full web application of the AirBnB clone. In this first step we are building a console, a custom command interpreter that will be used in subsequent AirBnB projects to manage objects of our classes.

This console will allow us to do the following:

# Create a new object
# Retrieve an object from a file, a database etc…
# Do operations on objects (count, compute stats, etc…)
# Update attributes of an object
# Destroy an object.

#### USAGE ####
# The console can be run in both interactive and non-interactive mode.
# It prints a prompt (hbnb) and waits for the user for input.

##### INTERACTIVE MODE ####

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

##### NON INTERACTIVE MODE ####

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
