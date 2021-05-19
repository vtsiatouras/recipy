import React from "react";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faSearch} from '@fortawesome/free-solid-svg-icons'

function SearchBar(props) {
    const {onSearchChange, fetchSearchRecipes} = props;

    return (
        <Container maxWidth="sm">
            <Grid container spacing={3}>
                <Grid item xs={10}>
                    <input type="email" className="form-control" onChange={onSearchChange} placeholder="Search for a recipe like: Sushi"/>
                </Grid>
                <Grid item xs={2}>
                    <Button variant="contained" color="primary" onClick={() => fetchSearchRecipes(1)}>
                        <span className="sub-color"><FontAwesomeIcon icon={faSearch}/></span>Search
                    </Button>
                </Grid>
            </Grid>
        </Container>
    )
}

export default SearchBar;
