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

    license = input("Choose a license (type help for a list of licences): \n")
    try:
        if license in licenses.values() or license == "": return confirmLicense(show_options, license, licenses)
        elif license == "help": helpLicense(show_options, licenses)
        elif int(license) in licenses.keys(): return confirmLicense(show_options, licenses[int(license)], licenses)
        elif int(license) == 0: return confirmLicense(show_options, "", licenses)
    except ValueError: invalidLicense(show_options, licenses)

    if license is None: license = " "

    return license


def confirmLicense(show_options, license, licenses):
    if license == "":
        confirmation = input("You are about to create your repository without a license, are you sure? (y/n): ")
        if confirmation == "y": return license
        elif confirmation == "n": chooseLicense()
        else: confirmLicense(show_options, license, licenses)

    elif license == "help": helpLicense(show_options, licenses)

    else:
        confirmation = input("you are about to create your repository with the '%s' license, are you sure? (y/n): " %license)
        if confirmation == "y": return license
        elif confirmation == "n": chooseLicense()
        else: confirmLicense(show_options, license, licenses)


def helpLicense(show_options, licenses):
    print("Please choose a number from the following list, corresponding to your desired license. If you dont want a license press 0")
    try: key = int(input("%s \n" %show_options))
    except ValueError: key = " "
    if key in licenses.keys():
        confirmLicense(show_options, licenses[key], licenses)
    elif key == 0:
        confirmLicense(show_options, "", licenses)
    else: invalidLicense(show_options, licenses)


def invalidLicense(show_options, licenses):
    option = input("Invalid input. To view a list of all valid licenses type help \n")
    if option == "help": helpLicense(show_options, licenses)
    elif option in licenses.values(): confirmLicense(show_options, option, licenses)
    else: invalidLicense(show_options, licenses)
