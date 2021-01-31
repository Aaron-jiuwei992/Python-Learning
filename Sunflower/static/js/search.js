$(function(){
    $('input#submit').on('submit',function(){
		/*
		获取id为query的输入框的值
		*/
		var query = $("input#query").val();
	    $.ajax({
			url:'/search/',
			type:'GET',
			data:{query: query}
		})
	});
	
})