import React from 'react'
import { Component } from 'react';
import { Card, Button } from 'react-bootstrap';
import Neo from './neo';


class HeaderTab extends Component {
    render() {
        return (
            <div>
              <Card className="text-center">
                <Card.Header>Neo4j</Card.Header>
                <Card.Body>
                    <Card.Title>Graph Database</Card.Title>
                    <Card.Text>
                    

                        <div>
                        <form onSubmit={this.handleSubmit}>
                        <label>
                            Choose Filter : 
                            <input type="text" name="name" onChange={this.handleChange} />
                        </label>
                        <button type="submit">Add</button>
                        </form>

                        </div>
                        <div>

                        <div>
                    <form onSubmit={this.handleSubmit}>
                    <label>
                       Delete Filter:
                        <input type="text" name="id" onChange={this.handleChange} />
                    </label>
                    <button type="submit">Delete</button>
                    </form>
                    </div>

                        </div>
                    
                 </Card.Text>
                    <Button variant="primary">Go somewhere</Button>
                </Card.Body>
                
                </Card>
                <br />
                <Card>
                    <h1>Hello World</h1>
                <Neo /> 
                <h1>Hello World</h1>
                <Card.Body>
                <Card.Text>
                  
                </Card.Text>
                </Card.Body>
            </Card>
            </div>
        )
    }
}

export default HeaderTab;


