/*
Function to add ingredients and set proper attribute values
*/

$(".add-ingredient").click(function (event) {
    event.preventDefault();
    let ingredientDetails = $(".ingredient-details").children().first().clone();
    let numIngredients = $(".ingredient-details").children().length + 1;
    // Attributes for, id and name should be unique 
    ingredientDetails.find(".recipe-ingredient label").html("Ingredient " + numIngredients).attr("for", "ingredient-" + numIngredients);
    ingredientDetails.find(".recipe-ingredient input").val("").attr("id", "ingredient-" + numIngredients).attr(
        "name", "ingredient-" + numIngredients).attr("placeholder", "Ingredient " + numIngredients);
    ingredientDetails.find(".recipe-quantity label").attr("for", "quantity-" + numIngredients);
    ingredientDetails.find(".recipe-quantity input").val("").attr("id", "quantity-" + numIngredients).attr(
        "name", "quantity-" + numIngredients);
    ingredientDetails.find(".recipe-unit label").attr("for", "unit-" + numIngredients);
    ingredientDetails.find(".recipe-unit input").val("").attr("id", "unit-" + numIngredients).attr(
        "name", "unit-" + numIngredients);
    // Append cloned and modified elements
    $(".ingredient-details").append(ingredientDetails);
})