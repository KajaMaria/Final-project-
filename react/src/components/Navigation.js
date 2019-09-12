import React, { Component } from 'react';
import { NavDropdown, Navbar, Button, Form, FormControl } from 'react-bootstrap';
import styled from 'styled-components';

export class NavigationBar extends Component {
    render() {
        const Styles = styled.div`
            .navbar {
                background-color: #222;
            }
        
            .navbar-brand, .navbar-nav .nav-link {
                color: #bbb;
        
                &:hover {
                    color: white;
                }
            }
        `;
        return (
        
         <Styles>
                <Navbar bg="light" expand="lg" className="navbar">
                    <Navbar.Brand href= "/">Botter</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                    <NavDropdown title="Go Fish" id="basic-nav-dropdown">
                      
                      {/* <a href="#" onClick={setloadedFalse()}>Frequency</a> */}
                      <NavDropdown.Item href="#">Tweets to Age Ratio</NavDropdown.Item>
                      <NavDropdown.Item href="#">Hours of Activity per day</NavDropdown.Item>
                            
                      <NavDropdown.Item href="#">After Scoring Criteria</NavDropdown.Item>
                            
                      <NavDropdown.Item href="#">Frequency Weight</NavDropdown.Item>
                    <NavDropdown.Item href="#">Tweets to Age Ratio Weight</NavDropdown.Item>
                    <NavDropdown.Item href="#">Hours of Activity per day Weight</NavDropdown.Item>
                            
                    <NavDropdown.Item href="#">Choose search start point</NavDropdown.Item>
                    <NavDropdown.Item href="#">Bot Graveyard</NavDropdown.Item>
                       </NavDropdown>
                    </Navbar.Collapse>

                    <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button variant="outline-primary">Search</Button>
                    </Form>
                </Navbar>
            </Styles>
        )
  
    }
}

export default NavigationBar