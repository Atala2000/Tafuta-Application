import mascot from '../assets/images/index-mascot.png'
import '../assets/styles/Index.css'

const Contact = () => {
    return (
        <>
            <form id='contact-us'>
                <label htmlFor="name">Name: </label>
                <input type="text" id="name" name="name" placeholder="John Doe" />
                <label htmlFor="phone_no">Phone No: </label>
                <input type="number" required id="phone_no" name="phone_no" />
                <label htmlFor="message">Write us a message: </label>
                <input type="text" name="message" id="message" required />
            </form>
        </>
    )
}

const Numbers = () => {
    return (
        <section className="our-numbers">
            <h3 className='title'>Our Numbers</h3>
            <article id="card-numbers">
                <div className="numbers-blob">
                    <div id="items-reported">
                        <p>
                            <span className="numbers">
                                10
                            </span>
                            Items reported
                        </p>
                        <hr />
                    </div>
                    <div id="items-connected">
                        <p>
                            <span className="numbers">
                                10
                            </span>
                            Items connected
                        </p>
                        <hr />
                    </div>
                </div>
            </article>
        </section>
    )
}


const Details = () => {
    return (
        <section className='process-details'>
            <article id='process'>
                <h3 className='title'>Our Process</h3>
                <p>
                    <span>3</span> steps, find the item, report the item on our platform and
                    then our sofware will connect you to the owner of the item. 3 easy efficient steps
                </p>
            </article>
            <Numbers />
            <Contact />
        </section>
    )
}


const Header = () => {
    return (
        <header>
            <div className='header-details'>
                <h1 id='title'>TA<span className='text-white'>FUTA</span></h1>
                <h2>Find <span className='text-white'>Report</span> Connect</h2>
                <button>Report</button>
            </div>
            <div className='header-mascot'>
                <img src={mascot} loading='lazy' />
            </div>
        </header>
    )
}


const Index = () => {
    return (
        <main>
            <Header />
            <Details />
        </main>
    )
}

export default Index