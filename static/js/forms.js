// move page container to reveal form
$(document).on("click", ".add-form", function() {
    if ($("#add-data-form-container").hasClass("closed")) {
        // show the form
        tl.to(".profile-page-container", 0.5, {transform: "translate(0, 555px)"});
    } 
    $("#add-data-form-container").removeClass("closed");
});

// send status form
$(document).on("click", "#send-button", function() {

    // Try and submit the status form
    try {
        if ($("#form-title").val().length == 0) {
            $("#error-container").html("<p class='m-0 text-danger'>Please add a title</p>");
        } else if ($("#form-content").val().length == 0) {
            $("#error-container").html("<p class='m-0 text-danger'>Please add content to your post</p>");
        } else {
            $("#status-form").submit();
        };
        // if not try and submit the item form 
    } catch {
        if ($("#form-item").val().length == 0) {
            $("#error-container").html("<p class='m-0 text-danger'>Please add an item</p>");
        } else if ($("#form-quantity").val().length == 0) {
            $("#error-container").html("<p class='m-0 text-danger'>Please add the quantity for your item</p>");
        } else if ($("#form-category").val().length == 0) {
            $("#error-container").html("<p class='m-0 text-danger'>Please select a category for you item</p>");
        } else {
            $("#item-form").submit();
        };
    };
});
