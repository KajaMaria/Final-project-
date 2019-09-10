import React, { Component } from 'react';
import { Footer,  FooterSection, FooterLinkList } from 'react-mdl';

class FooterBar extends Component {
    render() {
        return(
            <div>
            <Footer size="mini">
                <FooterSection type="left" logo="Footer">
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



