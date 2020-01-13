$(window).scroll(() => {
    if ($(document).scrollTop() > 450) {
        $("nav").addClass("shrink")
        $(".navbar-form").show()
        
    } else  {
        $("nav").removeClass("shrink")
        $(".navbar-form").hide()

    }
})