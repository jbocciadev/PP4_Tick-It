// Script to add Event listeners to ticket-list rows
document.addEventListener("DOMContentLoaded", function(){
    let rows = document.getElementsByClassName("ticket-row");
    for (let row of rows) {
        row.addEventListener("click", function() {
            let pk = row.getAttribute("data-ticket");
            let currentURL = window.location.href;
            let newURL = currentURL.replace('ticket_list/', `view/${pk}`);
            // console.log(currentURL, newURL);
            window.open(newURL, name="_self");
        })
    }

    let statusOption = document.getElementById("status-option");
    let statusSaveBtn = document.getElementById("status-save-btn");
    statusOption.addEventListener("change", function(){
        statusSaveBtn.classList.remove("visually-hidden");
    });

})