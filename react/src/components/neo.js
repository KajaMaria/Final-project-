import React, { Component } from "react";
import NeoVis from 'neovis.js';


export class Neo extends Component {
    state = {
        neo_labels: [],
        neo_relationships: []
    }

    fetchData() {

        let config = {
            container_id: "viz",
            server_url: "bolt://localhost:7687/",
            server_user: "neo4j",
            server_password: "dansbugs",
            labels: {
                "User": { name: "screen_name" }
            },
            relationships: {
                TWEETED: ""
            },
            initial_cypher: "MATCH p=(:User)-[:TWEETED]->(:Source) RETURN p"
        };

        var viz = new NeoVis(config);
        viz.render();

    }

    componentDidMount() {
        this.fetchData();
    }

    render() {
        return (

            <div id="viz"></div>

        );
    }
}

export default Neo;