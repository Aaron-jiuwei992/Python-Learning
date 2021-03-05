$(function () {
     $('li.logout').click(function(){
       var csrf = $('input[name="csrfmiddlewaretoken"]').val();
       $.ajax({
                url: '/logout/',
                type: 'post',
                data: {
                    'csrfmiddlewaretoken': csrf
                },
                success: function(res){
                    if(res.code == 0){
                        window.location.href="/login/";
                    }
                }
            })
    })
})
