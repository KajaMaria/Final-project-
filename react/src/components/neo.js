import React, { Component } from "react";
import NeoVis from "../../node_modules/neovis.js";

export class Neo extends Component {
  draw() {
    var config = {
      container_id: "viz",
      server_url: "bolt://localhost:7687",
      server_user: "",
      server_password: "",
      labels: {
        User: {}
      },
      initial_cypher: "MATCH (p) RETURN p"
    };
    var viz = new NeoVis(config);
    viz.render();
  }
  componentDidMount() {
    this.draw();
  }

  render() {
    return (
      <div>
        <div id="viz"></div>
      </div>
    );
  }
}

export default Neo;
