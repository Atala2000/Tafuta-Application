import { useState } from 'react';

const SignUp = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [phone, setPhone] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:5000/auth/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password, firstName, lastName, phone })
        });
        const data = await response.json();
        if (response.status === 200) {
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
            setSuccess('Sign up successful! Please log in.');
            setError('');
        } else {
            setError(data.message || 'An error occurred');
            setSuccess('');
        }
    }

    return (
        <section id="signup__form__container">
            <form id="signup__form" onSubmit={handleLogin}>
                <h1>Sign Up</h1>
                {error && <p className="error">{error}</p>}
                {success && <p className="success">{success}</p>}
                <label htmlFor="firstName">
                    First Name:
                    <input
                        type="text"
                        id="firstName"
                        placeholder="John"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                        required
                    />
                </label>
                <label htmlFor="lastName">
                    Last Name:
                    <input
                        type="text"
                        id="lastName"
                        placeholder="Doe"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                        required
                    />
                </label>
                <label htmlFor="email">
                    Email:
                    <input
                        type="email"
                        id="email"
                        placeholder="example@gmail.com"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </label>
                <label htmlFor="password">
                    Password:
                    <input
                        type="password"
                        id="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </label>
                <label htmlFor="phone">
                    Phone Number:
                    <input
                        type="text"
                        id="phone"
                        placeholder="+254712345678"
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        required
                    />
                </label>
                <button type="submit">Register</button>
            </form>
        </section>
    );
}

export default SignUp;
