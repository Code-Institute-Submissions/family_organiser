console.log('working')

$(document).on('click', '.far', function() {
    $(this).toggleClass('fa-plus-square')
    $(this).toggleClass('fa-minus-square')
});