import React from 'react';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

function Header() {
    return (
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand>Predictive Astronaut Health Metrics</Navbar.Brand>
        </Container>
      </Navbar>
    );
  }
  
  export default Header;