<?php
  
$user = 'njccic_usr';
$password = 'iJdf56*kf'; 

$database = 'njccic_capstone'; 
  
$servername='soccerdb.calingaiy4id.us-east-2.rds.amazonaws.com';
$mysqli = new mysqli($servername, $user, 
                $password, $database);
  
// Checking for connections
if ($mysqli->connect_error) {
    die('Connect Error (' . 
    $mysqli->connect_errno . ') '. 
    $mysqli->connect_error);
}
  
// SQL query to select data from database
$sql = "SELECT * FROM requests ORDER BY request_id DESC ";
$result = $mysqli->query($sql);
$mysqli->close(); 
?>

<!DOCTYPE html>
<html lang="en">
    <head>
    <link rel="stylesheet" href="/styles/result_page.css">
    </head>
    <body>
        <section>
            <h1>Search Results</h1>
            <!-- TABLE CONSTRUCTION-->
            <table>
                <tr>
                    <th>IP Address</th>
                    <th>Owner, Street Address</th>
                </tr>
                <!-- PHP CODE TO FETCH DATA FROM ROWS-->
                <?php   // LOOP TILL END OF DATA 
                    while($rows=$result->fetch_assoc())
                    {
                ?>
                <tr>
                    <!--FETCHING DATA FROM EACH 
                        ROW OF EVERY COLUMN-->
                    <td><?php echo $rows['address'];?></td>
                    <td><?php echo $rows['result'];?></td>
                </tr>
                <?php
                    }
                ?>
            </table>
        </section>
    </body>

</html>

<script>
    window.setInterval('refresh()', 10000);     
    // Call a function every 10000 milliseconds 
    // (OR 10 seconds).

    // Refresh or reload page.
    function refresh() {
        window .location.reload();
    }
</script>