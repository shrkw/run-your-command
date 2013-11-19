$(function() {
  $("#start").click(function() {
    $("div.input-warning").hide(0);
    $("pre#stdout").text("");
    $("pre#stderr").text("");
    var name = $("input#dvd_name").val();
    if (name == "") {
      $("div.input-warning").fadeIn();
      return;
    }
    $("#ripping-now").fadeIn("slow");
    $.post("/run?name=" + name, function(data) {
        $("#ripping-now").hide();
        $("pre#stdout").text(data.Result.out);
        $("pre#stderr").text(data.Result.err);
    });
  });
});
