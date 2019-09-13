import React from 'react'
import { Component } from 'react';
import { Card, Button, Form, Row, Col, Container } from 'react-bootstrap';

class HeaderTab extends Component {
    render() {
        return (
            <div className ="head">


            
<Container >
    <h2>Check Users</h2>
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
<p><a href="https://github.com/BenjaminDarking/project_pry"> Get involved in our Open Source API </a></p>
</Container>

            </div>
        )
    }
}

export default HeaderTab;


