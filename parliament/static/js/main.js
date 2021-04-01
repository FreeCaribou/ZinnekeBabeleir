$(document).ready(function () {

  $("#dropdown-change-language").change(function (e) {
    console.log($("#dropdown-change-language option:selected").val());

    $("#button-change-language").click()
  })

});

