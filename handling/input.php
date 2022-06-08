<!DOCTYPE html>
<html>
  
<head>
    <title>Insert Page page</title>
</head>
  
<body>
    <center>
        <?php
  
        session_start();
        $user = 'root';
        $password = 'dapos&e7efE_rU@uphi#'; 
        $database = 'njccic_capstone'; 
        $servername='127.0.0.1';
        // servername => localhost
        // username => root
        // password => empty
        // database name => staff
        $conn = mysqli_connect($servername, $user, $password, $database);
          
        // Check connection
        if($conn === false){
            die("ERROR: Could not connect. " 
                . mysqli_connect_error());
        }
          
        // Taking ip from the form data(input) and request type
        $ip =  $_REQUEST['address'];
        $request_type = $_REQUEST['request_type'];;
          
        // Performing insert query execution
        $id = uniqid();
        $_SESSION['id'] = $id;
        $sql = "INSERT INTO requests (request_id, request_type, address, result, input_type) VALUES ('$id','$request_type', '$ip', '', 'single')";
          
        if(mysqli_query($conn, $sql)){
            echo "<h3>data stored in a database successfully." 
                . " Please browse your localhost phpMyAdmin" 
                . " to view the updated data</h3>"; 
  
            echo nl2br("\n$request_type\n$ip");
        } else{
            echo "ERROR: Hush! Sorry $sql. " 
                . mysqli_error($conn);
        }

        // Close connection
	mysqli_close($conn);

        header("Location: /capstone_prototype/handling/queue_page.php");
        ?>
    </center>
</body>
  
</html>
