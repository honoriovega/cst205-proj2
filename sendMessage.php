<?php


include 'functions.php';


$msg = $_GET["msg"];


echo "<h4 style='display:inline-block;'>Message" .rand(1,100) . 
				" </h4> " . divColor() . ": " . $msg. "<br>";


?>
