import { useEffect, useState } from 'react';

const Items = () => {
    const [items, setItems] = useState([]);
    const [filteredItems, setFilteredItems] = useState([]);
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState('All');
    const [error, setError] = useState(null);

    // Fetch categories when component mounts
    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await fetch('http://localhost:5000/items/');
                if (!response.ok) {
                    throw new Error('Failed to fetch categories');
                }
                const data = await response.json();
                if (Array.isArray(data)) {
                    const allCategories = [...new Set(data.map(item => item.category))];
                    setCategories(['All', ...allCategories]);
                } else {
                    setError('Unexpected data format received for categories');
                }
            } catch (error) {
                setError(`Error fetching categories: ${error.message}`);
            }
        };

        fetchCategories();
    }, []);

    // Fetch items based on selected category
    useEffect(() => {
        const fetchItems = async () => {
            try {
                let url = 'http://localhost:5000/items/';
                if (selectedCategory !== 'All') {
                    url += `category/${encodeURIComponent(selectedCategory)}`;
                }

                console.log('Fetching items from URL:', url); // Debugging URL

                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error('Failed to fetch items');
                }
                const data = await response.json();
                if (Array.isArray(data)) {
                    setItems(data);
                    setFilteredItems(data);
                } else {
                    setError('Unexpected data format received for items');
                }
            } catch (error) {
                setError(`Error fetching items: ${error.message}`);
            }
        };

        fetchItems();
    }, [selectedCategory]);

    // Handle notification to item owner
    const handleNotifyOwner = async (item) => {
        try {
            const response = await fetch(`http://localhost:5000/items/notify-owner/${item.id}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`,
                },
            });
            if (!response.ok) {
                throw new Error('Failed to send notification');
            }
            alert('Notification successfully sent to the owner.');
        } catch (error) {
            alert(`Failed to send notification: ${error.message}`);
        }
    };

    // Handle category selection change
    const handleCategoryChange = (event) => {
        setSelectedCategory(event.target.value);
    };

    return (
        <>
            <h1>Items</h1>
            <div className="filter-container">
                <label htmlFor="category-select">Filter by category:</label>
                <select
                    id="category-select"
                    className="filter-select"
                    value={selectedCategory}
                    onChange={handleCategoryChange}
                >
                    {categories.map(cat => (
                        <option key={cat} value={cat}>{cat}</option>
                    ))}
                </select>
            </div>
            <section id="items__container">
                {filteredItems.length > 0 ? (
                    filteredItems.map(item => (
                        <div key={item.id} className="item__container">
                            <span className="item__img">
                                <img src={`http://localhost:5000/${item.file_url}`} alt={item.name} />
                            </span>
                            <span className="item__body">
                                <h2>{item.name}</h2>
                                <p><strong>Description:</strong> {item.description}</p>
                                <p><strong>Date Found:</strong> {new Date(item.date_found).toLocaleDateString()}</p>
                                <p><strong>Location Found:</strong> {item.location_found}</p>
                                <p><strong>Category:</strong> {item.category}</p>
                                <button className="notify-btn" onClick={() => handleNotifyOwner(item)}>
                                    Notify Owner
                                </button>
                            </span>
                        </div>
                    ))
                ) : (
                    <p>No items found.</p>
                )}
                {error && <p className="error-message">Error: {error}</p>}
            </section>
        </>
    );
};

export default Items;
