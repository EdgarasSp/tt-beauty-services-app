/*jshint esversion: 6 */

/* load spinner */
$(window).on('load', function() {
	$(".loader").fadeOut("slow");
});

/* alert messages */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.contacting-form');
  });

// contact form validation

function validateForm() {
    let formvalid = true;

    // FIRST NAME & LAST NAME
    let firstname = document.forms["contactingForm"]["first_name"].value;
    let lastname = document.forms["contactingForm"]["last_name"].value;
    if (!/^[a-z_-]{1,50}$/i.test(firstname) || !/^[a-z_-]{1,50}$/i.test(lastname)) {
        formvalid = false;
        alert("Your name should only contain A-Z, a-z or the '-' character and be a maximum of 50 characters long. If your name contains other characters or symbols, please contact the department directly to book your appointment."); 
    }
    // CONTACT NUMBER 
    let contnum = document.forms["contactingForm"]["contact_number"].value;
    if (!/^0[0-9]{1,20}$/.test(contnum)) {
        formvalid = false;
        alert("Please provide a valid phone number between 5 and 20 numbers long using characters 0-9 (Please do not put spaces in your contact number)."); 
    }
    return formvalid;
    
  }
