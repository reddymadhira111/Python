var MILLS_TO_IGNORE_LIKES = 500;

var processLike = function() {
	var $button_just_clicked_on = $(this);
	var color_id = $button_just_clicked_on.data('color_id');
	var processServerResponse = function(serverResponse_data, textStatus_isjqXHR_ignored) {
		$('#toggle_color_like_cell_' + color_id).html(serverResponse_data);
	}
	var config = {
		url: LIKE_URL_PRE_ID + color_id + '/',
		dataType: 'html',
		success: processServerResponse
	};
	$.ajax(config);
};

