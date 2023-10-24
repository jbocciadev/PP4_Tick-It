// Script to add Event listeners
document.addEventListener("DOMContentLoaded", function(){
    // Open detail view for clicked ticket
    let rows = document.getElementsByClassName("ticket-row");
    for (let row of rows) {
        row.addEventListener("click", function() {
            let pk = row.getAttribute("data-ticket");
            let currentURL = window.location.href;
            let newURL = currentURL.replace('ticket_list/', `view/${pk}`);
            window.open(newURL, name="_self");
        })
    };    
})
