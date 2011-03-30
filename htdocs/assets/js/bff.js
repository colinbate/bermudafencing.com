(function ($) {
	var $map;
	
	var toggleMap = function () {
		$map.slideToggle();
		return false;
	};
	
	$(function () {
		$map = $('#map');
		$map.hide();
		$('#maplink').click(toggleMap);
	});
}(jQuery));