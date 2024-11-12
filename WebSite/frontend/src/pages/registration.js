

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
                        <Link to='/authorization'>Sign up!</Link>
                        <button className="input__button__shadow">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#000000" width="20px" height="20px">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16a6.471 6.471 0 0 0 4.23-1.57l.27.28v.79l5 5L20.49 19l-5-5zm-6 0C8.01 14 6 11.99 6 9.5S8.01 5 10.5 5 15 7.01 15 9.5 12.99 14 10.5 14z"></path>
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