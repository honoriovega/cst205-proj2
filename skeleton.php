<html>
    <head>
        <link href="images/favicon.ico" rel="icon" type="image/x-icon" />
        <link rel="stylesheet" href="css/styles.css">
        <style>
			#userPicture
			{
				width:25px;
				height:25px;
				
				display:inline-block;
			}
        </style>
     </head>
    <body>
        <div class='header'>        <center><h1>Project 2 - Meme Chatroom</h1></center>
</div>    
        <div class='users'><h3>User List</h3>
        
        <?php
			for($i = 0; $i < rand(10,15); $i++)
				echo  divColor() . "random_user" . rand(1,100) . "<br>";
        ?>
        </div>
        <div class='box'>
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
           
				for($i = 0; $i < rand(10,100); $i++)
				{
					echo "<h4 style='display:inline-block;'>Message" .($i + 1) . " </h4> " . divColor() . ": " . randomWord() . "<br>";
				}
           ?>
         
        </div>
  <div class='messageBox'> <input type="text" id="message" name="message" value="Enter message">
		<button onclick="doThis()">Send message</button></div>
		
	<script>
		function doThis()
		{
			var text = document.getElementById("message").value;
			
			var message = 'You tried to send the following message:  "' + text + '"';
			
			alert(message);
		}
	</script>
    </body>
</html>
