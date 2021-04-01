import React, {useState} from 'react';
import './App.css';
import Cover from "./components/Cover";
import Body from "./components/Body";

import data from './assets/recipe_data_min'


function App() {


    const [coverSize, setCoverSize] = useState(5);  //starting at 15
    return (
        <div>
            <Cover size={coverSize}/>
            <Body recipes={data}/>
        </div>
    );
}

export default App;
