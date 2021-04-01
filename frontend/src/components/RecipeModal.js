import React from 'react';
import Modal from '@material-ui/core/Modal';
import Grid from "@material-ui/core/Grid";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faHamburger, faPizzaSlice, faDrumstickBite, faPepperHot} from '@fortawesome/free-solid-svg-icons'
import Container from "@material-ui/core/Container";

function RecipeModal(props) {
    const {open, setClose, recipe} = props;

    const ingredientList = recipe.ingredients.map(ingr => {

        const iconId = Math.floor(Math.random() * 4);
        const icon = iconId === 0 ? faHamburger : iconId === 1 ? faPizzaSlice : iconId === 2 ? faDrumstickBite : faPepperHot;

        const faIcon = <FontAwesomeIcon icon={icon}/>
        return (
            <Grid xs={3}>
                <p><span className="sub-color">{faIcon} </span> {ingr.ingredient} </p>
            </Grid>
        )
    });

    const body =
        <div className="center-modal">
            <Grid container spacing={2}>
                <Grid item xs={12} alignContent="center" justify="center">
                    <h1 className="text-center sub-color">
                        {recipe.name}<br/>
                        <img atl="recipe-image" src={recipe.img} width={350} height={350}
                             className="modal-image text-center"/>
                    </h1>

                </Grid>
                <Grid item xs={12}>
                    <h3 className="sub-color text-center"> Category </h3>
                    <p className="text-center" style={{fontSize: "35px"}}>{recipe.category}</p>

                </Grid>

            </Grid>
            <Grid item xs={12}>
                <h3 className="sub-color text-center">Instructions</h3>
                <p>{recipe.instructions}</p>
            </Grid>
            <Grid item xs={12}>
                <h3 className="sub-color text-center">Ingredients</h3>
                <Container style={{width: "75%"}} className="some-space-please">

                    <Grid container spacing={1}>
                        {ingredientList}
                    </Grid>
                </Container>
            </Grid>
        </div>;

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