<?php


  class API{
    function __construct($data){
      $this -> user = new User($data);
      $this->user.authenticate($data["CREDENTIALS"]["GITHUB_TOKEN"]);
    }

    function postRepository($data){

      $url = "https://api.github.com/user/repos";

      $curl = curl_init($url);
      curl_setopt($curl, CURLOPT_URL, $url);
      curl_setopt($curl, CURLOPT_POST, true);
      curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

      $headers = array(
          "Authorization: Bearer $this->user->token",
          "Content-Type: application/json",
          "user-agent: testing",
      );
      curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

      $data = <<<DATA
  {
    "name": "$object->name",
    "private": $object->private
  }
  DATA;

      curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
      $resp = curl_exec($curl);
      curl_close($curl);
      return($resp);
    }
  }

 ?>
