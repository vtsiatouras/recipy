import React, {useEffect, useState} from 'react';
import './App.css';
import Cover from "./components/Cover";
import Body from "./components/Body";
import axios from "axios";

import data from './assets/recipe_data_min'
import CircularProgress from "@material-ui/core/CircularProgress";
import Grid from "@material-ui/core/Grid";
import CenteredSpinner from "./components/CenteredSpinner";


function App() {
    const [search, setSearch] = useState(false);
    const [recipes, setRecipes] = useState([]);
    const [searchQuery, setSearchQuery] = useState("");
    const [spinner, setSpinner] = useState(false);

    useEffect(() => {
        console.log("fetch some random results");
        //here fetch some random recipes
    }, []);

    const fetchSearchRecipes = async () => {
        console.log("fetch results for query: ", searchQuery);
        setRecipes([]);
        setSpinner(true);

        // const responce = await axios.get('api/recipes', { params: { search: searchQuery}});
        // setRecipes(responce.data);
        // setSearch(true);
        // setSpinner(false);

        // test only case --to-be-deleted
        setTimeout(
            () => {
                setRecipes(data);
                setSearch(true);
                setSpinner(false);
            }, 3000
        )
    };

    const onSearchChange = (e) => {
        const searchQuery = e.target.value;
        console.log("onSearchChange: ", searchQuery);
        setSearchQuery(searchQuery)
    };

    return (
        <div>
            <Cover search={search} onSearchChange={onSearchChange} fetchSearchRecipes={fetchSearchRecipes}/>
            {spinner && <CenteredSpinner/>}
            {!spinner && <Body recipes={recipes} search={search}/>}
        </div>
    );
}


export default App;
