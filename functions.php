<?php
function randomWord()
{
	$str = array("hello there","welcome !", "how is everyone",
				"how is the weather","cool", "random phrase",
				"who voted for trump?","hello from CSUMB");

	$size = count($str) - 1;


	return $str[rand(0,$size)];
}

function randomColor() {
	$values = array('A','B','C','D','E','F','0','1','2','3','5','6','7','8','9');

	$temp = "#";

	$size = count($values) - 1;
	for($i = 0; $i < 6; $i++)
		$temp .= $values[rand(0,$size)];

	return $temp;

}

function divColor()
{
	return "<div id='userPicture' style='background-color:" . randomColor(). ";'></div>";
}


function generateFakeUsers()
{
	for($i = 0; $i < rand(10,100); $i++)
		echo  divColor() . "random_user" . rand(1,100) . "<br>";
}


function generateFakeMessage()
{

	for($i = 0; $i < rand(10,100); $i++)

	{
		echo "<h4 style='display:inline-block;'>Message" .($i + 1) .
				" </h4> " . divColor() . ": " . randomWord() . "<br>";
	}

}

?>
