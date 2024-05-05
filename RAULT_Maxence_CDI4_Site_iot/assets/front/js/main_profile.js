document.addEventListener("DOMContentLoaded", async () => {
  const links = document.querySelectorAll("nav li");

  icons.addEventListener("click", function () {
    nav.classList.toggle("active");
  });

  links.forEach(function (link) {
    link.addEventListener("click", function () {
      nav.classList.remove("active");
    });
  });

  const tabButtons = document.querySelectorAll(".tab-btn");
  const tabPanes = document.querySelectorAll(".tab-pane");

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      tabButtons.forEach((btn) => {
        btn.classList.remove("active");
      });
      tabPanes.forEach((pane) => {
        pane.classList.remove("active");
      });

      const target = document.querySelector(button.dataset.tabTarget);
      button.classList.add("active");
      target.classList.add("active");
    });
  });

  const token = localStorage.getItem("token");

  if (!token) {
    window.location.href = "./login.html";
  }

  const response = await fetch("http://localhost:3000/getMyProfile", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.status === 401 || response.status === 403) {
    window.location.href = "./login.html";
    localStorage.removeItem("token");
  }

  const data = await response.json();

  document.getElementById("name").textContent = data.name;
  document.getElementById("email").textContent = data.email;
  console.log(data);
});
