import { useState, useEffect } from 'react';
import { Link, Routes, Route } from 'react-router-dom';
import Home from './Home';
import Report from './Report';
import Items from './Items';
import Login from './Login';
import Logout from './Logout';
import ErrorBoundary from './Error';
import SignUp from './SignUp';
import '../assets/scss/Dashboard.scss';

const Dashboard = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('accessToken'));

    useEffect(() => {
        const handleStorageChange = () => {
            setIsAuthenticated(!localStorage.getItem('accessToken'));
        };

        // Listen for changes in localStorage
        window.addEventListener('storage', handleStorageChange);

        // Clean up event listener on component unmount
        return () => {
            window.removeEventListener('storage', handleStorageChange);
        };
    }, []);

    return (
        <ErrorBoundary>
            <nav>
                <Link to="/home" className='nav__link'>Home</Link>
                <Link to="/report" className='nav__link'>Report</Link>
                <Link to="/items" className='nav__link'>Items</Link>
                {!isAuthenticated ? (
                    <>
                        <Link to="/login" className='nav__link'>Login</Link>
                        <Link to="/register" className='nav__link'>Register</Link>
                    </>
                ) : (
                    <Link to="/logout" className='nav__link'>Logout</Link>
                )}
            </nav>
            <main>
                <Routes>
                    <Route path="/home" element={<Home />} />
                    <Route path="/report" element={<Report />} />
                    <Route path="/items" element={<Items />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/logout" element={<Logout />} />
                    <Route path="/register" element={<SignUp />} />
                </Routes>
            </main>
        </ErrorBoundary>
    );
};

export default Dashboard;
