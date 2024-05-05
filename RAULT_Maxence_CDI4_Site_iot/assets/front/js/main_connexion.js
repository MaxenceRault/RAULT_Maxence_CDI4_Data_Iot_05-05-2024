document.addEventListener("DOMContentLoaded", function () {
  const links = document.querySelectorAll("nav li");

  icons.addEventListener("click", function () {
    nav.classList.toggle("active");
  });

  links.forEach(function (link) {
    link.addEventListener("click", function () {
      nav.classList.remove("active");
    });
  });

  let form = document.getElementById("form");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    
    const name= document.getElementById("pseudo").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    const response = await fetch("http://localhost:3000/login", {
      method: "POST",
      body: JSON.stringify({ name, email, password }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  
    const data = await response.json();
  
    const token = data.token;
  
    localStorage.setItem("token",token);
    
    window.location.href = "./profile.html";
  });

  // form.addEventListener("submit", async (event) => {
  //   event.preventDefault();

  //   let errorContainer = document.querySelector(".message-error");
  //   let errorList = document.querySelector(".message-error ul");

  //   errorList.innerHTML = "";
  //   errorContainer.classList.remove("visible");

  //   let email = document.querySelector("#email");
  //   if (email.value === "") {
  //     errorContainer.classList.add("visible");
  //     email.classList.remove("success");

  //     let err = document.createElement("li");
  //     err.innerText = "Le champ email ne doit pas être vide";

  //     errorList.appendChild(err);
  //   } else {
  //     email.classList.add("success");
  //   }

  //   let pseudo = document.querySelector("#pseudo");
  //   if (pseudo.value.length < 6) {
  //     errorContainer.classList.add("visible");
  //     pseudo.classList.remove("success");

  //     let err = document.createElement("li");
  //     err.innerText = "Le pseudo doit avoir au moins 6 caractères";

  //     errorList.appendChild(err);
  //   } else {
  //     pseudo.classList.add("success");
  //   }

  //   let passCheck = new RegExp(
  //     "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[-+_!@#$%^&*.,?]).+$"
  //   );

  //   let password = document.querySelector("#password");
  //   if (
  //     password.value.length < 10 ||
  //     passCheck.test(password.value) === false
  //   ) {
  //     errorContainer.classList.add("visible");
  //     password.classList.remove("success");

  //     let err = document.createElement("li");
  //     err.innerText =
  //       "Le mot de passe doit avoir au moins 10 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial";

  //     errorList.appendChild(err);
  //   } else {
  //     password.classList.add("success");
  //   }

  //   let passwordConfirm = document.querySelector("#password2");
  //   if (password.value !== "") {
  //     if (password.value !== passwordConfirm.value) {
  //       errorContainer.classList.add("visible");
  //       passwordConfirm.classList.remove("success");

  //       let err = document.createElement("li");
  //       err.innerText = "Les deux mots de passe doivent être identiques";

  //       errorList.appendChild(err);
  //     } else {
  //       passwordConfirm.classList.add("success");
  //     }
  //   }

  //   let successContainer = document.querySelector(".message-success");
  //   successContainer.classList.remove("visible");

  //   if (
  //     email.classList.contains("success") &&
  //     pseudo.classList.contains("success") &&
  //     password.classList.contains("success") &&
  //     passwordConfirm.classList.contains("success")
  //   ) {
  //     successContainer.classList.add("visible");

  //   }
  // });

  
    
});
