// show selection list when user selects yes
function myCheckbox() {
  var checkBox = document.getElementById("myCheck");
  if (checkBox.checked == true) {
    document.getElementById("list1").disabled = false;
  } else {
    document.getElementById("list1").disabled = true;
  }
}
// REGEX validation for form inputs
function validation() {
  var email = document.getElementById("emailid").value;
  var pass = document.getElementById("password").value;
  var addr = document.getElementById("address").value;
  var dates = document.getElementById("date").value;
  var numb = document.getElementById("num").value;
  var emailcheck = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  //for special chars in email
  // /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  var passwordcheck =
    /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;
  var addrcheck =
    /^(\d{1,}) [a-zA-Z0-9\s]+(\,)? [a-zA-Z]+(\,)? [A-Z]{2} [0-9]{5,6}$/;
  var datescheck =
    /^(0?[1-9]|1[0-2])[\/\-](0?[1-9]|1\d|2\d|3[01])[\/\-](19|20)\d{2}$/;
  var numcheck = /\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{4})/;
  if (emailcheck.test(email)) {
    document.getElementById("one").innerHTML = "";
  } else {
    document.getElementById("one").innerHTML = "Enter Email in right format";
    return false;
  }
  if (passwordcheck.test(pass)) {
    document.getElementById("two").innerHTML = "";
  } else {
    document.getElementById("two").innerHTML = "Enter password in right format";
    return false;
  }
  if (addrcheck.test(addr)) {
    document.getElementById("three").innerHTML = "";
  } else {
    document.getElementById("three").innerHTML =
      "Enter address in right format";
    return false;
  }
  if (datescheck.test(dates)) {
    document.getElementById("four").innerHTML = "";
  } else {
    document.getElementById("four").innerHTML = "Enter date in right format";
    return false;
  }
  if (numcheck.test(numb)) {
    document.getElementById("five").innerHTML = "";
  } else {
    document.getElementById("five").innerHTML =
      "Enter phone numb in right format";
    return false;
  }

  alert("All data is valid...Form Submitted!!");
}
// Date validation if past date is selected
function dateval() {
  var before = new Date(document.getElementById("date").value);
  var now = new Date();
  if (before < now) {
    alert("Select a future date");
    return false;
  }
}
// character counter for textbox
function counter(msg) {
  document.getElementById("counter_div").innerHTML = msg.value.length + "/100";
}
// Checks if word lenght is less than 10 or more than 100 for textbox
function checkLength() {
  var textbox = document.getElementById("tarea");
  if (textbox.value.length > 100 || textbox.value.length < 10) {
    alert("Please enter a minimum of 10 chars and max of 100 chars!!");
  }
}

var navbar = ` 
<nav>
<div class="nav">
  <a class="aa" href="home.html" style="text-decoration: none;color: white;">Home</a>
  <a class="aa" href="gallery.html" style="text-decoration: none;color: white;">Gallery</a>
  <a class="aa" href="pricing.html" style="text-decoration: none;color: white;">Pricing</a>
  <a class="aa" href="contactus.html" style="text-decoration: none;color: white;">Contact Us</a>
</div>
</nav>     
      `;

// inserting navbar in beginning of body
document.body.insertAdjacentHTML("afterbegin", navbar);
