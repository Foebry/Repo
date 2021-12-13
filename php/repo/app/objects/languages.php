<?php
  include "packages";
  include "repositories";


  class mainLanguage{
    public function __construct($app, $opts){
      $this->repo = new Repository($opts);
    }

    public function devBranch(){
      exec("git chechout -b develop");
      exec("git add *");
      exec("git push --set-upstream origin develop");
    }
  }


  class PHP extends mainLanguage{
    public function __construct($app, $opts){
      parent::__construct($app, $opts);
      parent::$repo->initPHP();
      parent::$app::$git->commit(this->repo);
      parent::devBranch();
    }
  }



  class Python extends mainLanguage{
    public function __construct($app, $opts){
      parent::__construct($app, $opts);
      $this->repo->createSetup($app);
      $this->package = new Package($this->repo, $app);
      $this->app->git->commit($this->repo);
      $this->devBranch();
    }
  }



  class Web extends mainLanguage{
    public function __construct($app, $opts){
      parent::__construct($app, $opts);
      $this->repo->initWeb();
      $this->app->git->commit($this->repo);
      $this->devBranch();
    }
  }

 ?>
