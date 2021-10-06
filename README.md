# Example Exercise

This is an example exercise for the Python Tool Manager.

## Requirements

* Python >= 3.6
* Access to the Python Tool Manager
* Pycharm CE or Professional (not mandatory, but recommended)
* Basic knowledge in the Python programming language

## Quickstart

Proceed the following steps to set up your project:

1. Clone or download this repository.
2. Navigate to the project folder and run the appropriate init script.
3. Adjust the exercise UUID according to your created exercise in the tool manager.

## Manual Setup

For a manual setup, you need to create a Python virtual environment. To do so, execute the following command in a
terminal inside your project folder:

````bash
python -m venv venv
````

This will create a new `venv` folder, containing the virtual environment. It is mandatory, that the folder is
named `venv`. Otherwise you need to adjust the `.dockerignore` file.

## Hints

* The `start` method in the `Exercise` class is the main entrypoint for the application.
* Place your static assets inside the `static` folder.
* It is recommended to put your project under version control.
