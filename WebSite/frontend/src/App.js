import React, { Component } from 'react';
import Header from "./components/header.js";
import { Routes, Route} from 'react-router-dom';
import Registration  from './pages/registration';
import Catalog from './pages/catalog.js';



class App extends Component {
    
    render() {
        return (
            <>
                <div>
                    <Header />
                    <Routes>
                        <Route path='/' element={<Catalog/>}/>
                        <Route path="/registration" element={<Registration />} />
                        
                    </Routes>  
                </div>
            </>
        );
    }
}



export default App;
