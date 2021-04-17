$(function(){




                //propertychange监听input里面的字符变化,属性改变事件
                $('input').bind('input propertychange', function() {
                    var $this = $(this);
                    var text_length = $this.val().length;//获取当前文本框的长度
                    var current_width = parseInt(text_length) *16;//该16是改变前的宽度除以当前字符串的长度,算出每个字符的长度
                    $this.css("width",current_width+"px");
                });



                $("button[name='edit']").bind('click', function() {
                   input=$(this).parent("td").siblings("td");
                   console.log(input.attr("contenteditable"));
                   if(input.attr("contenteditable")=="false"){
                      input.attr("contenteditable","true")
                   }
                   else{
                      input.attr("contenteditable","false")
                   }
                });

            })





 function tdchange(){
       console.log( $("input[name='combination']").val())
       console.log( $("td[name='combination_td']").html())
     if($("td[name='name_td']").html()!=$("input[name='name']").val()){
      $("input[name='name']").val($("td[name='name_td']").html());
     }
       if($("td[name='sex_td']").html()!=$("input[name='sex']").val()){
      $("input[name='sex']").val($("td[name='sex_td']").html());
     }
      if($("td[name='date_td']").html()!=$("input[name='date']").val()){
      console.log($("input[name='date']").val());
      $("input[name='date']").val($("td[name='date_td']").html());
     }
     if($("td[name='syndrome_td']").html()!=$("input[name='syndrome']").val()){
      $("input[name='syndrome']").val($("td[name='syndrome_td']").html());
     }
         if($("td[name='source_td']").html()!=$("input[name='source']").val()){
      $("input[name='source']").val($("td[name='source_td']").html());
     }

         if($("td[name='combination_td']").html()!=$("input[name='combination']").val()){
      $("input[name='combination']").val($("td[name='combination_td']").html());

     }
 }
