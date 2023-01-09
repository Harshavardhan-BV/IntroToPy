# Installation

For this course we will be using vanilla python. An alternate would be to use anaconda which packages python along with a few packages/libraries and handles environment and package management. However, I have personally faced multiple problems with it and would prefer to avoid it.

## Installing python
- We will be installing the latest version, which at the time of writing is python 3.11.1
- Download the installer from:
	- [For Windows (64bit)](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)
	- [For Mac OS](https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg)
	- For Linux (Ubuntu/Debian): Should be pre-installed, to be sure run
	```
	sudo apt install python3 python3-dev python3-pip python-is-python3
	```
- Run the installer 
- Make sure to check **Add python to PATH**
- Follow the instructions on screen
- Reboot your system

## Running python
- Open a terminal (or cmd.exe) and run the command `python`
- You'll get a shell as follows 
```
> python
Python 3.11.1 (main, Dec  7 2022, 00:00:00) [GCC 12.2.1 20221121 (Red Hat 12.2.1-4)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
- Make sure you don't get python 2.x. Remove the python2 versions you have if possible 
- You can run any commands in the shell if you wish
- Type `exit()` or `Ctrl-D` to exit

You have successfully installed python. However, this is not a user friendly way to run things, hence we would be installing an IDE (similar to RStudio in Kishore's course)

## Installing Jupyter
Jupyter Notebook is one particular IDE that gives a very interactive environment. The files are stored in a (.ipynb) notebook format which is similar to the .Rmd format.

- Open a terminal (or cmd.exe) and run the following code
```
pip install --user notebook 
```
- On windows there seems to be issues with the path, run the following command. **WARNING**: Make sure to type it correctly, or it might break your system
```
setx path "%PATH%;%APPDATA\python\python311\Scripts"
```
- Reboot your system

## Installing packages

 `pip` is the package management software for python, aka how you would install/remove/update packages.

- Let us install the package numpy with the following command. Note: `--user` is specified so that it installs the package in the user directory and avoid any permission errors
```
pip install --user numpy
```
- Now to remove it
```
pip uninstall --user numpy
```
- We can also install multiple packages at once with a requirements file 
	- Download the [requirements.txt](../requirements.txt) file in this repo
	- Change directory to wherever you downloaded (this might vary)
	```
	cd Downloads
	```
	- Install it with 
	```
	pip install --user -r requirement.txt
	```
	- To get such a file run. Note that this would contain a list of all the packages installed by you
	```
	pip freeze > requirement.txt
	```
- For updating packages I use pip-review
	- Install it with
	```
	pip install --user pip-review
	```
	- To update packages do
	```
	pip-review -i
	```

## Running Jupyter
- In a terminal run `jupyter notebook`
- It will open a browser window. Else click on one of the links in the terminal
- You can navigate the folders and create new files in this view
- Quit the program with the Quit button or `Ctrl-C` in the terminal 
- We shall run some actual codes in next class

## Optional notes

### Virtual environments
Virutal environments are independent sets of packages. We would not be using this for our course. But, it would be useful in future when you're working with a lot of packages and to minimize dependency clashes. 

- You can create a new environment at any path, for example a new folder `venv/base` in your current directory with the following command
```
python -m venv venv/base
```
- Activate the environment with the following command
```
# For Linux/Mac OS
source ./venv/base/bin/activate 
# For windows
.\venv\base\Scripts\activate
```
- If you face errors related to execution policy on windows, run the following command 
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- You can install packages into this environment with `pip` as you would normally
```
pip install -r requirements.txt
```
- After you're done, deactivate your environment with
```
deactivate
```

### Linux
If you would like to get into serious programming, consider learning Linux as it is designed with programmers in mind and many of the headaches faced with windows can be avoided. However, teaching Linux is not an objective for this course. Consider [WSL(Windows Subsystem for Linux)]() if you would like to use a Linux shell inside a Windows installation.