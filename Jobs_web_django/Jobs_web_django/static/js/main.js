//首页基本js
$(function() {

    $.ajax({
    url: location.search + "/api/image/load/img/?target=0",
    type: 'get',
    dataType: 'json',
    success:function (data) {
        console.log(data);
        $('body').css({'background': 'url('+ data.data +')'});
        }
    });

    $('.box2').click(function(){
        window.location.href = location.search + '/jobs_analyse/'
	});


    var i = 1;
    var timer = setInterval(function(){
        if ( i===0) {
            // 停止定时器
            clearInterval(timer)
        }
        else {
            console.log(i++);
            var d = new Date();
            console.log(d.toLocaleString());
            time.innerHTML = d.toLocaleString()
        }
    },1000);



});