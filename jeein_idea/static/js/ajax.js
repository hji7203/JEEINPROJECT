$(document).ready(function(){
	$('#submit').click(function(){
		var tweet_box = $('#tweet_box').val();
		$.ajax({
			url: '/tweet',
			type: 'POST',
			data:{"tweet_box" : tweet_box},
			success:function(response){
				var result = $.parseJSON(response);
				console.log(result);

				var table_content = "<table>";
				for (var i = 0; i < result.length ; i ++){
					table_content += '<tr><td>' + result[i]['user'] + result[i]['content'] +'</td></tr>';
				}
				table_content += "</table>";
				$('#table_here').append(table_content);

			},
			error: function(){
				console.log('error');
			},
			complete:function(){
				console.log('complete');
			}

		});
	});
});