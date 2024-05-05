const Report = () => {
    return (
        <>
            <form className="report-form">
                <legend>
                    <label htmlFor="user_name">Name: </label>
                    <input type="text" required name="user_name" id="user_name" />
                </legend>
                <legend>
                    <label htmlFor="location_found">Location found: </label>
                    <input type="text" id="location_found" required name="location_found" />
                    <label htmlFor="description" id="description">Item Description: </label>
                    <input type="text" id="description" name="description" required />
                    <label htmlFor="category">Category: </label>
                    <select id="category" name="category">
                        <option value="electronics">Electronics</option>
                        <option value="clothing">Clothing</option>
                        <option value="identification">Identification</option>
                    </select>
                    <label htmlFor="filename">Upload file</label>
                    <input type="file" name="filename" id="filename" />
                </legend>
            </form>
        </>
    )
}

export default Report