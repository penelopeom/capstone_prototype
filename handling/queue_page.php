<?php
session_start();
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
$id = $_SESSION['id'];
$sql = "SELECT * FROM requests WHERE request_id = '$id'";
$result = $mysqli->query($sql);
if ($result->num_rows == 0) {
  header("Location: /error_page.html");
}
$mysqli->close(); 
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <script>
            window.setInterval('refresh()', 9700);     
            // Call a function every 10000 milliseconds 
            // (OR 10 seconds).

            // Refresh or reload page.
            function refresh() {
                window.location.reload();
            }
        </script>

        <meta charset="UTF-8">

        <title>NJCAT | In Queue...</title>

        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">


        <!-- Shared site-wide CSS  -->
        <link rel="stylesheet" href="/styles/main.css">
        <link rel="stylesheet" href="/styles/tab.css">
        <link rel="stylesheet" href="/styles/icons.css">
        <link rel="stylesheet" href="/styles/tools.css">
        <link rel="stylesheet" href="/styles/result_page.css">
        <link rel="stylesheet" href="/styles/queue_page.css">

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
            <button class="tablinks" onclick="location.href='/tools/nslookup.html'">nslookup <img src="/images/website.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='/tools/geolocation.html'">geolocation <img src="/images/geolocation.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='/tools/socials.html'">socials <img src="/images/socials.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='/tools/contact.html'">contact <img src="/images/contact.png" width="20" height="20"></button>
          </div>

        <div class="result_page">
            <h5 id="page_title"><b>In Queue...</b></h5>

            <div class="results">
                <!-- TABLE CONSTRUCTION-->
                <?php 
                    $finished = True;
                    while($rows=$result->fetch_assoc()) {
                        if($rows['result'] == "") {
                            echo "<h2>Request is in the Queue.</h2>";
                            $finished = False;
                            break;
                        }
                        elseif($rows['result'] == "PENDING") {
                            echo "<h2>Request is currently Pending.</h2>";
                            $finished = False;
                            break;
                        }
                        
                    }
                    
                    if ($finished) {
                        header("Location: /handling/result_page.php");
                    }
                ?>
                <table>
                    <br>
                    <td style="text-align: center;">
                        <div class="timer">
                            <img src="/images/bar.gif" width="200" height="150">
                        </div>
                    </td>
                </table>
            </div>
        </div>
    </body>
</html>
