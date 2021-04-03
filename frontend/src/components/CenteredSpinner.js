import React from "react";
import Grid from "@material-ui/core/Grid";
import CircularProgress from "@material-ui/core/CircularProgress";

function CenteredSpinner() {
    return (
        <Grid
            container
            spacing={0}
            className="spinner-wrapper"
            direction="column"
            alignItems="center"
            justify="center"
        >
            <Grid item xs={3}>
                <CircularProgress size={120}/>
            </Grid>
        </Grid>
    );
}

export default CenteredSpinner;