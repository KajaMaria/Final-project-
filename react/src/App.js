import React from 'react';
import { Component } from 'react';
import './App.css';
import Main from './components/main';
import axios from 'axios';
import HeaderTab from './components/Header';
import NavigationBar from './components/Navigation';
import FooterBar from './components/Footer';
import Layout from './components/Layout';
import LoadingBar from './components/Loading';
import { Container, Col, Row, Navbar } from 'react-bootstrap';
import Neo from './components/neo';

class App extends Component {

  state = {
    persons: [],
    name: '',
    id: '',
  }

  componentDidMount() {
    axios.get(`https://jsonplaceholder.typicode.com/users`)
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleDeleteChange = event => {
    this.setState({ id: event.target.value });
  }


  handleDeleteSubmit = event => {
    event.preventDefault();

    axios.delete(`https://jsonplaceholder.typicode.com/users/${this.state.id}`)
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }



  handleSubmit = event => {
    event.preventDefault();

    const user = {
      name: this.state.name
    };

    axios.post(`https://jsonplaceholder.typicode.com/users`, { user })
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }


  
  render() {


  //  this.state = {
  //   mainContent: 0,
  // }

  
    // if (this.state.mainContent == 0) {
    //   let display = <PleaseChooseanOption />;
    // } else if (this.state.mainContent == 1 ) {
    //   let display = <Neo />;
    // } else {
    //   let display = <LoadingBar />;
    // }
  

    return (
      <div style={{ height: '100vh', position: 'relative' }}>
        <NavigationBar />
        <Row className="main-content">
          <Neo />
        </Row>
        <div className ="footie">
        <a href="https://github.com/BenjaminDarking/project_pry"> Get involved in our Open Source API </a>
        </div>

      </div>
    );
  }
}

export default App;
