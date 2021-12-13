<?php
  require "app/help.php";
  require "app/app.php";
  require "app/objects/languages.php";

  $origin = dirname($argv[0], 1);
  $opts = (getopt("h:p:", ["name:", "lan:"]));

  $help_needed = (array_key_exists("h", $opts) or !array_key_exists("name", $opts) or count($argv) < 2);
  if ($help_needed){
      print("help needed");
      exit();
  }
  if(!array_key_exists("lan", $opts)) $opts["lan"] = "php";


  $file = file_get_contents("$origin/config.json", "r");
  $data = json_decode($file, true);
  $app = new App($data);


  switch($opts["lan"]){
    case "py":
      new Python($app, $opts);
      break;
    case "php":
      new PHP($app, $opts);
      break;
    case "web":
      new Web($app, $opts);
      break;
  }
 ?>
