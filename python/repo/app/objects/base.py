## everything to do with creation of a base folder for the web languages.
import os
import easygui
import json

from app.help import helpSection


def createBaseFolder(app):
    print("please select the location where you would like to store you reference base folder")
    print("If you need help, cancel...")
    folder = easygui.diropenbox()

    if folder is None:
        print(helpSection("## --lan web", "##"))
        createBaseFolder(app)

    os.chdir(folder)
    new_folder = os.path.join(folder, "base")
    os.system(f"mkdir {new_folder}")
    os.chdir(new_folder)
    os.system("cd .> _reset.scss")
    os.system("cd .> _extends.scss")
    os.system("cd .> _fonts.scss")
    os.system("cd .> _mixins.scss")
    os.system("cd .> _variables.scss")
    saveBaseFolder(app, new_folder)
    return new_folder


def findBaseFolder(app):
    print("Please select the correct location of your base folder, cancel to create a new base folder")
    folder = easygui.diropenbox()
    if folder is None:
        print("No base folder selected, creating new base folder")
        return createBaseFolder(app)
    saveBaseFolder(app, folder)
    return folder


def saveBaseFolder(app, new_folder):
    new_folder = new_folder.replace("\\", "//")
    with open(os.path.join(app.root, "config.json"), "r") as file:
        lines = file.readlines()
    new_lines = []
    for line in lines:
        if "WEB_BASE_FOLDER" in line:
            pos = line.find(":")
            line = line.replace(line[pos:], f':"{new_folder}",')
        new_lines.append(line)
    text = "".join(new_lines)

    with open(os.path.join(app.root, "config.json"), "w") as file:
        config = json.loads(text)
        json.dump(config, file, indent=4)
