import Card from "./components/card.js"
import axios from "axios"
import React, { Component } from 'react';
import Search from "./components/search.js";
import Header from "./components/header.js";

const CatalogUrl = "http://127.0.0.1:8000/api/Catalog"



class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [], // начальное состояние
        };
    }

    componentDidMount() {
        axios.get(CatalogUrl)
            .then((res) => {
                this.setState({ data: res.data }); // обновление состояния
            })
            .catch((error) => {
                console.error("Error fetching data:", error);
            });
    }

    render() {
        const { data } = this.state;

        return (
            <div>
                <div><Header></Header></div>
                <div className="flex  items-center justify-center mt-400" style={{ marginTop: '280px', marginBottom: '120px' }} ><Search></Search></div>
                <div className="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-40 gap-y-10">
                    {data.map((item, index) => (
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
            </div>
        );
    }
}

export default App;