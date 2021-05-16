import React, {useEffect, useState} from 'react';
import './App.css';
import Cover from "./components/Cover";
import Body from "./components/Body";

import data from './assets/recipe_data_min'
import CenteredSpinner from "./components/CenteredSpinner";

import axios from "axios";

// axios.defaults.baseURL = "http://localhost:8000/api/v1/";
// axios.defaults.headers.Accept = "application/json";

function App() {
    const [search, setSearch] = useState(false);
    const [recipes, setRecipes] = useState([]);
    const [searchQuery, setSearchQuery] = useState("");
    const [spinner, setSpinner] = useState(false);
    const [sites, setSites] = useState([]);
    const [alert, setAlert] = useState({show: false, type: "", msg: ""});

    useEffect(async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/v1/sites');
            response.data.forEach(site => site.ischecked = true);
            setSites(response.data);
        } catch (e) {
            console.log("Error on fetching sites caught")
        }
    }, []);

    function setUpAlert(type, message){
        setAlert({show: true, type: type, msg: message});
        setTimeout(() => setAlert({show: false, type: "", msg: ""}), 3000)
    }

    const setSiteCheckbox = (id, value) => {
        const updatedSites = sites.map(site => {
            if (site.id == id) {
                site.ischecked = value;
            }
            return site;
        });
        setSites(updatedSites)
    };

    const fetchSearchRecipes = async () => {
        console.log("fetch results for query: ", searchQuery);
        const selectedSites = sites.filter(site=>{return site.ischecked});
        if(selectedSites.length === 0 || searchQuery.length === 0){
            setUpAlert("warning", "Bad request. Please provide a site and a query");
            return;
        }

        const laSiteIds = selectedSites.map(site => {
                return site.id
        }).toString();
        setRecipes([]);
        setSpinner(true);
        try {
            const responce = await axios.get(
                'http://localhost:8000/api/v1/recipes/getRecipes',
                {
                    params: {
                        query: searchQuery, site_ids: laSiteIds
                    }
                });
            console.log(responce.data);
            setRecipes(responce.data.results);
            setSearch(true);
        } catch (e) {
            setUpAlert("danger", "Request failed.");
            console.log("Error on fetching recipes caught")
        }
        setSpinner(false);
    };

    const onSearchChange = (e) => {
        const searchQuery = e.target.value;
        setSearchQuery(searchQuery)
    };

    return (
        <div>
            <Cover search={search} onSearchChange={onSearchChange} fetchSearchRecipes={fetchSearchRecipes}
                   sites={sites} setSiteCheckbox={setSiteCheckbox} alert={alert}/>
            {spinner && <CenteredSpinner/>}
            {!spinner && <Body recipes={recipes} search={search}/>}
        </div>
    );
}


export default App;
