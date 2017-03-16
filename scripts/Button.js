import * as React from 'react';

import { Socket } from './Socket';
//Filename: Button.js
//authors Javar A, Honorio V. Antonio V. We all worked on this together. 
//making buttons here that deal with sending message data from the client to the server. 
export class Button extends React.Component {
        
        
        
        
        handleSubmit(event) {
        event.preventDefault();

        let random = Math.floor(Math.random() * 100);
        console.log('bruh i made a new number : ', random);
        console.log('sahhhh dude : ');
        
        // grabbing the contents of the textbox and storing them
        var referenceToMessage = document.getElementById('msg');
		var newMsg = referenceToMessage.value;
		referenceToMessage.value = "";
	

//resetting the value of the textbox.    
	document.getElementById('msg').value = " ";
	
//before sending the message, checking to see if the user is authenticated
FB.getLoginStatus((response) => {
if (response.status == 'connected') {
    
    
    var header = document.getElementById("banner");
    header.innerHTML = "";
    console.log("facbook user is logged in");
    Socket.emit('new msg', {
    'google_user_token': '',
    'facebook_user_token':
    response.authResponse.accessToken,
    'number': random,
    'msg' : newMsg

    });
      
} else {


let auth = gapi.auth2.getAuthInstance();
let user = auth.currentUser.get();
if (user.isSignedIn()) {
    console.log("google logged in");
    var header = document.getElementById("banner");
    header.innerHTML = "";

    Socket.emit('new msg', {
    'google_user_token':
    user.getAuthResponse().id_token,
    'facebook_user_token': '',
    'number': random,
    'msg': newMsg
    });
    
}
//letting the user know to sign in when attempting to send a message without being authenticated
else {
    var header = document.getElementById("banner");
    header.innerHTML = "You must be logged in to message!";
}

}

});

            console.log('Sent up the random number to server!');
        		    
}


    render() {
        return (
            <div>
            <form onSubmit={this.handleSubmit}>
            <div className ="enjoy-css">
				 <input type = "text" id = "msg" name="lname"/>
			</div>
                <button>{this.props.name}</button>
            </form>
            </div>
         
        );
    }
}