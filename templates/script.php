<?php
function getUserIpAddr()
{
    if(!empty($_SERVER['HTTP_CLIENT_IP'])){
        //ip from share internet
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    }elseif(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
        //ip pass from proxy
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    }else{
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}
function validate_address($address)
{
$check_pattern = '/\d+ [0-9a-zA-Z ]+/';
$has_error = !preg_match($check_pattern, $address);
return $has_error;
}
function test_input($info)
{
  $data = trim($info);
  $data = stripslashes($info);
  $data = htmlspecialchars($info);
  return $info;
}

  // $ip=$Gender=$Disease=$Disease_reply=$Blood_Pressure=$Tattoo=$Tatoo_Length=$IV=$Medication=$Pregnant=$Location=$Cancer=$Age=$STD=$BloodType=$Iron_lvl=$Travel=$TripLength=$Piercing=$Piercing_date=NULL;
  if (isset($_POST['submit']))
  {
    echo "<h1>whattheadasdasdasdasd</h1>";
    if (isset($_POST['gender'])
    {
    $Gender=test_input($_POST["gender"]);
    }
    else {
        echo "A selection is required.";
    }
    $Age = test_input($_POST['Age']);
    if(!filter_var($Age,FILTER_VALIDATE_INT) || empty($Age))
    echo "A integer is required";
     $Weight=test_input($_POST['Weight']);
     if(!filter_var($Weight,FILTER_VALIDATE_INT) || empty($Weight))
     echo "A integer is required";
     if (!isset($_POST['bloodtype']))
       echo 'A selection is required.';
     $LastDonation =  test_input($_POST['LastDonation']);
     if(!filter_var($LastDonation,FILTER_VALIDATE_INT) || empty($LastDonation))
     echo "A integer is required";
     $BloodPressure =  test_input($_POST['Bp']);
     if(!filter_var($BloodPressure,FILTER_VALIDATE_INT) || empty($BloodPressure))
     echo "A integer is required";
     $Iron =  test_input($_POST['Ir']);
     if(!filter_var($BloodPressure,FILTER_VALIDATE_INT) || empty($BloodPressure))
      echo "A integer is required";
     if (!isset($_POST['Sick']))
      echo "A selection is required.";
      else {
        $Sick=
      }
     if (!isset($_POST['Cancer']))
      echo "A selection is required.";
     if (!isset($_POST['Tattoo']))
      echo "A selection is required.";
     if (!isset($_POST['Piercing']))
      echo "A selection is required.";
      if (!isset($_POST['Medication']))
        echo "A selection is required.";
     if (!isset($_POST['IV']))
       echo "A selection is required.";
     if (!isset($_POST['STD']))
        echo "A selection is required";
     if (!isset($_POST['Pregnant']))
        echo "A selection is required.";
      if (!isset($_POST['HighRisk']))
        echo "A selection is required.";
        if (!isset($_POST['Travel']))
          echo "A selection is required.";
  }

  ?>
