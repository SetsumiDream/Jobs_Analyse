//首页基本js
$(function() {
    $('.box input[type="button"]').eq(1).click(function(){

        var phone = $('.inputBox input[type="text"]').val();
        console.log(phone);
        var phonenum = /^1[3|4|5|7|8][0-9]{9}$/;
        if (phone == "") {
            window.alert("请输入手机号")
        }else if(!phonenum.test(phone)){
            window.alert("请输入正确的手机号")
        }else{
            $.ajax({
                url: location.search + "/api/user/submit/phone/",
                type: 'post',
                data: {'phone': phone},
                // headers:{'X-CSRFToken': '{{ csrf_token }}'},
                dataType: 'json',
                success:function (data) {
                    if (data.code==0) {
                        window.alert("验证码发送成功");
                    }else{
                        window.alert("验证码发送失败");
                    }
                    }
            })
        }
	});



    $('.box input[type="button"]').eq(0).click(function(){

        var phone = $('.inputBox input[type="text"]').val();
        var vcode = $('.inputBox input[type="vcode"]').val();
        console.log(phone);
        var phonenum = /^1[3|4|5|7|8][0-9]{9}$/;
        if (phone == "") {
            window.alert("请输入手机号")
        }else if(!phonenum.test(phone)){
            window.alert("请输入正确的手机号")
        }else{
            $.ajax({
                url: location.search + "/api/user/submit/vcode/",
                type: 'post',
                data: {'phone': phone,
                    'vcode': vcode
                },
                // headers:{'X-CSRFToken': '{{ csrf_token }}'},
                dataType: 'json',
                success:function (data) {
                    if (data.code==0) {
                        window.location.href = location.search + '/main/'
                    }else{
                        window.alert("验证码错误");
                    }
                    }
            })
        }
	})

});