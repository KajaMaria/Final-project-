import React from 'react'
import { Component } from 'react';
import { Card, Button, Form, Row, Col, Container } from 'react-bootstrap';


class HeaderTab extends Component {
    render() {
        return (
            <div>

                <Card className="text-center " >
                    <Card.Title>Bots Map in Neo4j</Card.Title>
                </Card>
                <Container>
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group controlId="formBasic">
                        <Form.Label>Choose Filter : </Form.Label>
                        <Form.Control type="text" placeholder="Filter" type="text" name="name" onChange={this.handleChange} />
                        <Form.Text className="text-muted">
                            You can choose from 6 filters.
                    </Form.Text>
                </Form.Group>
                <Form.Group controlId="formBasicDelete">
                    <Form.Label>Delete Filter : </Form.Label>
                    <Form.Control type="text" placeholder="Remove" type="text" name="name" onChange={this.handleChange} />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
            </Container>
            </div>
        )
    }
}

export default HeaderTab;


