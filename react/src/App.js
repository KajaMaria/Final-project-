import React from 'react';
import { Component } from 'react';
import './App.css';
import Main from './components/main';
import Neo from './components/neo';
import HeaderTab from './components/Header';
import NavigationBar from './components/Navigation';
import FooterBar from './components/Footer';
import Layout from './components/Layout';

import { Container, Col, Row } from 'react-bootstrap';

class App extends Component {
  render() {


   this.state = {
    mainContent: 0,
  }

  // const display = {
  //   if (this.state.mainContent == 0) {
  //     display = <PleaseChooseanOption />;
  //   } else if (this.state.mainContent == 1 ) {
  //     display = <ShowGraph />;
  //   } else {
  //     display = <Loading />;
  //   }
  // }

    return (
      
      <div style={{ height: '100vh', position: 'relative' }}>
        
      <Row>
        <Col>
        <NavigationBar />
        </Col>
        </Row>
            
        <Row>
         <Col>
          <HeaderTab />
          </Col>
        </Row>
        
            {/* display */}
        
           
      <Row>
        <Col>
          <Layout />

        
          </Col>
        </Row>

        <Row>
        <Col>
          <FooterBar />
          </Col>
        </Row>

      </div>
    );
  }
}

export default App;
