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
                <option value="Artist" id="term">Artist</option>
                <option value="Track" id="term">Track</option>
                <option value="User" id = "term" >User</option>
                </select>
                <input type = "text" id = "searchQuery" name="searchQuery" />
                <button>Search Music on Spotify!</button>
            </form>
        );
    }
}