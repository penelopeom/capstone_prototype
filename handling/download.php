<?php
    include 'result_page.php';
    $filename = $_REQUEST['filename'] . '.csv';
    ob_clean();
    ob_start();
    header('Content-Type: text/csv');
    header("Content-Disposition: attachment; filename=$filename");
    header('Pragma: no-cache');
    header('Expires: 0');

    $fp = fopen('php://output', 'w');

    foreach ($final_arr as $fields) {
        fputcsv($fp, $fields);
    }

    readfile($filename);
?>