const searchItem = document.URL
    .split("=")[1]
    .replaceAll('+',' ')

document.getElementById("searchBar").value = decodeURIComponent(searchItem);

const foodTemplate = document.getElementById("food-template");
const foodContainer = document.getElementById("food-container");

fetch("menu.json")
    .then(res => res.json())
    .then(data => {
        data.forEach(food => {
                const card = foodTemplate.content.cloneNode(true);
                const bgImg = card.getElementById("food-image-content");
                const foodName = card.getElementById("food-name");
                const foodLink = card.getElementById("food-button-link");
                bgImg.src = food.image;
                foodName.textContent = food.name;
                foodLink.href = food.link;
                const matched = food.name.toLowerCase().includes(searchItem.toLowerCase())
                if (matched) {
                    foodContainer.append(card);
                };
            }
        )
    }
    );

