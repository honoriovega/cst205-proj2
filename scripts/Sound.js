import * as React from 'react';
import { Socket } from './Socket';

export class Sound extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            track : " "
        };
    }
    componentDidMount() {
    Socket.on('fromSpotify' ,(data) =>{
        this.setState({
            'track' : data 
            });
        document.getElementById("Spotifyframe").style.visibility ="visible";
    });
    }
     handleSubmitMusic(event) {
         event.preventDefault();
         var searchType = document.getElementById('SearchFor').value;
         var searchQuery = document.getElementById('searchQuery').value;
        Socket.emit('Spotify' , {
            'searchType' : searchType, 
            'searchQuery' : searchQuery,
        });
     }
      render() {
        return (
        <div>    
        <div>
        <br />
        <h4> Group music player </h4>
         <iframe id ="Spotifyframe" src={this.state.track}  frameborder="0" allowtransparency="true"></iframe>
         </div>
         <div className = "spotifyinput">
            <form onSubmit={this.handleSubmitMusic}>
                <select id = "SearchFor">
                <option value="Track" >Track</option>
                </select>
                <div className = "spotifyinput">
                <input type = "text" id = "searchQuery" name="searchQuery" />
                <input type="submit" id = "submit" />
                </div>
            </form>
            </div>
            <div>
            </div>
            </div>
        );
    }
}