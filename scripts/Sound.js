import * as React from 'react';


export class Button extends React.Component {
    
    
    
    
      render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button>Music player!</button>
            </form>
        );
    }
}