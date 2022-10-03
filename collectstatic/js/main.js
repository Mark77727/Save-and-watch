/*Меню*/
$('ul.menu a[href^="index.html"').click(function(){
    var target=$(this).attr('href')
    $('html,body').animate({
        scrollTop: $(target).offset().top
    }, 500);
    return false;
})
/*выпадающее меню*/
$('.bar').click(function() {
    $('nav').slideToggle (500);
    $('ul').css({
        'display':'flex','flex-direction':'column'
    })

})

/*кнопка на вверх*/
$(window).scroll(function () {
    if ($(this).scrollTop() !=0)
    $('#toTop').fadeIn();
        else
        $('#toTop').fadeOut();
    });
    $('#toTop').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
    });
