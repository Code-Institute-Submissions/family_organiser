var tl = gsap.timeline()

$(document).on('click','.toggle-menu', function() {
    if ($('.burger-container').hasClass('closed')) {
        // open the navigation bar
        tl.to('.mobile-navigation-links', 0.4, {transform: "translate(-50vw, 0)"});
        tl.to('.burger-container', 0.4, {transform: "translate(-50vw, 0)"},'-=0.4');
        tl.to('#navigation-alpha-over', 0.5, {transform: 'translate(0vw, 0)'},'-=0.2')
        tl.from('.navigation-item', 0.3, {transform: "translate(50vw, 0)", stagger: 0.05}, '-=0.6');
        tl.to('#navigation-alpha-over', 0.5, {opacity: 0.96},'-=0.7')
        gsap.to('.burger-top', 0.5, {transform: 'translate(6px, 9px) rotateZ(45deg)'})
        gsap.to('.burger-mid', 0.5, {opacity: 0})
        gsap.to('.burger-bottom', 0.5, {transform: 'translate(6px, -9px) rotateZ(-45deg)'})
    } else {
        // close the navigaiton bar
        tl.to('#navigation-alpha-over', 0.4, {transform: 'translate(100vw, 0)'})
        tl.to('.mobile-navigation-links', 0.4, {transform: "translate(10vw, 0)"},'-=0.2');
        tl.to('.burger-container', 0.4, {transform: "translate(0vw, 0)"},'-=0.4');
        tl.to('#navigation-alpha-over', 0.5, {opacity: 0.5},'-=0.3')
        gsap.to('.burger-top', 0.5, {transform: 'rotateZ(0deg)'})
        gsap.to('.burger-mid', 0.5, {opacity: 1})
        gsap.to('.burger-bottom', 0.5, {transform: 'rotateZ(0deg)'})
    }
    $('.burger-container').toggleClass('closed')
})






