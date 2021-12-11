from termcolor import colored


def help():
    return """
        The correct use of this script is: repo.py --name 'your_project_name' --lan 'your_main_project_language'
        You can add an extra flag --private if you want to create your repository as private.

        --name:
            - This is the name of your project, and will automatically name your online repository the same

        --lan:
            - This is the main language of your project. Use the extension as the flag attribute.
            - More on lan below.

        --private:
            - This is the private settings flag.
            - default is it left out and will create a public repository.
            - if used, will create a private repository.

        --base:
            - This is the flag indicating you want to create a new standard base folder
            - default it is left out and will use the base folder specified in your config.json file
            - if no base folder is specified in your config.json file, a new standard base folder will be created anyway


        # LANGUAGES
        -----------
        A list of supported lan settings:
            - py -> creates a repository with main language python
            - php -> creates a repository with main language PHP
            - web -> creates a webfolder


        # REPOSITORIES
        --------------
        Default each project folder will be created with the following files:
            - .gitignore
            - .README.md

        Depending on your lan setting the following will be added:
        ## --lan py
        -----------
        If you set the lan flag to py, the following files and directories will be added to your project folder:
            - setup.py
            - config_ex.json
            - config.json
            - subfolder with project name as package

        You will be provided with a package subfolder named after your project. Inside you will find the following files:
            - __init__.py
            - __version__.py
            - main.py

        Your project directory structure will be as follows:
            <project_name>
                |- .gitignore
                |- README.md
                |- setup.py
                |- config_ex.json
                |- config.json
                |- <package_name>
                    |- __init__.py
                    |- __version__.py
                    |- main.py

        ## --lan php
        ------------
        If you set the lan flag to php, the following files and directories will be added to your project folder:
            - main.php

        Your project directory structure will be as follows:
            <project_name>
                |- .gitignore
                |- README.md
                |- main.php

        ## --lan web
        -------------
        If you set the lan flag to web, the following files and directories will be added to your project folder:
            - +assets
            - css
            - images
            - index.html

        You will be provided with a css folder containing the following items:
            - base
            - style.scss

        Your base folder will contain the following items:
            - _reset.scss
            - _fonts.scss
            - _mixins.scss
            - _extends.scss
            - _variables.scss

        Your project directory structure will be as follows:
            <project_name>
                |- +assets
                |- css
                |   |- reset.css
                |   |- style.css
                |- images
                |- .gitignore
                |- README.md
                |- index.html

        """


def helpSection(begin, end):
    text = help()

    start = text.find(begin)
    stop = text[start + len(begin) :].find(end)

    if stop == -1:
        stop = len(text)

    return text[start:stop]


def helpSpecificLicense(app, string, licenses):
    license = string[string.find("-") + 1 :]

    if int(license) > len(licenses) - 1:
        print(f"invalid license, a license with number {license} does not exist")
        return False

    license_key = app.api.getLicenses()[int(license)][int(license)]
    data = app.api.getLicense(license_key)
    print(len(data["permissions"]), len(data["limitations"]))
    print(f"{data['description']}")
    print(f"below is a list of the permissions and limitations in regard {data['name']}\n")

    for i in range(max(len(data["limitations"]), len(data["permissions"]))):
        perm = ""
        lim = ""
        if i < len(data["limitations"]):
            lim = data["limitations"][i]
        if i < len(data["permissions"]):
            perm = data["permissions"][i]
        print(f"{' '*5}{colored('+', 'green')} {perm}{' '*(25-7-len(perm))}{colored('-', 'red')} {lim}")

    print("\n")
