$(function(){
    var initial_comment_display = $('span.comment button').html();
    $('#QESinput').focus(function(){
    	$('#makeQuestion').css({'display':'none'});
    	$('.search_detail_box').show();
		$(this).css('width','300px');
	})
	 $('#QESinput').blur(function(){
		$('#makeQuestion').css({'display':'block'});
		$('.search_detail_box').hide();
		
		$(this).css('width','250px');
	})

	$('.profile_img_box').click(function(){
		$('span.menu_arrow').toggle();
		$('.user_profile_menu').toggle();
	})

	$('span.comment').click(function(){
		$('.comments_container').toggle();
		if($('.comments_container').css('display')=='block'){
			$('span.comment button').html('<i class="fa fa-comment" aria-hidden="true"></i>'+'收起评论');
		}else{
			$('span.comment button').html(initial_comment_display);
		}
	})

	$('span.cclose').click(function(){
		$('.modal_wrapper').hide();
		$('.comments_container').hide();
	});

	$('#makeQuestion').click(function(){
		$('.modal_wrapper').css('display','flex');
		$('.make_question_container').show();
	});

	$('span.close').click(function(){
		$('.modal_wrapper').hide();
		$('.make_question_container').hide();
	});
})