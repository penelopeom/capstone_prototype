<!DOCTYPE html>
<html>
  
<head>
    <title>File Input Page</title>
</head>
  
<body>
    <center>
        <?php
  
        session_start();
        $user = 'root';
        $password = 'dapos&e7efE_rU@uphi#'; 
        $database = 'njccic_capstone'; 
        $servername='127.0.0.1';
        
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
            mysqli_query($conn, $sql);
        }

        // Close connection
        mysqli_close($conn);
        header("Location: ../handling/queue_page.php");
        ?>
    </center>
</body>
  
</html>
