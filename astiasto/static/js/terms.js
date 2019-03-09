$(() => {
  
  $(document).ready(function() {
    console.log( "logging!" );
  });

  $(document).ready(function(){
        $(".dee").load("/static/txt/teksti.txt", function(responseTxt, statusTxt, xhr){
    });
  });
});
