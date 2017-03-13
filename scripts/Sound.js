import * as React from 'react';
import { Socket } from './Socket';

export class Sound extends React.Component {
    
     handleSubmitMusic(event) {
         
         console.log("Type of search :" + document.getElementById('SearchFor'));
      
      
         
     }
    
    
      render() {
        return (
            <form onSubmit={this.handleSubmitMusic}>
                <select id = "SearchFor">
                <option value="Artist">Artist</option>
                <option value="Track">Track</option>
                <option value="User">User</option>
                </select>
                <input type = "text" id = "searchQuery" name="searchQuery" />
                <button>Search Music on Spotify!</button>
            </form>
        );
    }
}