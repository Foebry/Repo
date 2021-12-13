<?php

  include "api.php";

  class App{
    public function __construct($data){
      $this->email = $data["INFO"]["EMAIL"];
      $this->name = $data["INFO"]["NAME"];
      $this->security = $data["APP"]["security"];
      $this->git = new Git($data["APP"]["CREDENTIALS"]);
    }
  }

 ?>
