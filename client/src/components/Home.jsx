import { Link } from "react-router-dom";
import HomeImage from '../assets/images/hand-phone.png'

const Home = () => {
    return (
        <section id="home__page">
            <div className="title">
                <div className="title__text">
                    <h1>Welcome To Tafuta</h1>
                    <p>Search, Find, Connect</p>
                </div>
                <div className="title__image">
                    <img src={HomeImage} alt="Lost and Found" />
                </div>
            </div>
            <div className="home__content">
                <div className="home__content__text">
                    <h2>What is Tafuta?</h2>
                    <p>
                        Tafuta is a platform that allows users to report lost items and search for found items.
                        Users can also connect with each other to return found items.
                    </p>
                    <p>
                        The process is simple, look for your lost item and once you find it click accept and a message is sent to the other party
                        From there you can connect with them to arrange for the return of the item.
                    </p>
                    <div className="links">
                        <button><Link to="/report">Report</Link></button>
                        <button><Link to="/items">Items</Link></button>
                    </div>
                </div>
            </div>
        </section>
    );
}

export default Home;
