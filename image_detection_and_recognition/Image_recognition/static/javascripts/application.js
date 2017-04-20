$(function(){
  $(".file_details").hide();
  $("marquee").hover(function () { 
    this.stop();
    }, function () {
    this.start();
  });
  $('.go-to-top').bind("click", function () {
    $('html, body').animate({scrollTop: 0 }, 1200);
    return false;
  });
  $("#browse-input-file").change(function(){
    readURL(this);
  });
  function readURL(input) {
    var file_name = $("input").val();
    if(file_name) { 
      $("#file_name").html(file_name);
      var width=$("input#browse-input-file")[0].naturalWidth;
      var height=$("input#browse-input-file")[0].naturalHeight;      
      $("#dimensions").html(width+"X"+height);
      var size=$("input#browse-input-file")[0].size;
      $("#file_size").html(size+"KB")
      $(".file_details").show();
    }
    else {
      $("#message_modal").modal()
    }
    if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
        $('#image_upload').attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
    }
  }
});