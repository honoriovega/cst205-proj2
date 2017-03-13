import * as React from 'react';
import { Socket } from './Socket';

export class Sound extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
			
        };
    }
    

    

    componentDidMount() {
    
    Socket.on('fromSpotify' ,(data) =>{
        console.log("hello from spotify");
        
    });
    }
    
     handleSubmitMusic(event) {
         
         
         var searchType = document.getElementById('SearchFor').value;
         var searchQuery = document.getElementById('SearchQuery').value;
        
        Socket.emit('Spotify' , {
            
            'searchType' : searchType, 
            'searchQuery' : searchQuery,
        });
     }
    
    
      render() {
        return (
        <div>    
            <h4> Spotify web player! </h4>
            <form onSubmit= {this.handleSubmitMusic}>
                <select id = "SearchFor">
                <option value="Artist">Artist</option>
                <option value="Track" >Track</option>
                <option value="User">User</option>
                </select>
                <input type = "text" id = "searchQuery" name="searchQuery" />
                <input type="submit" id = "submit" />
            </form>
            </div>
        );
    }
}