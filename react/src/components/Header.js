import React from 'react'
import { Component } from 'react';
import { Card, Button, Form, Row, Col, Container } from 'react-bootstrap';
import Neo from './neo';


class HeaderTab extends Component {
    render() {
        return (
            <div>
                <Card className="text-center">
                    
                    <Card.Body >
                        <Card.Title>Neo4j</Card.Title>
                        
                        <Card.Text>
                    <Container>
                        <Row className="text-center">
                            <Col>
                        <Col  xs={6}>
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
                                </Col>
                                </Col>
                            </Row>
                            </Container>
                        </Card.Text>
                    
                    </Card.Body>

                </Card>
                <br />
            <Container>
                <Row className="justify-content-md-center">
                    <Col>
                        <Col xs={6}>
                <Card className="text-center" style={{ width: '120rem', height: '60rem' }} >


                    <Neo />

                </Card>
                </Col>
                </Col>
                </Row>
                </Container>
            </div>
        )
    }
}

export default HeaderTab;


