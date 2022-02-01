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
        <meta charset="UTF-8">

        <title>NJCAT | Contact</title>

        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">


        <!-- Shared site-wide CSS  -->
        <link rel="stylesheet" href="/styles/main.css">
        <link rel="stylesheet" href="/styles/tab.css">
        <link rel="stylesheet" href="/styles/icons.css">
        <link rel="stylesheet" href="/styles/tools.css">
        <link rel="stylesheet" href="/styles/result_page.css">

        <!-- Icons -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

        <!-- Page specific CSS -->
    </head>
    <body style="background-color: #e7f1f8;">
        <header>
            <nav>
                <div class="nav-title">
                    <div class="padding">
                        <a href="https://www.cyber.nj.gov/">
                            <img src="/images/njccic.png">
                        </a>
                    </div>
                </div>
                <div class="nav-title">
                    <a href="overview.html">
                        <h5 id="move">NJCCIC Cyber Analyst Toolkit<h5>
                    </a>
                 </div>
            </nav>
        </header>

        <div class="tab">
            <button class="tablinks" onclick="location.href='/tools/whois.html'">whois <img src="/images/whois.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='/tools/geolocation.html'">geolocation <img src="/images/geolocation.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='/tools/socials.html'">socials <img src="/images/socials.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='/tools/contact.html'">contact <img src="/images/contact.png" width="20" height="20"></button>
          </div>

        <div class="result_page">
            <h5 id="page_title"><b>Search Results</b></h5>

            <div class="buttons">
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
            </div>
        </div>
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