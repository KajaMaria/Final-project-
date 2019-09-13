import React, { Component } from 'react'
import {Button, Spinner, ButtonToolbar } from 'react-bootstrap';

export class LoadingBar extends Component {
    render() {
        return (
            <ButtonToolbar>
                <Button variant="primary" disabled>
                    <Spinner
                    as="span"
                    animation="grow"
                    size="sm"
                    role="status"
                    aria-hidden="true"
                    />
                    Loading...
                </Button>
            </ButtonToolbar>
        )
    }
}

export default LoadingBar;

