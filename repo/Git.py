def init(package, repo, is_private):
    from secrets import GITHUB_PROFILE, GITHUB_TOKEN, EMAIL
    import os
    import requests

    profile = GITHUB_PROFILE

    # create Github repository
    url = "https://api.github.com/user/repos"
    payload = '{"name": "' + repo + '", "private": true}'
    if not is_private: payload = payload = '{"name": "' + repo + '", "private": false}'

    headers = {
        "Authorization": 'token '+ GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json"
    }
    requests.post(url, data=payload, headers=headers)

    os.system("git init")
    os.system("git remote add origin https://github.com/%s/%s" %(profile, repo))
    os.system("git config --global user.email %s" %EMAIL)
    os.system("git config --global user.name %s" %profile)
    os.chdir(package)


def ignore():
    import os
    IGNORE = """
/env
/logs
/Logs
.log
__pycache__
/tests
config.py
"""
    file = open(".gitignore", "w")
    file.write(IGNORE)
    file.close()


def chooseLicense():
    licenses = {
        1: 'Apache license 2.0',
        2: 'GNU General Public license v3.0',
        3: 'MIT license',
        4: 'BSD 2-Clause "Simplified" license',
        5: 'BSD 3-Clause "New" or "Revised" license',
        6: 'Boost Software license 1.0',
        7: 'Creative Commons Zero v1.0 Universal license',
        8: 'Eclipse Public license 2.0',
        9: 'GNU Affero General Public license v3.0',
        10: 'GNU General Public Licenc v2.0',
        11: 'GNU Lesser Public license v2.1',
        12: 'Mozilla Public license 2.0',
        13: 'The Unlicense'
    }

    options = [licenses[key] for key in licenses]
    options.append('')
    show_options = str(licenses).replace(",", "\n").replace("{", " ").strip('}')

    license = input("Choose a license: \n")
    try:
        if license in licenses.values() or license == "": return confirmLicense(show_options, license, licenses)
        elif license == "help": helpLicense(show_options, licenses)
        elif int(license) in licenses.keys(): return confirmLicense(show_options, licenses[int(license)], licenses)
        elif int(license) == 0: return confirmLicense(show_options, "", licenses)
    except ValueError: invalidLicense(show_options, licenses)


def confirmLicense(show_options, license, licenses):
    if license == "":
        confirmation = input("You are about to create your package without a license, are you sure? (y/n): ")
        if confirmation == "y": return license
        elif confirmation == "n": chooseLicense()
        else: confirmLicense(show_options, license, licenses)

    elif license == "help": helpLicense(show_options, licenses)

    else:
        confirmation = input("you are about to create your package with the '%s' license, are you sure? (y/n): " %license)
        if confirmation == "y": return license
        elif confirmation == "n": chooseLicense()
        else: confirmLicense(show_options, license, licenses)


def helpLicense(show_options, licenses):
    print("Please choose a number from the following list, corresponding to your desired license. If you dont want a license press 0")
    try: key = int(input("%s \n" %show_options))
    except ValueError: key = " "
    if key in licenses.keys():
        print("option chosen from listed licenses")
        confirmLicense(show_options, licenses[key], licenses)
    elif key == 0:
        print("chosen for no license")
        confirmLicense(show_options, "", licenses)
    else: invaLidlicense(show_options, licenses)


def invalidLicense(show_options, licenses):
    option = input("Invalid input. To view a list of all valid licenses type help \n")
    if option == "help": helpLicense(show_options, licenses)
    elif option in licenses.values(): confirmLicense(show_options, option, licenses)
    else: invalidLicense(show_options, licenses)


def commit():
    import os

    os.system('git add .')
    os.system('git commit -m "initial commit"')
    os.system('git push origin master')
    os.system('git tag v0.0.1')
    os.system('git push --tag')
