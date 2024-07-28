import { useState } from 'react';

const Login = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:5000/auth/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        const data = await response.json();
        if (response.status === 200) {
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
        } else {
            console.log(data);
        }
    }

    return (
        <section id="login__form__container">
            <form id="login__form" onSubmit={handleLogin}>
                <label htmlFor="username">
                    Username:
                    <input 
                        type="text" 
                        id="username" 
                        placeholder="Username" 
                        value={email} 
                        onChange={(e) => setEmail(e.target.value)} 
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
                    />
                </label>
                <button type="submit">Login</button>
            </form>
        </section>
    );
}

export default Login;
