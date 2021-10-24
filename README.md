# First steps with django

## Setup Virtual Environment  - LINUX

### Installing virtualenv

```sh
python3 -m pip install --user virtualenv
```

### Creating a virtual environment

```sh
mdkdir <folder_project>
cd <folder_project>
```
```sh
virtualenv -p python3 .
```

### Activating a virtual environment

```sh
source bin/activate
```

You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

```sh
which python
```

### Leaving the virtual environment

```sh
deactivate
```

View more detail here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Install Django

```sh
pip3 install django
```

### Start a Blank Django Project

```sh
mdkri src
```
```sh
django-admin startproject <folder_project> .
```

-----


## Setup Virtual Environment - WINDOWS

### Installing virtualenv

```sh
py -m pip install --user virtualenv
```

### Creating a virtual environment

```sh
mdkdir <folder_project>
cd <folder_project>
```
```sh
py -m venv .
```

### Activating a virtual environment

```sh
.\env\Scripts\activate.bat
```
You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

```sh
where python
```

### Leaving the virtual environment

```sh
deactivate
```
View more detail here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Install Django

```sh
pip install django
```

### Start a Blank Django Project

```sh
mdkri src
```
```sh
django-admin startproject <folder_project> .
```
