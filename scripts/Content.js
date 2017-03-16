import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';
import { Chatroom } from './Chatroom';
import {Sound} from './Sound';


export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
			'messages': [],
            'numbers': [],
            'my name': 'I dont have a name yet :(',
            'all users': []
        };
    }
    

    

    componentDidMount() {

        Socket.on('all numbers', (data) => {
            this.setState({
                'numbers': data['numbers']
            });
   
        });
        
    
function tryToGreet() {
    FB.getLoginStatus((response) => {
    if (response.status == 'connected') {
        
    
        console.log("facbook user is logged in");
        Socket.emit('greet user', {
        'google_user_token': '',
        'facebook_user_token':
        response.authResponse.accessToken
        });
    } else {
    
    
    let auth = gapi.auth2.getAuthInstance();
    let user = auth.currentUser.get();
    if (user.isSignedIn()) {
    
    
    
        Socket.emit('greet user', {
        'google_user_token':
        user.getAuthResponse().id_token,
        'facebook_user_token': ''
        });
    }
    
    }
    
    });
    }        
   
        
        Socket.on('all messages', (data) => {
            this.setState({
                'messages': data['messages']
            });
            
            
            	var objDiv = document.getElementById("messageArea");
				objDiv.scrollTop = objDiv.scrollHeight;
            

        })
        
        
        Socket.on('server generated a new name', (data) => {
            console.log('Got a new name from server:', data);
            this.setState({
                'my name': data['name'],
            })
        });
        Socket.on('list of all users', (data) => {
            console.log('Got a list of all users from the server:', data);
            this.setState({
                'all users': data['users']
            })
            console.log('New state:', this.state);
        });
    }

    render() {


        

        
        let all_users = this.state['all users'].map(
			(user) => <li key={user}>{user}</li>
		);
	
		
		
        return (
            <div>
                <h1>CST 205 - Project 2</h1>
         

 <div
className="fb-login-button"
data-max-rows="1"
data-size="medium"
data-show-faces="false"
data-auto-logout-link="true">
</div>
<div>
                <div onClick={this.tryToGree}
                className="g-signin2"
                data-theme="dark">
                </div>
                <Chatroom messages={this.state.messages}/>
                
                  <div className = "spotifyContainer">
                <Sound/>
           </div>
           
            </div>
        
           </div>
        );
    }
}
