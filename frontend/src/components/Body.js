import React from "react";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";

import RecipeCard from "./RecipeCard";

import kotsiPic from "../assets/kotsi.jpg";
import paidakiaPic from "../assets/paidakia.jpg";
import arniPic from "../assets/arni.jpg";


function ResultsInfo(props){
    const {search, size} = props;
    const body = search ?
        <div>Found <span className="sub-color">{size}</span> tasty recipes</div> : <div> Some random results </div>;
    return (
        <Typography variant="h4" component="h4" className="text-center">
            {body}
        </Typography>
    )
}

function Body(props) {
    const {search, recipes} = props;
    console.log("rendering body with: ", search);

    const recipesContent = recipes.map(recipe => {
        // --to-be-deleted
        const imgId = Math.floor(Math.random() * 3);
        recipe.img = imgId === 0 ? paidakiaPic : imgId === 1 ? arniPic : kotsiPic;

        return (
            <Grid item lg={3} md={4} sm={6} xs={12} key={recipe.id}>
                <RecipeCard recipe={recipe}/>
            </Grid>
        )
    });

    return (
        <Container className="body-container">
            <div className="some-space-please"> <ResultsInfo search={search} size={recipes.length}/></div>
            <Grid container spacing={2}>
                {recipesContent}
            </Grid>
        </Container>
    )
}

export default Body;