import React, { Component } from 'react';
import { Layout, Footer, Textfield, FooterSection, FooterLinkList, Header, Navigation, Drawer, Content } from 'react-mdl';

export class NavigationBar extends Component {
    render() {
        return (
            <div>
                <Drawer title="Go Fish">
                  <Navigation >
                      <a href="#">After Bot Identification Criteria</a>
                      
                      {/* <a href="#" onClick={setloadedFalse()}>Frequency</a> */}
                      <a href="#">Tweets to Age Ratio</a>
                      <a href="#">Hours of Activity per day</a>
                    
                      <a href="#">After Scoring Criteria</a>
                    
                      <a href="#">Frequency Weight</a>
                      <a href="#">Tweets to Age Ratio Weight</a>
                      <a href="#">Hours of Activity per day Weight</a>
                    
                      <a href="#">Choose search start point</a>
                      <a href="#">Bot Graveyard</a>
                      {/* <a href="#" onClick={setLoaded}>Hours of Activity per day Weight</a>  */}
                  </Navigation>
              </Drawer>
            </div>
        )
    }
}

export default NavigationBar
