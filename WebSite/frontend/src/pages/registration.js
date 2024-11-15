
import axios from 'axios'
import React, { Component } from 'react';
import { Link } from 'react-router-dom';



class Registration extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            password: '',
        };
    }
    
      // ... existing code ...

handleChange = event => {
    // Update only the field that changed
    this.setState({ [event.target.name]: event.target.value });
}

handleSubmit = event => {
    event.preventDefault();
    
    const userData = {
        username: this.state.name,
        password: this.state.password
    };
    
    
    axios.post(`http://127.0.0.1:8000/api/User`, userData, {
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(res => {
        console.log('Success:', res.data);
        // Redirect or show success message
    })
    .catch(error => {
        console.log('Error response:', error.response?.data); // Debug log
        console.log('Error status:', error.response?.status);
        console.log('Error headers:', error.response?.headers);
    });
}
    
    
    render() {
       

        return (
            <>
            <div className="flex items-center justify-center" style={{ marginTop: '280px', marginBottom: '120px' }}>
                <div className="input__container_register">
                    
                    
                    <input
                        type="text"
                        className="input__search"
                        placeholder="Nickname"
                        name="name"          
                        value={this.state.name}
                        onChange={this.handleChange}
                    />
                    <input
                        type="text"
                        className="input__search"
                        placeholder="password"
                        name="password"       
                        value={this.state.password}
                        onChange={this.handleChange}
                    />
                    

                    <div className="auth__row">
                        <Link to='/authorization'>Sign In!</Link>
                        <button className="input__button__shadow " onClick={this.handleSubmit}>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#000000" width="20px" height="20px">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path d="M9 16.2l-3.5-3.5a1 1 0 0 1 1.41-1.41L9 13.38l7.09-7.09a1 1 0 0 1 1.41 1.41L9 16.2z"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>


            </>
        );
    }
}

export default Registration;