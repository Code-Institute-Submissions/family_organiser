var tl = gsap.timeline()

$(document).on('click','.burger-container', function() {
    if ($(this).hasClass('closed')) {
        // open the navigation bar
        tl.to('.burger-container', 0.4, {transform: "translate(-50vw, 0)"});
        tl.to('.mobile-navigation-links', 0.4, {transform: "translate(-50vw, 0)"},'-=0.4');
        tl.from('.mobile-navigation-links li', 0.3, {transform: "translate(50vw, 0)", stagger: 0.05}, '-=0.2');
    } else {
        // close the navigaiton bar
        tl.to('.burger-container', 0.4, {transform: "translate(0vw, 0)"});
        tl.to('.mobile-navigation-links', 0.4, {transform: "translate(10vw, 0)"},'-=0.4');
    }
    $(this).toggleClass('closed')
})