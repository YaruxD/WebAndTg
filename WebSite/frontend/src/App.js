import React, { Component } from 'react';
import Header from "./components/header.js";
import { Routes, Route} from 'react-router-dom';
import Catalog from './pages/catalog.js';
import Authorization from './pages/authorization.js';
import Registration from './pages/registration.js';



class App extends Component {
    
    render() {
        return (
            <>
                <div>
                    <Header />
                    <Routes>
                        <Route path='/' element={<Catalog/>}/>
                        <Route path="/authorization" element={<Authorization />} />
                        <Route path="/registration" element={<Registration />} />
                    </Routes>  
                </div>
            </>
        );
    }
}



export default App;
