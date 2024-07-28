import { useEffect, useState } from 'react';

const Items = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            const response = await fetch('http://localhost:5000/items/');
            const data = await response.json();
            setItems(data);
        }
        fetchItems();
    }, []);

    return (
        <>
            <h1>Items</h1>
            <section id="items__container">
                {items.map(item => (
                    <div key={item.id} className="item__container">
                        <span className="item__img">
                            <img src={item.file_url} alt={item.name} />
                        </span>
                        <span className="item__body">
                        <h2>{item.name}</h2>
                        <p>{item.description}</p>
                        <p>Date Found: {item.date_found}</p>
                        <p>Location Found: {item.location_found}</p>
                        <p>Category: {item.category}</p>
                        </span>
                    </div>
                ))}
            </section>
        </>
    )
}

export default Items;