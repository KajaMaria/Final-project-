import React, { Component } from 'react';
import { Layout,  Textfield, Drawer, Content } from 'react-mdl';


class Layout extends Component {
    render() {
        return(
                <div class="demo-layout-transparent mdl-layout mdl-js-layout">

            <Layout fixedHeader fixedDrawer>
            
            <Navigation setLoaded={setLoaded} /> 
                
                <Content>
                <div className="page-content" />
                <Main />
                </Content>  
            </Layout>
                </div>
        )
    }
}

export default Layout;


