// static/script.js

$(document).ready(function () {
    $("#ajaxButton").click(function () {
        var name = prompt("Enter your name:");
        if (name !== null && name !== "") {
            $.ajax({
                type: "POST",
                contentType: "application/json;charset=UTF-8",
                url: "/ajax",
                data: JSON.stringify({ name: name }),
                success: function (response) {
                    $("#result").text(response.message);
                    $("#catImage").attr("src", response.cat_url);
                    $("#catImage").show();
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
    });
});
