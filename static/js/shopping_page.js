console.log('working')

$(document).on('click', '.plus-minus-square', function() {
    $(this).toggleClass('fa-plus-square')
    $(this).toggleClass('fa-minus-square')
});

$(document).on('click', '.select-category-inputs', function() {
    var inputClass = '.'.concat(this.id);
    if ($(inputClass).prop('checked') == true) {
        $(inputClass).prop('checked', false);
    } else {
        $(inputClass).prop('checked', true);
    }
});

$(document).on('click', '.select-all-checkboxes', function() {
    var inputClass = '.checkbox';
    if ($(inputClass).prop('checked') == true) {
        $(inputClass).prop('checked', false);
    } else {
        $(inputClass).prop('checked', true);
    }
})