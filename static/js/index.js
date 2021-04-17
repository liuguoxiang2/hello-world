window.onload = function(){


   $(".layui-nav-item").find("a").each(function () {

     var url = 'http://127.0.0.1:8000'+$(this).attr('href');
        if (window.location.href==url){
          console.log($(this))
         $(this).closest('.layui-nav-item').addClass("layui-nav-itemed");
         $(this).addClass("layui-this");
        }
        else{

        }
  });

}



