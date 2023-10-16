// Script to add Event listeners to ticket-list rows
const slugify = str =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');

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

    let assignedTeam = document.getElementById("ticket_detail_team");
    
    assignedTeam.addEventListener("change", function() {
        let teamSlug = slugify(assignedTeam.value);
        let memberOptions = document.getElementsByName("member");
        for (member of memberOptions){
            member.setAttribute("disabled", "");
            member.classList.add("visually-hidden");
        }
        let selectedTeam = document.getElementsByClassName(teamSlug)[0];
        selectedTeam.removeAttribute("disabled");
        selectedTeam.classList.remove("visually-hidden");
    });
    
    
})