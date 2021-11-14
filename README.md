# Introduction

This Repo package was designed to ease the manual labor of creating a new project and github repository. the repo.py script can handle 2 arguments, 1 of which is required. Name of the project, which will be the name of the main folder as well as the name of the github repository is required. Make sure the new project name is not present as a github repository already, if it is no new repository will be created.

For the repo.py script to run you will need Python installed on your machine and have a github account. Follow the next steps to make your life a lot easier.

<<<<<<< HEAD
To get started select the branch you desire. Branches are named to scripting languages
=======
##STEP 1: Create GITHUB_TOKEN
  1) Create a github-account
  2) Navigate to github.com/settings/profile
  3) click "Developer settings" button
  4) click "Personal access tokens" button
  5) click "Generate new token" button
  6) enter a note and check desired permissions
  7) click Generate token
  8) Copy your generated token

##STEP 2: Setup config 
  1) change the config_ex.json file into config.json
  2) paste your generated token in the "YOUR_GITHUB_TOKEN" placeholder
  3) save the file

##STEP 3: Start creating repositories
  1) open cmd in windows or terminal in OS
  2) type in "py <path/to/repo/main.py> --name <repo_name> and hit enter
  3) Watch how the scripts generates a package at the cwd and a new repository on github.

  # Examples
  1) python C:/repo/main.py --name example_of_puclic_repo
  2) python C:/repo/main.py --name example_of_private_repo --private
  3) python C:/repo/main.py --name example_with_var_env --env example
>>>>>>> 8a5b24f366cc87c4f6617e1d3bd2087964853047
