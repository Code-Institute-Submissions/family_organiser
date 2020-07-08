// move page container to reveal form
$(document).on('click', '.add-form', function() {
    if ($('#add-data-form-container').hasClass('closed')) {
        // show the form
        tl.to('.profile-page-container', 0.5, {transform: 'translate(0, 350px)'})
    } 
    $('#add-data-form-container').removeClass('closed')
});

// send status form
$(document).on('click', '#send-button-status', function() {
    if ($('#form-title').val() == '') {
        $('#error-container').html('<p class="m-0 text-danger">Please add a title</p>')
    } else if ($('#form-content').val() == '') {
        $('#error-container').html('<p class="m-0 text-danger">Please add content to your post</p>')
    } else {
        $('#status-form').submit()
    }
});


// send item form
$(document).on('click', '#send-button-item', function() {
    if ($('#form-item').val() == '') {
        $('#error-container').html('<p class="m-0 text-danger">Please add an item</p>')
    } else if ($('#form-quantity').val() == '') {
        $('#error-container').html('<p class="m-0 text-danger">Please add the quantity for your item</p>')
    } else if ($('#form-category').val() == '') {
        $('#error-container').html('<p class="m-0 text-danger">Please select a category for you item</p>')
    } else {
        $('#status-form').submit()
    }
});

