import React from "react";
import SearchBar from "./SearchBar";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormGroup from "@material-ui/core/FormGroup";
import Checkbox from "@material-ui/core/Checkbox";
import withStyles from "@material-ui/core/styles/withStyles";
import green from "@material-ui/core/colors/green";
import Alert from "@material-ui/lab/Alert";

const GreenCheckbox = withStyles({
    root: {
        color: green[400],
        '&$checked': {
            color: green[600],
        },
    },
    checked: {},
})((props) => <Checkbox color="default" {...props} />);

function Sites(props) {
    const {sites, setSiteCheckbox} = props;
    const handleChange = (event) => {
        setSiteCheckbox(event.target.value, event.target.checked)
    };

    return (
        <div className="site-box-wrapper">
            <div className="site-box">

                <FormGroup aria-label="position" column>
                    {sites.map(site => {
                        return <FormControlLabel key={site.id}
                                                 value={site.id}
                                                 control={<GreenCheckbox color="primary" checked={site.ischecked}
                                                                         onChange={handleChange}/>}
                                                 label={site.name}
                                                 labelPlacement="end"
                        />
                    })}
                </FormGroup>
            </div>
            <p> Found <span className="sub-color">{sites.length}</span> sites!</p>
        </div>
    )
}


function Cover(props) {
    const {search, onSearchChange, sites, setSiteCheckbox, fetchSearchRecipes, alert} = props;
    const coverSize = search ? "5%" : "8%";

    return (
        <div className="cover" style={{paddingTop: coverSize}}>
            <h3> Welcome to </h3>
            <h1> Reci<span className="sub-color">Py</span></h1>
            <p> Find different recipes from multiple sites.</p>
            <SearchBar onSearchChange={onSearchChange} fetchSearchRecipes={fetchSearchRecipes}/>
            <Sites sites={sites} setSiteCheckbox={setSiteCheckbox}/>

            {alert.show && <div className="search-alert">
                <Alert severity={alert.type}>{alert.msg}</Alert>
            </div>}
        </div>
    );
}

export default Cover;
