import { Link, Routes, Route } from 'react-router-dom';
import Home from './Home';
import Report from './Report';
import Items from './Items';
import Login from './Login'; // Ensure this component is defined
import Logout from './Logout'; // Ensure this component is defined
import '../assets/scss/Dashboard.scss';

const Dashboard = () => {

    const isAuthenticated = !!localStorage.getItem('accessToken');
    return (
        <>
            <nav>
                <Link to="/home" className='nav__link'>Home</Link>
                <Link to="/report" className='nav__link'>Report</Link>
                <Link to="/items" className='nav__link'>Items</Link>
                {!isAuthenticated && <Link to="/login" className='nav__link'>Login</Link>}
            </nav>
            <main>
                <Routes>
                    <Route path="/home" element={<Home />} />
                    <Route path="/report" element={<Report />} />
                    <Route path="/items" element={<Items />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/logout" element={<Logout />} />
                </Routes>
            </main>
        </>
    );
};

export default Dashboard;
