document.addEventListener('DOMContentLoaded', () => {
    loadRecipes();
    
    const recipeForm = document.getElementById('recipe-form');
    recipeForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        await addRecipe();
    });

    const cuisineFilter = document.getElementById('cuisine-filter');
    cuisineFilter.addEventListener('change', () => {
        loadRecipes();
    });
});

function convertImageToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(file);
    });
}

async function addRecipe() {
    const name = document.getElementById('recipe-name').value;
    const cuisine = document.getElementById('recipe-cuisine').value;
    const ingredients = document.getElementById('recipe-ingredients').value;
    const instructions = document.getElementById('recipe-instructions').value;
    const imageFile = document.getElementById('recipe-image').files[0];

    let imageData = null;
    if (imageFile) {
        imageData = await convertImageToBase64(imageFile);
    }

    const recipe = {
        name,
        cuisine,
        ingredients,
        instructions,
        image: imageData,
        id: Date.now()
    };

    let recipes = getRecipes();
    recipes.push(recipe);
    localStorage.setItem('recipes', JSON.stringify(recipes));

    document.getElementById('recipe-form').reset();
    loadRecipes();
}

function deleteRecipe(id) {
    let recipes = getRecipes();
    recipes = recipes.filter(recipe => recipe.id !== id);
    localStorage.setItem('recipes', JSON.stringify(recipes));
    loadRecipes();
}

function getRecipes() {
    return JSON.parse(localStorage.getItem('recipes') || '[]');
}

function loadRecipes() {
    const recipesList = document.getElementById('recipes-list');
    const recipes = getRecipes();
    const selectedCuisine = document.getElementById('cuisine-filter').value;

    recipesList.innerHTML = '';
    
    const filteredRecipes = selectedCuisine 
        ? recipes.filter(recipe => recipe.cuisine === selectedCuisine)
        : recipes;

    filteredRecipes.forEach(recipe => {
        const recipeCard = document.createElement('div');
        recipeCard.className = 'recipe-card';
        
        recipeCard.innerHTML = `
            <h3>${recipe.name}</h3>
            <p class="cuisine-tag">${recipe.cuisine}</p>
            ${recipe.image ? `<img src="${recipe.image}" alt="${recipe.name}" class="recipe-image">` : ''}
            <h4>Ingredients:</h4>
            <p>${recipe.ingredients.replace(/\n/g, '<br>')}</p>
            <h4>Instructions:</h4>
            <p>${recipe.instructions}</p>
            <button onclick="deleteRecipe(${recipe.id})" class="delete-btn">Delete Recipe</button>
        `;

        recipesList.appendChild(recipeCard);
    });
}
