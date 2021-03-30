import React, {useState} from 'react';
import './App.css';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Container from "@material-ui/core/Container";
import RecipeCard from "./components/RecipeCard";

import arniPic from './assets/arni.jpg'
import paidakiaPic from './assets/paidakia.jpg'
import kotsiPic from './assets/kotsi.jpg';

function Cover(size) {
    return (
        <div className="cover" style={{paddingTop: size + "%"}}>
            <h3> Welcome to </h3>
            <h1> Reci<span className="sub-color">Py</span></h1>
            <p> Find different recipes from multiple sites.</p>
            <SearchBar/>
        </div>
    );
}

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


function Body() {
    return (
        <Container className="body-container">
            <Grid container spacing={2}>
                <Grid item xs={4}>
                    <RecipeCard img={kotsiPic} title={"Kotsi"}/>
                </Grid>
                <Grid item xs={4}>
                    <RecipeCard img={paidakiaPic} title={"Paidakia"}/>
                </Grid>
                <Grid item xs={4}>
                    <RecipeCard img={arniPic} title={"Arni"}/>
                </Grid>
            </Grid>
        </Container>
    )

}

function App() {
    const [coverSize, setCoverSize] = useState(15)
    return (
        <div>
            <Cover size={coverSize}/>
            <Body/>
        </div>
    );
}

export default App;
