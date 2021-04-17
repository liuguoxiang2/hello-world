  $(function(){
        //页面加载完毕后触发事件
        $("input[name='name']").bind('input propertychange', function() {
           console.log(1)

           if($(this).val()=="无"){
           $("input[name='sex']").attr("disabled", true);
           $("input[name='sex']").attr("disabled", true);
           }


         else{
         $("input[name='sex']").attr("disabled", false);
          $("input[name='sex']").attr("disabled", false);
         }
 });
    });