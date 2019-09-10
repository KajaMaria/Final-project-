import React, { Component } from 'react';
import { Layout, Footer, Textfield, FooterSection, FooterLinkList, Header, Navigation, Drawer, Content } from 'react-mdl';

class FooterBar extends Component {
    render() {
        return(
            <div>
            <Footer size="mini">
           <FooterSection type="left" logo="Title">
              <FooterLinkList>
                  <a href="#">Help</a>
                  <a href="#">Privacy & Terms</a>
              </FooterLinkList>
           </FooterSection>
           </Footer>
            </div>
        
        )
    }
}

export default FooterBar;



