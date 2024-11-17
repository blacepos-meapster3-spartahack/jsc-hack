import React from 'react';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

function Header() {
    return (
      <Navbar bg="dark" data-bs-theme="dark">
      <Container>
        <Navbar.Brand href="/">Crew Health And Wellbeing Monitor and Predictor (CHAWMP)</Navbar.Brand>
      </Container>
      </Navbar>
    );
  }
  
  export default Header;