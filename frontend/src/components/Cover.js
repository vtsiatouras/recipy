import React from "react";
import SearchBar from "./SearchBar";

function Cover(props) {
    const CoverSize = props.size;

    return (
        <div className="cover" style={{paddingTop: CoverSize + "%"}}>
            <h3> Welcome to </h3>
            <h1> Reci<span className="sub-color">Py</span></h1>
            <p> Find different recipes from multiple sites.</p>
            <SearchBar/>
        </div>
    );
}

export default Cover;
