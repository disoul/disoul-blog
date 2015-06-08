var leftflag = 1;

$(document).ready(function(){
		$(".left-list-control").click(function(){
			 if (leftflag > 0){
					 $(".left-list").animate({width: '220px'});
					 $(".left-list-control i").removeClass('fa-angle-double-right');
					 $(".left-list-control i").addClass('fa-angle-double-left');
					 leftflag = -leftflag;
			 }else{
					 $(".left-list").animate({width: '0px'});	
					 $(".left-list-control i").removeClass('fa-angle-double-left');
					 $(".left-list-control i").addClass('fa-angle-double-right');
					 leftflag = -leftflag;
			 }
		});
});
