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
    // let saveBtn = document.getElementById("saveBtn");  
    
    // let ticketForm = document.getElementById("ticketForm");
    // let statusForm = document.getElementById("statusForm");
    // let teamForm = document.getElementById("teamForm");
    // let memberForm = document.getElementById("memberForm");
    // let selectItems = document.getElementsByTagName("select");
    // let teamSelect = document.getElementById("team_select");
    // let memberSelect = document.getElementById("member_select");
    // let statusSelect = document.getElementById("status_select");
    // // let myModal = new bootstrap.Modal(document.getElementById("exampleModal"),{});
    // // console.log(selectItems);
    // for (item of selectItems) {
    //     if (item == statusSelect){
    //         item.addEventListener("change", function(){
    //             // teamSelect.setAttribute("disabled", "");
    //             // memberSelect.setAttribute("disabled", "");
    //             ticketForm.submit();
    //         })
    //     } else if (item == teamSelect) {
    //         item.addEventListener("change", function() {
    //             // statusSelect.setAttribute("disabled", "");
    //             // memberSelect.setAttribute("disabled", "");
    //             teamForm.submit();
    //         })
    //     } else {
    //         item.addEventListener("change", function(){
    //             // statusSelect.setAttribute("disabled", "");
    //             // teamSelect.setAttribute("disabled", "");
    //             memberForm.submit();
    //         })
    //     }
    // }
    
})
