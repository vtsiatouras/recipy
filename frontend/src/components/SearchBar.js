import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import React from "react";

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

export default SearchBar;
