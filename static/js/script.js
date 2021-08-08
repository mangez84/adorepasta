/* 
The attributes for, id and name should be unique
*/

function modifyAttributes() {
    let numIngredients = 0;
    let numSteps = 0;
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
    $(".method label").each(function (index) {
        numSteps = index + 1;
        $(this).html("Method - Step " + numSteps).attr("for", "method-" + numSteps);
    });
    $(".method input").each(function (index) {
        numSteps = index + 1;
        $(this).attr("id", "method-" + numSteps).attr("name", "method-" + numSteps).attr("placeholder", "Step" + numSteps);
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

/*
Function to add a step to the method
*/

$(".add-step > button").click(function (event) {
    event.preventDefault();
    let method = $(".method").children().first().clone();
    method.find(".method-step input").val("");
    console.log(method);
    $(".method").append(method);
    modifyAttributes();
});

/*
Function to remove a step from the method
*/

$(document).on("click", ".remove-step > button", function (event) {
    event.preventDefault();
    let numSteps = $(".method").children().length;
    if (numSteps !== 1) {
        $(this).parent().parent().remove();
    }
    modifyAttributes();
});

/*
Function to confirm removal of a recipe
*/

$("button.delete-recipe").click(function (event) {
    event.preventDefault();
    let cancelButton = '<button type="button" class="btn btn-warning delete-cancel mx-3 my-1">Cancel</button>';
    $(this).parent().siblings().remove();
    $(this).parent().parent().prepend(cancelButton);
    $("button.delete-cancel").click(function () {
        location.reload();
    });
    $(this).html("Confirm").attr("type", "submit").trigger("blur");
    $(this).unbind("click");
});