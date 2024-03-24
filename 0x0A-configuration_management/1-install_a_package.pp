#install flask version (2.1.0) of flask using pip

  package {'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }


  package {'python3-pip':
    ensure   => installed,
  }

