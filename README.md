# First steps with django

## Setup Virtual Environment 

### Installing virtualenv

- Linux and macOS:
```sh
python3 -m pip install --user virtualenv
```

- Windows:
```sh
py -m pip install --user virtualenv
```

### Creating a virtual environment


```sh
$ mdkdir <folder_project>
$ cd <folder_project>
```

- Linux and macOS(recommend):
```sh
$ virtualenv -p python3 .
```
Or:
```sh
$ python3 -m venv env
```

- Windows:
```sh
$ py -m venv env
```

### Activating a virtual environment

- Linux and macOS:
```sh
$ source env/bin/activate
```

- Windows:
```sh
$ .\env\Scripts\activate.bat
```
You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

- Linux and macOS:
```sh
$ which python
.../env/bin/python
```
On Windows:
```sh
$ where python
.../env/bin/python.exe
```

### Leaving the virtual environment

```sh
$ deactivate
```
View more detail here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Install Django

- Linux and macOS:
```sh
$ pip3 install django
```

- Windows:
```sh
$ pip install django
```

### Start a Blank Django Project

```sh
$ django-admin startproject <folder_project>
```
