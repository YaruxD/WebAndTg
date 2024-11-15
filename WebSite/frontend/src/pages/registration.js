import axios from 'axios'

import React, { Component } from 'react';
import { Link } from 'react-router-dom';



class Registration extends Component {
    

    render() {
       

        return (
            <>
            <div className="flex items-center justify-center" style={{ marginTop: '280px', marginBottom: '120px' }}>
                <div className="input__container_register">
                    
                    
                    <input
                        type="text"
                        className="input__search"
                        placeholder="Nickname"
                    />
                    <input
                        type="text"
                        className="input__search"
                        placeholder="password"
                    />
                    <input
                        type="text"
                        className="input__search"
                        placeholder="email"
                    />

                    <div className="auth__row">
                        <Link to='/authorization'>Sign In!</Link>
                        <button className="input__button__shadow">
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