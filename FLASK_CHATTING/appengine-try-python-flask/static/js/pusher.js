$(document).ready(function(){
	var p = new Pusher('136fb99306188ba55ed3');
	var channel = p.subscribe('syg');
	channel.bind('notification', function(data){
		alert(data.username + ' is Online.');
	});
	$("#submit").click(function(){
		console.log("woierjw");
		var chat_box = $('#chat_box').val();
		console.log(chat_box);
		$.ajax({
			url: '/chat_box',
			type: 'POST',
			data:{"chat_box" : chat_box},
			// success:function(response){
			// 	//do something
			// 	console.log("woeirjwoie");
			// 	var result = $.parseJSON(response);
			// },
			// error: function(){
			// 	console.log('error');
			// },
			complete:function(){
				console.log('complete');
			}
		});
	});
	channel.bind('chatting', function(data){
		console.log(data);
		$("tr").append(data.username + " : ")
		$("tr").append(data.chat_box +"<br>")

	});

});