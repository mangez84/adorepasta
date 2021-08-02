/* 
The attributes for, id and name should be unique
*/

function modifyAttributes() {
    let numIngredients = 0;
    $(".recipe-ingredient label").each(function (index) {
        numIngredients = index + 1;
        $(this).html("Ingredient " + numIngredients).attr("for", "ingredient-" + numIngredients);
    });
    $(".recipe-ingredient input").each(function (index) {
        numIngredients = index + 1;
        $(this).attr("id", "ingredient-" + numIngredients).attr("name", "ingredient-" + numIngredients).attr(
            "placeholder", "Ingredient " + numIngredients);
    });
    $(".recipe-quantity label").each(function (index) {
        numIngredients = index + 1;
        $(this).attr("for", "quantity-" + numIngredients);
    });
    $(".recipe-quantity input").each(function (index) {
        numIngredients = index + 1;
        $(this).attr("id", "quantity-" + numIngredients).attr("name", "quantity-" + numIngredients);
    });
    $(".recipe-unit label").each(function (index) {
        numIngredients = index + 1;
        $(this).attr("for", "unit-" + numIngredients);
    });
    $(".recipe-unit input").each(function (index) {
        numIngredients = index + 1;
        $(this).attr("id", "unit-" + numIngredients).attr("name", "unit-" + numIngredients);
    });
}

/*
Function to add ingredients
*/

$(".add-ingredient > button").click(function (event) {
    event.preventDefault();
    let ingredientDetails = $(".ingredient-details").children().first().clone();
    ingredientDetails.find(".recipe-ingredient input").val("");
    ingredientDetails.find(".recipe-quantity input").val("");
    ingredientDetails.find(".recipe-unit input").val("");
    $(".ingredient-details").append(ingredientDetails);
    modifyAttributes();
});

/*
Function to remove ingredients
*/

$(document).on("click", ".remove-ingredient > button", function (event) {
    event.preventDefault();
    let numIngredients = $(".ingredient-details").children().length;
    if (numIngredients !== 1) {
        $(this).parent().parent().remove();
    }
    modifyAttributes();
});