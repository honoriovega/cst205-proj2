import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
        
        
        
        
        handleSubmit(event) {
        event.preventDefault();

        let random = Math.floor(Math.random() * 100);
        console.log('bruh i made a new number : ', random);
        console.log('sahhhh dude : ');

		var newMsg = document.getElementById('msg').value;
		console.log("tried to send ", newMsg);

        console.log("messag is " + newMsg);
        document.getElementById('msg').val = "";

console.log('Generated a random number: ', random);
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
            <form onSubmit={this.handleSubmit}>
				 <input type="text" id='msg' name="lname" /><br />
                <button>{this.props.name}</button>
            </form>
        );
    }
}