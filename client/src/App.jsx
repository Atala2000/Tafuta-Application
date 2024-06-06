import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Container } from "react-bootstrap";
import NavBar from "./components/Navbar";
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from "./components/Home";
import Report from "./components/Report";
import Items from "./components/Items";

const App = () => {
  return (
    <BrowserRouter>
      <NavBar />
      <Container> {/* Add top margin to create space */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/items" element={<Items />} />
          <Route path="/report" element={<Report />} />
        </Routes>
      </Container>
    </BrowserRouter>
  )
}

export default App;
