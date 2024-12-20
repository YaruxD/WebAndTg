import React, { useState } from 'react';

export default function Search({ onSearch }) {
    const [query, setQuery] = useState('');

    const handleInputChange = (e) => {
        const newQuery = e.target.value;
        setQuery(newQuery);
        onSearch(newQuery); // вызываем onSearch сразу после каждого изменения
    };

    return (
        <div className="input__container">
            <button className="input__button__shadow" onClick={() => onSearch(query)}>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#000000" width="20px" height="20px">
                    <path d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16a6.471 6.471 0 0 0 4.23-1.57l.27.28v.79l5 5L20.49 19l-5-5zm-6 0C8.01 14 6 11.99 6 9.5S8.01 5 10.5 5 15 7.01 15 9.5 12.99 14 10.5 14z"></path>
                </svg>
            </button>
            <input
                type="text"
                className="input__search"
                placeholder="Start typing"
                value={query}
                onChange={handleInputChange} // вызываем handleInputChange при каждом изменении
            />
        </div>
    );
}
