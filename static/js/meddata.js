$(document).ready(function(){
   $('.alldata').each(function () {
  	 var x = $(this).find('#sys').text();
     var y = $(this).find('#dia').text();
     var z = (parseInt(x) + 2*parseInt(y))/3;
     $(this).find('#map').html(z.toFixed(2));
	});
});