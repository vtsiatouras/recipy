import React from 'react';
import './App.css';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Input from '@material-ui/core/Input';
import Button from '@material-ui/core/Button';
import Container from "@material-ui/core/Container";

function SearchBar() {
    return (
        <Container maxWidth="sm">
            <Grid container spacing={3}>
                <Grid item xs={10}>
                    <input type="email" className="form-control" placeholder="Search for a recipe like: Sushi"/>
                </Grid>

                <Grid item xs={2}>
                    <Button variant="contained" color="primary">
                        Search
                    </Button>
                </Grid>
            </Grid>
        </Container>
    )
}

function Cover() {
    return (
        <div className="cover ">
            <h3> Welcome to </h3>
            <h1> Reci<span className="sub-color">Py</span></h1>
            <p> Find different recipes from multiple sites.</p>
            <SearchBar/>
        </div>
    );
}

function App() {
    return (
        <div>
            <Cover/>
        </div>
    );
}

export default App;
