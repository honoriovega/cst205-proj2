<?php include 'functions.php'; ?>

<html>
    <head>
        <link href="images/favicon.ico" rel="icon" type="image/x-icon" />
        <link rel="stylesheet" href="css/styles.css">

     </head>
    <body>
        <div class='header'>  <center><h1>Project 2 - Meme Chatroom</h1></center>
</div>
        <div class='users'><h3>User List</h3>

		<?php generateFakeUsers(); ?>

        </div>
        <div class='box' id='boxMessage'>

           <?php generateFakeMessage(); ?>

        </div>
  <div class='messageBox'> <input type="text" id="message" name="message" value="Enter message">
		<button id="myButton">Send message</button></div>
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
	<script src="scripts/myscript.js"></script>



    </body>
</html>
