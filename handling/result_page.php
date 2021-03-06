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
    $id = $_SESSION['id'];
    $sql = "SELECT * FROM requests WHERE request_id = '$id'";
    $result = $mysqli->query($sql);
    # $sql = "DELETE from requests WHERE request_id = '$id'";
    # $mysqli->query($sql);
    $mysqli->close(); 
?>



<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">

        <title>NJCAT | Results</title>

        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">


        <!-- Shared site-wide CSS  -->
        <link rel="stylesheet" href="../styles/main.css">
        <link rel="stylesheet" href="../styles/tab.css">
        <link rel="stylesheet" href="../styles/icons.css">
        <link rel="stylesheet" href="../styles/tools.css">
        <link rel="stylesheet" href="../styles/result_page.css">

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
                            <img src="../images/njccic.png">
                        </a>
                    </div>
                </div>
                <div class="nav-title">
                    <a href="../tools/overview.html">
                        <h5 id="move">NJCCIC Cyber Analyst Toolkit<h5>
                    </a>
                 </div>
            </nav>
        </header>

	<div class="tab">
	    <button class="tablinks" onclick="location.href='../tools/overview.html'">overview <img src="../images/overview.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='../tools/whois.html'">whois <img src="../images/whois.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='../tools/nslookup.html'">nslookup <img src="../images/website.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='../tools/geolocation.html'">geolocation <img src="../images/geolocation.png" width="20" height="20"></button>
            <button class="tablinks" onclick="location.href='../tools/contact.html'">contact <img src="../images/contact.png" width="20" height="20"></button>
          </div>

        <div class="result_page">
            <h5 id="page_title"><b>Search Results</b></h5>

            <div class="results">
                <!-- TABLE CONSTRUCTION-->
                <table>
                    <tr>
                        <th>IP Address</th>
                        <th>Results</th>
                    </tr>
                    <!-- PHP CODE TO FETCH DATA FROM ROWS-->
                <?php   // LOOP TILL END OF DATA 
                        $addr_arr = [];
                        $result_arr = [];
                        $final_arr = [];
                        $counter = 0;
                        $type = '';

                        while($rows=$result->fetch_assoc())
                        {
                            $type = $rows['input_type'];
                            if($type == 'single')
                            {
                ?>
                            <tr>
                                <!--FETCHING DATA FROM EACH 
                                    ROW OF EVERY COLUMN-->
                                <td><?php echo $rows['address'];?></td>
                                <td><?php echo trim($rows['result'], "; ");?></td>
                            </tr>
                <?php
                            }
                            elseif($type == 'file')
                            {
                                $address = trim($rows['address']);
                                $table_results = trim($rows['result']);                                
                                $arr = array($address, $table_results);
                                array_push($final_arr, $arr);
                    ?>

                    <?php
                            }
                        }
                        
                        if($type == 'file') {
                            $_SESSION['final_arr'] = $final_arr;

                    ?>
                            <tr>
                                <td>File</td>
                                <td>
                                    <form action="download.php" method="post">
                                    <label for="filename">Name Download:</label><br>
                                    <input type="text" id="filename" name="filename">
                                    <input type="submit" name="submit" value="Download File" />
                                    </form>
                                </td>
                            </tr>
                    <?php
                        }
                    ?>

                </table>
            </div>
        </div>
    </body>
</html>


