import { Link, NavLink } from "react-router-dom"
import '../assets/styles/Navbar.css'
import { useEffect, useState } from "react"

const Navbar = () => {
    const [scrolled, setScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                setScrolled(true);
            } else {
                setScrolled(false);
            }
        };
        document.addEventListener("scroll", handleScroll);

        return () => {
            document.removeEventListener("scroll", handleScroll);
        };
    }, []);


    return (
        <>
            <nav className={scrolled ? "nav-bar scrolled" : "nav-bar"}>
                <div className="logo">
                </div>
                <div className="nav-links">
                    <NavLink to='/'>Home</NavLink>
                    <NavLink to='/report'>Report</NavLink>
                    <NavLink to='/items'>Items</NavLink>
                </div>
            </nav>
        </>
    )
}

export default Navbar