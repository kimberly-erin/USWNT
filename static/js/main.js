console.log("js loaded");
function docready() {
	$('#get-results').on('click', function(){

		console.log("clicked");
		var rawData= $("#stats-form :input").serializeArray();
		var formData = JSON.stringify($("#stats-form").serializeArray());
		console.log(formData);
		console.log(rawData);
    $.ajax({
        type: "POST",
        url: "/get_prediction",
        contentType: 'application/json; charset=UTF-8',
		  data: formData,
        dataType: 'json',
        success: function(data){
            $('#my_table').html(data);
        },
        error: function(error){
            console.log(error);
        },

    });
});

};
