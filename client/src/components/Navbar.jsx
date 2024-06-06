import { Navbar, NavbarToggle } from "react-bootstrap";
import { Container } from "react-bootstrap";
import { Nav } from "react-bootstrap";
import { Routes } from "react-router-dom";
import { Link } from "react-router-dom";

const NavBar = () => {
    return (
        <Navbar collapseOnSelect bg="dark" data-bs-theme="dark" expand="lg" className="bg-body-tertiary">
            <Container>
                <Navbar.Brand href="#home">Tafuta</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="me-auto">
                            <Nav.Link href="#home" as={Link} to="/">Home</Nav.Link>
                            <Nav.Link href="#features" as={Link} to="/items">Items</Nav.Link>
                            <Nav.Link href="#pricing" as={Link} to="/report">Report</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default NavBar