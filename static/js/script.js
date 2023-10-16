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
            // console.log(currentURL, newURL);
            window.open(newURL, name="_self");
        })
    };

    // Event listeners for ticketDetail form
    let saveBtn = document.getElementById("saveBtn");    
    let selectItems = document.getElementsByTagName("select");
    for (item of selectItems) {
        item.addEventListener("change", function(e) {
            // function for change of status
            if (e.target.name == "status"){
                showBtn(saveBtn);
            }
            // function for change of team
            else if (e.target.name == "assigned_team"){
                console.log(e.target.name);
                let assignedTeam = document.getElementById("team");
                let teamSlug = slugify(assignedTeam.value);
                let memberOptions = document.getElementsByName("member");
                for (member of memberOptions){
                    member.setAttribute("disabled", "");
                    member.classList.add("visually-hidden");
                }
                let selectedTeam = document.getElementsByClassName(teamSlug)[0];
                selectedTeam.removeAttribute("disabled");
                selectedTeam.classList.remove("visually-hidden");
                showBtn(saveBtn);                
            }
            // function for change of member
            else if (e.target.name == "assigned_member") {
                console.log(e.target.name);
                showBtn(saveBtn);
            }
        })
    }
    
})
