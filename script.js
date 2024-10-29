document.addEventListener('DOMContentLoaded', () => {
    loadRecipes();
    
    const recipeForm = document.getElementById('recipe-form');
    recipeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        addRecipe();
    });
});

function addRecipe() {
    const name = document.getElementById('recipe-name').value;
    const ingredients = document.getElementById('recipe-ingredients').value;
    const instructions = document.getElementById('recipe-instructions').value;

    const recipe = {
        name,
        ingredients,
        instructions,
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

    recipesList.innerHTML = '';
    
    recipes.forEach(recipe => {
        const recipeCard = document.createElement('div');
        recipeCard.className = 'recipe-card';
        
        recipeCard.innerHTML = `
            <h3>${recipe.name}</h3>
            <h4>Ingredients:</h4>
            <p>${recipe.ingredients.replace(/\n/g, '<br>')}</p>
            <h4>Instructions:</h4>
            <p>${recipe.instructions}</p>
            <button onclick="deleteRecipe(${recipe.id})" class="delete-btn">Delete Recipe</button>
        `;

        recipesList.appendChild(recipeCard);
    });
}
