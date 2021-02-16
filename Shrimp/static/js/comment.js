$(function () {
     $('div.comments_footer_box').click(function(){
       var comment = $('input[name="comment"]').val();
       var answer_id = $("div.contentItem_answerItem").attr("data-answer-id");
       var csrf = $('input[name="csrfmiddlewaretoken"]').val();

       $.ajax({
                url: '/comment/',
                type: 'post',
                data: {
                    comment: comment,
                    answer_id: answer_id,
                    'csrfmiddlewaretoken': csrf
                },
                success: function(res){
                    if(res.code == 0){
                        window.location.href="/";
                    }
                }
            })
    })

})