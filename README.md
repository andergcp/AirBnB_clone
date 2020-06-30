# AirBnB_clone
[![Contributors][contributors-shield]][contributors-url]

<p align="center">
  <img src="https://press.airbnb.com/wp-content/uploads/sites/4/2017/07/airbnb-newsroom-twitter-card-default.png?fit=2000%2C1050" width="60" height="32">
  <h2 align="center">AirBnB_clone</h2>
  <h3 align="center">Command Interpreter</h3>
</p>

### This project is a command interpreter to manage our AirBnB clone objects.
This is the first step towards building a first full web application: the AirBnB clone.
The command interpreter in this project will be able to manage the objects of the AirBnb clone project:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Usage
#### Execution
* Interactive mode. Example:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

* Non-interactive mode. Example:

```sh
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
```

### Authors
* Andrés Ariza - [Githug](https://github.com/afarizap) - [LinkedIn](https://www.linkedin.com/in/arizarocks)
* Anderson Castiblanco [Github](https://github.com/andergcp) - [LinkedIn](https://www.linkedin.com/in/anderson-castiblanco-prieto)

[contributors-shield]: https://img.shields.io/github/contributors/andergcp/AirBnB_clone?style=social&logo=appveyor
[contributors-url]: https://github.com/andergcp/AirBnB_clone/graphs/contributors
