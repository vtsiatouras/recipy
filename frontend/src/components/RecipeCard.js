import React, {useState} from 'react';

import {makeStyles} from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import RecipeModal from "./RecipeModal";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faUtensils} from "@fortawesome/free-solid-svg-icons";
import Alert from "@material-ui/lab/Alert";


const useStyles = makeStyles({
    root: {
        maxWidth: 345,
    },
    media: {
        height: 140,
    },
});

function RecipeCard(props) {
    const recipe = props.recipe;
    const [open, setOpen] = useState(false);
    const classes = useStyles();
    const setClose = () => {
        setOpen(false)
    };

    return (
        <div>
            {open && <RecipeModal open={open} setClose={setClose} recipeId={recipe.id} />}
            <Card className={classes.root} onClick={() => {setOpen(true)}}>
                <CardActionArea>
                    <CardMedia
                        className={classes.media}
                        image={recipe.image_url}
                        title="Contemplative Reptile"
                    />
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="h2">
                            {recipe.name}
                        </Typography>
                        <Typography gutterBottom variant="body1" component="h3" color="primary">
                            {recipe.category}
                        </Typography>
                            <FontAwesomeIcon icon={faUtensils} style={{marginRight: "10px"}}/>
                            <a href={recipe.site.url} style={{marginLeft: "10px"}} target="_blank">{recipe.site.name}</a>
                    </CardContent>
                </CardActionArea>
                <CardActions>
                    <Button size="small" color="primary">
                        Read More
                    </Button>
                </CardActions>
            </Card>
        </div>
    );
}

export default RecipeCard;