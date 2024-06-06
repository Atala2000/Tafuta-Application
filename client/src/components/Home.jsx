import { Button } from "react-bootstrap"

const LearnMore = () => {
    return (
        <Button variant="primary">Learn More</Button>
    )
}

const Home = () => {
    return (
        <div>
            <h1>Welcome to Tafuta</h1>
            <p>
                Tafuta is a simple search engine that allows you to search for items.
            </p>
            <LearnMore />
        </div>
    )
}

export default Home;