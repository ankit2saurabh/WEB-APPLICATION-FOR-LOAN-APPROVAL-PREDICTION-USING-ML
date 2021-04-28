// Time Section
var d = new Date();
var date = d.getDate();
var month = d.getMonth() + 1; // Since getMonth() returns month from 0-11 not 1-12
var year = d.getFullYear();
date = date < 10 ? "0" + date : date;
month = month < 10 ? "0" + month : month;
var dateStr = date + "/" + month + "/" + year;
document.getElementById("date").innerHTML = dateStr;
setInterval(showTime, 1000);
function showTime() {
  let time = new Date();
  let hour = time.getHours();
  let min = time.getMinutes();
  let sec = time.getSeconds();
  am_pm = "AM";
  if (hour > 12) {
    hour -= 12;
    am_pm = " PM";
  }
  if (hour == 0) {
    hr = 12;
    am_pm = " AM";
  }
  hour = hour < 10 ? "0" + hour : hour;
  min = min < 10 ? "0" + min : min;
  sec = sec < 10 ? "0" + sec : sec;
  let currentTime = hour + ":" + min + ":" + sec + "  " + am_pm;
  document.getElementById("clock").innerHTML = currentTime;
}
showTime();

// Number Validation
function validateNumber() {
  var x = document.getElementById("defaultFormNum");
  var pattern = /^\+?([0-9]{2})\)?[-. ]?([0-9]{4})[-. ]?([0-9]{4})$/;
  if (x.value.match(pattern)) return true;
  // else if (x.value.length > 10)
  //     document.getElementById("numHelp").innerHTML = "Mobile Number Length must be 10 digit";
  else {
    document.getElementById("numHelp").innerHTML = "Pattern didn't Match...";
    return false;
  }
}

// E-Mail Validation
function validatePassword() {
  var passw = document.getElementById("passw").value;
  var cpass = document.getElementById("cpass").value;
  if (passw == "") alert("Password field is empty");
  else if (passw !== cpass) {
    alert("Password didn't match");
    return false;
  }
}

// News Element

$(".counter-count").each(function () {
  $(this)
    .prop("Counter", 0)
    .animate(
      {
        Counter: $(this).text(),
      },
      {
        //chnage count up speed here
        duration: 4000,
        easing: "swing",
        step: function (now) {
          $(this).text(Math.ceil(now));
        },
      }
    );
});

// Contact Us Page

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();
