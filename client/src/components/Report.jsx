import { useState , useEffect} from 'react';
import { useNavigate } from 'react-router-dom';

const Report = () => {
    const navigate = useNavigate()

//     useEffect(() => {
//     if (!localStorage.getItem('accessToken')) {
//         navigate('/login');
//     }
// }, [navigate]);
    const [dateFound, setDateFound] = useState('');
    const [locationFound, setLocationFound] = useState('');
    const [description, setDescription] = useState('');
    const [file, setFile] = useState(null);
    const [category, setCategory] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('dateFound', dateFound);
        formData.append('locationFound', locationFound);
        formData.append('description', description);
        formData.append('file', file);
        formData.append('category', category);

        const response = await fetch("http://localhost:5000/items/add", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        if (data.status === 200) {
            navigate('/items');
        } else {
            alert(data.message);
        }
    };

    return (
        <section id="report__form__container">
            <form id="report__form" onSubmit={handleSubmit}>
                <label htmlFor='date_found'>
                    Date Found:
                    <input 
                        type="date" 
                        id='date_found' 
                        value={dateFound} 
                        onChange={(e) => setDateFound(e.target.value)} 
                    />
                </label>
                <label htmlFor="description">
                    Description:
                    <input 
                        type="text" 
                        id='description' 
                        value={description} 
                        placeholder='A black book' 
                        onChange={(e) => setDescription(e.target.value)} 
                    />
                </label>
                <label htmlFor="file">
                    Upload File:
                    <input 
                        type="file" 
                        id='file' 
                        onChange={handleFileChange} 
                    />
                </label>
                <label htmlFor="category">
                    Category:
                    <input 
                        type="text" 
                        id='category' 
                        value={category} 
                        placeholder='Stationery' 
                        onChange={(e) => setCategory(e.target.value)} 
                    />
                </label>
                <label htmlFor="location">
                    Location Found:
                    <input 
                        type="text" 
                        id='location' 
                        value={locationFound} 
                        placeholder='Nairobi' 
                        onChange={(e) => setLocationFound(e.target.value)} 
                    />
                </label>
                <button type="submit">Submit</button>
            </form>
        </section>
    );
};

export default Report;
