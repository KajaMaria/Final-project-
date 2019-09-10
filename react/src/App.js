import React from 'react';
import './App.css';
import { Layout, Footer, Textfield, FooterSection, FooterLinkList, Header, Navigation, Drawer, Content } from 'react-mdl';
import Main from './components/main';
import classnames from "classnames";

class App extends React.Component { 
  render() {
    return (
      <div style={{height: '100vh', position: 'relative'}}>
        <div class="demo-layout-transparent mdl-layout mdl-js-layout">
          <Layout fixedHeader fixedDrawer>
             <Header transparent title="Botter" style={{color: 'white'}}>
                  <Textfield
                      value=""
                      onChange={() => {}}
                      label="Search"
                      expandable
                      expandableIcon="search"
                  />
              </Header>
              
              <Drawer title="Go Fish">
                  <Navigation >
                      <a href="#">After Bot Identification Criteria</a>
                      <Navigation>
                      <a href="#">Frequency</a>
                      <a href="#">Tweets to Age Ratio</a>
                      <a href="#">Hours of Activity per day</a>
                    </Navigation>
                      <a href="#">After Scoring Criteria</a>
                      <Navigation >
                      <a href="#">Frequency Weight</a>
                      <a href="#">Tweets to Age Ratio Weight</a>
                      <a href="#">Hours of Activity per day Weight</a>
                    </Navigation>
                      <a href="#">Choose search start point</a>
                      <a href="#">Bot Graveyard</a>
                      <a href="#">Hours of Activity per day Weight</a> 
                  </Navigation>
              </Drawer>
              <Content>
              <div className="page-content" />
              <Main />
              </Content>  
          </Layout>
      </div>

      <Footer size="mini">
    <FooterSection type="left" logo="Title">
        <FooterLinkList>
            <a href="#">Help</a>
            <a href="#">Privacy & Terms</a>
        </FooterLinkList>
    </FooterSection>
</Footer>
      </div>
    
   

    );
  }
}

export default App;
