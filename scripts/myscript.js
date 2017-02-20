$( "#myButton" ).click(function() {

	sendMessage();
	
});

function sendMessage() {

	$.ajax({
		url: "sendMessage.php",
		async: true,
		cache: false,
		type:"GET",
		data: {
				msg: $("#message").val()
		
			  },
		
		success:function(data) {
		updateText(data); 
		}
		
		});
}

function updateText(message) {

	var before = document.getElementById("boxMessage").innerHTML;

	document.getElementById("boxMessage").innerHTML = before + message  + "<br>";

	var objDiv = document.getElementById("boxMessage");
	objDiv.scrollTop = objDiv.scrollHeight;

}

