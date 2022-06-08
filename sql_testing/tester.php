<?php
    session_start();
    $user = 'root';
    $password = 'dapos&e7efE_rU@uphi#'; 

    $database = 'njccic_capstone'; 
    
    $servername='127.0.0.1';
    $mysqli = new mysqli($servername, $user, 
                    $password, $database);
    
    // Checking for connections
    if ($mysqli->connect_error) {
        die('Connect Error (' . 
        $mysqli->connect_errno . ') '. 
        $mysqli->connect_error);
    }
    
    // SQL query to select data from database
    $sql = "SELECT * FROM requests";
    $result = $mysqli->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>

    <body>
        <?php
            while($rows=$result->fetch_assoc()) {
                $type = $rows['input_type'];
                
        ?>
        
        <tr>
        <!--FETCHING DATA FROM EACH 
        ROW OF EVERY COLUMN-->
        <td><?php echo $rows['address'];?></td>
        <td><?php echo trim($rows['result'], "; ");?></td>
        
        </tr>
        <?php
            }
        ?>
</html>