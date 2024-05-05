document.addEventListener("DOMContentLoaded", function () {
  

  const links = document.querySelectorAll('nav li')

  icons.addEventListener("click", function(){
  nav.classList.toggle("active"); 
  })


  links.forEach( function(link){
    link.addEventListener('click',function(){
    nav.classList.remove("active")
  })
  })

  let currentPage = 1;

  async function fetchCards(page) {
    const url = `https://hp-api.lainocs.fr/characters`;
    const response = await fetch(url);
    const data = await response.json();
    displayCards(data);
  }

  function displayCards(cartes) {
    const container = document.getElementById("cards-container");
    const template = document.getElementById("cards-template");

    // Supprime les cartes précédentes, sauf le template
    container.innerHTML = "";
    container.appendChild(template);

    cartes.forEach((carte) => {
      const hpCard = template.cloneNode(true);
      hpCard.style.display = "block"; // Rend la carte visible

      hpCard.id = ""; // Enlève l'id pour éviter les doublons

      hpCard.querySelector(".cards-img").src=carte.image;
      hpCard.querySelector(".cards-title").textContent = carte.name;
      hpCard.querySelector(".cards-description").textContent = carte.house;
      hpCard.querySelector(
        ".cards-details-link"
      ).href = `detail.html?id=${carte.id}`;
      container.appendChild(hpCard);
    });
  }

  

  fetchCards(currentPage);




  
});




