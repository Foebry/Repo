from app.help import helpSpecificLicense


def chooseLicense(app):
    licenses = app.api.getLicenses()

    license = input("Choose a license (type help for a list of licences): \n")
    try:
        if license == "help":
            return helpLicense(licenses, app)
        elif license == "" or (int(license) >= 0 and int(license) <= len(licenses)):
            return confirmLicense(license, licenses, app)
    except ValueError:
        return invalidLicense(licenses, app)


def confirmLicense(license, licenses, app):
    if license == "":
        confirmation = input("You are about to create your repository without a license, are you sure? (y/n): ")
        if confirmation == "y":
            return -1
        elif confirmation == "n":
            return chooseLicense(app)
        else:
            return confirmLicense(license, licenses, app)

    elif license == "help":
        return helpLicense(licenses, app)

    else:
        confirmation = input(
            "you are about to create your repository with the '%s' license, are you sure? (y/n): "
            % licenses[int(license)]["name"]
        ).lower()
        if confirmation == "y":
            return int(license)
        elif confirmation == "n":
            return chooseLicense(app)
        else:
            return confirmLicense(license, licenses, app)


def helpLicense(licenses, app):
    print("--------------------------------------------------------------------------------")
    for license in licenses:
        print(f"{licenses.index(license)}: {license['name']}")
    print(
        """
-----------------------------------------------------------------------------------------
Please choose a number from the following list, corresponding to your desired license.
If you dont want a license press enter.
If you need more help type help-{number} for extra info on a specific license.\n"""
    )
    key = input()
    if "help" in key:
        if helpSpecificLicense(app, key, licenses) == False:
            return helpLicense(licenses, app)

    elif key == "":
        return confirmLicense(key, licenses, app)

    try:
        key = int(key)
        if key > len(licenses) - 1:
            return helpLicense(licenses, app)
        elif 0 <= key <= len(licenses) - 1:
            return confirmLicense(key, licenses, app)
    except ValueError:
        print("please select a license from the list")
        return chooseLicense(app)


def invalidLicense(licenses, app):
    option = input("Invalid input. To view a list of all valid licenses type help \n")
    if option == "help":
        return helpLicense(licenses, app)
    elif option in range(len(licenses)):
        return confirmLicense(option, licenses, app)
    else:
        return invalidLicense(licenses, app)
