// Script to add Event listeners to ticket-list rows
const slugify = str =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');

function showBtn (btn) {
    btn.classList.remove("visually-hidden");
    btn.removeAttribute("disabled");
    btn.parentElement.classList.remove("visually-hidden");        
};

document.addEventListener("DOMContentLoaded", function(){
    let rows = document.getElementsByClassName("ticket-row");
    for (let row of rows) {
        row.addEventListener("click", function() {
            let pk = row.getAttribute("data-ticket");
            let currentURL = window.location.href;
            let newURL = currentURL.replace('ticket_list/', `view/${pk}`);
            window.open(newURL, name="_self");
        })
    };

    // Event listeners for ticketDetail form
    let saveBtn = document.getElementById("saveBtn");    
    let selectItems = document.getElementsByTagName("select");
    for (item of selectItems) {
        item.addEventListener("change", function(e) {
            showBtn(saveBtn);
            // Need to implement list modification depending on team members
        })
    }
    
})
