import React from "react";
import { MDBCol, MDBContainer, MDBRow, MDBFooter } from "mdbreact";

const FooterBar = () => {
  return (
    <MDBFooter color="blue" className="font-small pt-4 mt-4">
      <MDBContainer fluid className="text-center text-md-left">
        <MDBRow>
          <MDBCol className="footer-copyright text-center py-3">
            <h5 className="title">Botter By General May Be</h5>
            <p>
            <a href="https://github.com/BenjaminDarking/project_pry"> Get involved in our Open Source API </a>
            </p>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
      <div className="footer-copyright text-center py-3">
        <MDBContainer fluid>
          &copy; {new Date().getFullYear()} Copyright: <a href="https://github.com/BenjaminDarking/project_pry"> Botter By General May Be </a>
        </MDBContainer>
      </div>
    </MDBFooter>
  );
}

export default FooterBar;
