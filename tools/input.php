<!DOCTYPE html>
<html>
  
<head>
    <title>Insert Page page</title>
</head>
  
<body>
    <center>
        <?php
  

        $user = 'njccic_usr';
        $password = 'iJdf56*kf'; 
        $database = 'njccic_capstone'; 
        $servername='soccerdb.calingaiy4id.us-east-2.rds.amazonaws.com';
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
        $request_type = "whois";
          
        // Performing insert query execution
        $sql = "INSERT INTO requests (request_type, address, result) VALUES ('$request_type', '$ip', '')";
          
        if(mysqli_query($conn, $sql)){
            echo "<h3>data stored in a database successfully." 
                . " Please browse your localhost php my admin" 
                . " to view the updated data</h3>"; 
  
            echo nl2br("\n$request_type\n$ip");
        } else{
            echo "ERROR: Hush! Sorry $sql. " 
                . mysqli_error($conn);
        }

        // Close connection
        mysqli_close($conn);
        header("Location: /result_page.php");
        ?>
    </center>
</body>
  
</html>