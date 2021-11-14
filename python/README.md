# Introduction

This Repo package was designed to ease the manual labor of creating a new project and github repository.
The repo.py script can handle 3 flags of which 2 are required:

-   --name: Required -> This is the name of your project and will automatically be the name as your online repository
-   --lan: Required -> This is the main extension of your project
-   --private: Optional -> This is the private setting for your repository (use the flag if you want your repository to be private / default setting is false so default repositories are public)

Make sure the new project name is not present as a github repository already. If it is, no new repository will be created.
In order to use the repo.py script to run properly, you will need Python installed on your machine and have a github account.

Follow the next steps to make your life a lot easier.

# Getting started

## STEP 1: Create GITHUB_TOKEN

1. Create a github-account
2. Navigate to github.com/settings/profile
3. click "Developer settings" button
4. click "Personal access tokens" button
5. click "Generate new token" button
6. enter a note and check desired permissions
7. click Generate token
8. Copy your generated token

## STEP 2: Setup up

### Setup with pip

-   open cmd in windows
-   type pip install git+https://github.com/Foebry/repo.git
-   in 3.5 you should use "path_to_python_folder//Lib//site-packages//repo"

## Setup with download

-   Download repo subfolder
-   In 3.5 you should use the path to where you pasted the folder

1. Rename the config_ex.json file into config.json
2. paste your generated token in the "YOUR_GITHUB_TOKEN" placeholder
3. OPTIONAL

-   set your email adress and name
-   set your github profile

4. save the config.json file

## STEP 3: Add to PATH

1. Right click on my computer
2. Go to Advanced system settings
3. Go to environment variables
4. Select the 'Path' variable and click edit
5. Click new and paste in the path to the repo-folder (eg. C://Users//this_user//Projects//repo)
6. Click OK 3 times
7. Restart your computer for theses changes to take effect

## STEP 4: Set default open

1. Right click on any file with .py extension
2. select the open with option
3. select Python and check the box to always open .py files with the Python program.
4. close the command line if necessary.

## STEP 5: Start creating repositories

1. open cmd in windows or terminal in OS
2. Navigate to your desired destination for creating a new project
3. If you want to create a new project folder in you main folder called projects, navigate to your main folder projects.
4. Type repo.py --name <your desired project name> --lan <the main extension of your project>
5. Follow the process and watch how your project is being created along with the online repository.
6. The repository will be created with a branch called main and another branch called develop.

# Help

For help open the command prompt or terminal and type repo.py --help

# Examples

1. repo.py --name example_of_puclic_repo --lan py -> creates a public project called example_of_public_repo with main language using python
2. repo.py --name example_of_private_repo --lan php --private -> creates a private project called example_of_private_repo with main language using php