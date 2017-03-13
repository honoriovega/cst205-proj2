import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';

export class Chatroom extends React.Component {

		 handleLink(link)		
		{
			// empty string do nothing
		    if(link === '')
		    	return;
		    	
    	var len = link.length;
    	var res = link.slice(len - 3, len);
    	
    	if(res  === 'jpg' || res === 'png' || res === 'gif')
			return <img src={link} />;
		else if(link.slice(len - 4, len) == 'jpeg')
			return <img src={link} />;
		
		else if( link.slice(0, 12) === 'http://cache')
			return <img src={link} />;
		
		else if( link.includes('youtube.com')) {
			
			
    		var res = link.split("=");
			
			var ytlink = "https://www.youtube.com/embed/" + res[1];
			return <iframe width="560" height="315" src={ytlink } ></iframe>;
		}
		else
			return <a href={link} target="_blank"> {link} </a>;
		}
		
		handleName(name)
		{
		
			if(name == 'Bender_from_futurama')
				return <b>{name}</b>;
			else
				return name;
		}
	
		render() {
		
		
		
				var x = "/static/BOT.jpg";	
                 let allMessages = this.props.messages.map( (msg) =>
            <p >
            <img style={{width : 100, height: 100}}src={msg.picture} /> {this.handleName(msg.name)}: &nbsp;
            {msg.msg}
            {this.handleLink(msg.link)}
        	</p>	);
        	
			
        return (
			<div>
				<div id='messageArea' className='msgArea'>
				{allMessages}
				</div>
				<br />
				<div className='sendMessageArea'>
				<Button name='Send Message'/>
				</div>
			</div>
        );
    }
}
