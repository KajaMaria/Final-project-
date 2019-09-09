import React from 'react';
import './App.css';
import { Layout, Textfield, Header, Navigation, Drawer, Content } from 'react-mdl';
import Main from './components/main'

class App extends React.Component { 
  render() {
    return (
      <div style={{height: '1000px', position: 'relative'}}>
          <Layout fixedHeader fixedDrawer>
              <Header title="Title">
                  <Textfield
                      value=""
                      onChange={() => {}}
                      label="Search"
                      expandable
                      expandableIcon="search"
                  />
              </Header>
              <Drawer title="Title">
                  <Navigation>
                      <a href="#">Link</a>
                      <a href="#">Link</a>
                      <a href="#">Link</a>
                      <a href="#">Link</a>
                  </Navigation>
              </Drawer>
              <Content>
              <div className="page-content" />
              <Main />
              </Content>  
          </Layout>
      </div>

    );
  }
}

export default App;
