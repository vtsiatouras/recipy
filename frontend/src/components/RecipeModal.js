import React, {useEffect, useState} from 'react';
import Modal from '@material-ui/core/Modal';
import Grid from "@material-ui/core/Grid";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {
    faHamburger,
    faPizzaSlice,
    faDrumstickBite,
    faPepperHot,
    faExternalLinkAlt
} from '@fortawesome/free-solid-svg-icons'
import Container from "@material-ui/core/Container";
import Alert from '@material-ui/lab/Alert';
import axios from "axios";
import CenteredSpinner from "./CenteredSpinner";


function Ingredient(props){
    const { ingredient } = props;
    const iconId = Math.floor(Math.random() * 4);
            const icon = iconId === 0 ? faHamburger : iconId === 1 ? faPizzaSlice : iconId === 2 ? faDrumstickBite : faPepperHot;
            const faIcon = <FontAwesomeIcon icon={icon}/>;

            return (
                <Grid item xs={3}>
                    <p><span className="sub-color">{faIcon} </span> {ingredient.description} </p>
                </Grid>
            );
}

function RecipeModal(props) {
    const {open, setClose, recipeId} = props;
    const [recipe, setRecipe] = useState({});
    const [fetching, setFetching] = useState(true);

    useEffect(async () => {
        console.log("fetch recipe with id", recipeId);
        try {
            const response = await axios.get('http://localhost:8000/api/v1/recipes/' + recipeId);
            setRecipe(response.data);
            setFetching(false);
        } catch (e) {
            console.log("Error on fetching recipe details caught")
        }
    }, []);


    const body = fetching ?
            <div>
                <CenteredSpinner/>
            </div>
        :
        <div className="center-modal">
            <Grid container spacing={2} alignContent="center" justify="center">
                <Grid item xs={12}>
                    <h1 className="text-center sub-color">
                        {recipe.name}<br/>
                        {/*width={350} height={350}*/}
                        <img alt="recipe" src={recipe.image_url}
                             className="modal-image text-center"/>
                    </h1>
                </Grid>
                <Grid item xs={12}>
                    <h3 className="sub-color text-center"> Category </h3>
                    <p className="text-center" style={{fontSize: "35px"}}>{recipe.category}</p>
                </Grid>
                <Grid item xs={12}>
                    <h3 className="sub-color text-center">Instructions</h3>
                    <p>{recipe.instructions}</p>
                </Grid>
                <Grid item xs={12}>
                    <h3 className="sub-color text-center">Ingredients</h3>
                    <Container style={{width: "75%"}} className="some-space-please">
                        <Grid container spacing={1}>
                            {recipe.ingredients.map(ingredient => {return <Ingredient ingredient={ingredient}/>})}
                        </Grid>
                    </Container>
                </Grid>
                <Grid item xs={12}>
                    <Container style={{width: "25%"}} className="">
                        <Alert severity="success" className="sub-color text-center" icon={false}>
                            <FontAwesomeIcon icon={faExternalLinkAlt} style={{marginRight: "20px"}}/>
                            Find the original recipe
                            <a href={recipe.url} style={{marginLeft: "10px"}} target="_blank">here</a>
                        </Alert>
                    </Container>
                </Grid>
            </Grid>
        </div>
    ;

    return (
        <div>
            <Modal
                className="my-modal"
                open={open}
                onClose={setClose}
                aria-labelledby="simple-modal-title"
                aria-describedby="simple-modal-description"
            >
                {body}
            </Modal>
        </div>
    );
}

export default RecipeModal;