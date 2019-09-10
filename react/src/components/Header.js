import React from 'react'
import { Layout, Footer, Textfield, FooterSection, FooterLinkList, Header, Navigation, Drawer, Content } from 'react-mdl';

class HeaderTab extends Component {
    render() {
        return (
            <div>
                <Header transparent title="Botter" style={{ color: 'white' }}>
                    <Textfield
                        value=""
                        onChange={() => { }}
                        label="Search"
                        expandable
                        expandableIcon="search"
                    />
                </Header>
            </div>
        )
    }
}

export default HeaderTab;


