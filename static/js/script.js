// transform string into slug
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

    // Event listeners for ticketDetail form
    let form = document.getElementById("assignmentForm");
    let saveBtn = document.getElementById("saveBtn");    
    let selectItems = document.getElementsByTagName("select");
    let teamSelect = document.getElementById("id_assigned_team");
    for (item of selectItems) {
        if (item == teamSelect){
            item.addEventListener("change", function(){
                form.submit();
            })
        } else  {
            item.addEventListener("change", function() {
                showBtn(saveBtn);
            })}
    }
    
})
