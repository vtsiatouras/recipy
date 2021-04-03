import React from "react";
import SearchBar from "./SearchBar";

function Cover(props) {
    const {search, onSearchChange, fetchSearchRecipes} = props;
    const coverSize = search ? "5%" : "15%";

    return (
        <div className="cover" style={{paddingTop: coverSize }}>
            <h3> Welcome to </h3>
            <h1> Reci<span className="sub-color">Py</span></h1>
            <p> Find different recipes from multiple sites.</p>
            <SearchBar onSearchChange={onSearchChange} fetchSearchRecipes={fetchSearchRecipes}/>
        </div>
    );
}

export default Cover;
