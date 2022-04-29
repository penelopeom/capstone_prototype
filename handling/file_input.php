<!DOCTYPE html>
<html>
  
<head>
    <title>File Input Page</title>
</head>
  
<body>
    <center>
        <?php
  
        session_start();
        $user = 'njccic_usr';
        $password = 'iJdf56*kf'; 
        $database = 'njccic_capstone'; 
        $servername='soccerdb.calingaiy4id.us-east-2.rds.amazonaws.com';
        
        $conn = mysqli_connect($servername, $user, $password, $database);
          
        // Check connection
        if($conn === false){
            die("ERROR: Could not connect. " 
                . mysqli_connect_error());
        }
          
        // Taking txt file of IP addresses from the form data(input) and request type
        $input =  $_FILES['myfile']['tmp_name'];
        // $ip = file_get_contents($input);

        $fp = @fopen($input, 'r'); 
        // Add each line to an array
        if ($fp) {
            $array = explode("\n", fread($fp, filesize($input)));
        }

        $request_type = $_REQUEST['request_type'];
          
        // Performing insert query execution
        $id = uniqid();
        $_SESSION['id'] = $id;

        foreach($array as $ip) {
            $ip = trim($ip);
            $sql = "INSERT INTO requests (request_id, request_type, address, result, input_type) VALUES ('$id','$request_type', '$ip', '', 'file')";
            
            if(mysqli_query($conn, $sql)){
                echo "<h3>data stored in a database successfully." 
                    . " Please browse your localhost php my admin" 
                    . " to view the updated data</h3>"; 
    
                echo nl2br("\n$request_type\n$ip");
            } else{
                echo "ERROR: Hush! Sorry $sql. " 
                    . mysqli_error($conn);
            }
        }

        // Close connection
        mysqli_close($conn);
        header("Location: /handling/queue_page.php");
        ?>
    </center>
</body>
  
</html>