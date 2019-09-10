import React from 'react'
import { Component } from 'react';
import { Card, Button } from 'react-bootstrap';
import styled from 'styled-components';



class HeaderTab extends Component {
    render() {
        return (
            <div>
              <Card className="text-center">
                <Card.Header>Neo4j</Card.Header>
                <Card.Body>
                    <Card.Title>Graph Database</Card.Title>
                    <Card.Text>
                            Check how your users are interatcing with bots
                    </Card.Text>
                    <Button variant="primary">Go somewhere</Button>
                </Card.Body>
                <Card.Footer className="text-muted">2 days ago</Card.Footer>
                </Card>
                <br />
                <Card>
                <Card.Img variant="top" src="pic1.jpg" />
                <Card.Body>
                <Card.Text>
                    You can put neo4j here
                </Card.Text>
                </Card.Body>
            </Card>
            </div>
        )
    }
}

export default HeaderTab;


