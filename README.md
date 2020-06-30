# AirBnB_clone
[![Contributors][contributors-shield]][contributors-url]

<p align="center">
  <img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200630%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200630T223717Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=41b31543d4dd5050f6bca2fcb521553d195bada7e2a2a64dd9ae199cdb73d341">
  <h2 align="center">AirBnB_clone</h2>
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
