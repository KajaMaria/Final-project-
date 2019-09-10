import React from 'react';
import { Row, Column } from 'react';
import './App.css';
import Main from './components/main';
import Neo from './components/neo';
import HeaderTab from './components/Header';
import NavigationBar from './components/Navigation';
import FooterBar from './components/Footer';
import Layout from './components/Layout';

class App extends React.Component { 
  
  render() {
  //   this.state = {
  //     mainContent: 0,
  //   }

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
       
           <div style={{height: '100vh', position: 'relative'}}>
        <Row>
          <HeaderTab />
        </Row>
        <Row>
          <Column>
            <NavigationBar />
          </Column>
          <Column>
            display
          </Column>
        </Row>
        <Row>
          <Layout />
        </Row>
        <Row>
          <FooterBar />
        </Row>
        </div>
      
      

    
   

    );
  }
}

export default App;
