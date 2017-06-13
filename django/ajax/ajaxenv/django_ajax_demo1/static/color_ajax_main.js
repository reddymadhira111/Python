var MILLS_TO_IGNORE_SEARCH = 100;
var MILLS_TO_IGNORE_LIKES = 500;

$(document).ready(function() {
	$('#color_search_text').keyup(_.debounce(processSearch, MILLS_TO_IGNORE_SEARCH, true));
	$('.td__toggle_color_like_button').click(_.debounce(processLike, MILLS_TO_IGNORE_LIKES, true));
});