import Card from "../components/card.js"
import axios from "axios"
import React, { Component } from 'react';
import Search from "../components/search.js";



const CatalogUrl = "http://127.0.0.1:8000/api/Catalog"

class Catalog extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [], 
            searchQuery: "" //поиск
        };
    }

    componentDidMount() {
        axios.get(CatalogUrl)
            .then((res) => {
                this.setState({ data: res.data });
            })
            .catch((error) => {
                console.error("Error fetching data:", error);
            });
    }

    handleSearch = (query) => {
        this.setState({ searchQuery: query });
    };

    render() {
        const { data, searchQuery } = this.state;

        // Фильтрация данных на основе поискового запроса
        const filteredData = data.filter(item =>
            item.Product.toLowerCase().includes(searchQuery.toLowerCase())
        );

        return (
            <>
                
                
                <div className="flex items-center justify-center" style={{ marginTop: '280px', marginBottom: '120px' }}>
                    <Search onSearch={this.handleSearch} />
                </div>
                <div className="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-40 gap-y-10">
                    {filteredData.map((item, index) => (
                        <Card
                            key={index}
                            type={item.Type}
                            product={item.Product}
                            photo={item.Photo}
                            price={item.Price}
                            description={item.Description}
                        />
                    ))}
                </div>
            </>
        );
    }
}



export default Catalog;
