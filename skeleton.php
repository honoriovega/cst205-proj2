<html>
    <head>
        <link href="images/favicon.ico" rel="icon" type="image/x-icon" />
        <link rel="stylesheet" href="css/styles.css">
     </head>
    <body>
        <div class='header'>        <center><h1>Project 2 - Meme Chatroom</h1></center>
</div>    
        <div class='users'><h3>User List</h3>
        
        <?php
			for($i = 0; $i < rand(10,15); $i++)
				echo "random_user" . rand(1,100) . "<br>";
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
           
				for($i = 0; $i < rand(20,25); $i++)
				{
					echo "Message " . ($i + 1) . ": " . randomWord() . "<br>";
				}
           ?>
           <div class='messageBox'><p>Enter message</p></div>
        </div>

    </body>
</html>
