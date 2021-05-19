import Pagination from "@material-ui/lab/Pagination";
import React from "react";

function PageComp(props) {
    const {total, page, onPageChange} = props;
    const pagesCount = Math.floor(total / 20);
    if (pagesCount > 1)
        return (
            <div className="pagination-wrapper">
                <Pagination count={pagesCount} onChange={onPageChange} color="primary" page={page} style={{margin:"auto"}}/>
            </div>
        );
    else
        return null;
}

export default PageComp;
