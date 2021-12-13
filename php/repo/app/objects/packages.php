<?php

from datetime import datetime as dt


class Package{

    public function __construct($repo, $app, $git){
        $this->name = $repo->name;
        $this->path = realpath($repo->path.$this->name);
        exec("mkdir $this->path");
        chdir($this->path);
        exec("cd .> __init__.py");
        exec("cd .> main.py")
        $this->createVersion($git, $app);
      }


    private function createVersion($git, $app){
        $content = <<<EOD
__title__ = $git->$data->name
__description__ = $git->data->description
__version__ = '0.0.1'
__author__ = $app->profile
__author_email__ = $app->email
__copyright__ = 'Copyright %s %s'
""" %(git.data["name"].lower(), git.data["description"], app.profile, app.email, dt.now().year, app.name)

        file = open("__version__.py", 'w')
        file.write(content)
        file.close

        os.system("cd . > config.json")
        os.system("cd .> config_ex.json")
        EOD;
      }
    }

 ?>
