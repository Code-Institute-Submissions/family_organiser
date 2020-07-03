var tl = gsap.timeline()

console.log('working')

$(document).on( 'click','#add-button', function() {
    if ($(this).hasClass('closed')) {
        // reveal the links
       tl.to('.profile-page-container', 0.5, {transform: 'translate(0, 0)'})
    } else {
        // hide the links
        tl.to('.profile-page-container', 0.5, {transform: 'translate(0, -64px)'})
    }
    console.log('clicked')
    $(this).toggleClass('closed')
});