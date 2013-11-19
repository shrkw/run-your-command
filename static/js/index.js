$(function() {
  $("#start").click(function() {
    var name = $("input#name").val();
    if (name == "") {
      $("div.input-warning").fadeIn();
      return;
    }
    $("div.input-warning").hide();
    $("div.alert-success").hide();
    $("pre#stdout").text("");
    $("pre#stderr").text("");
    $("#running-now").fadeIn("slow");
    $.post("/run?name=" + name, function(data) {
      $("#running-now").hide();
      $("div.alert-success").fadeIn("slow");

      $("pre#stdout").text(data.Result.out);
      $("pre#stderr").text(data.Result.err);
    });
  });
});
