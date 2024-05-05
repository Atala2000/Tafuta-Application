import { Link, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import './App.css';
import Index from './components/Index';
import Footer from './components/Footer';
import Report from './components/Report';


function App() {
  return (
    <>
        <Navbar />
        <Routes>
          <Route path='/' element={<Index />} />
          <Route path='/report' element={<Report />} />
          
        </Routes>
        <Footer />
    </>
  );
}

export default App;
