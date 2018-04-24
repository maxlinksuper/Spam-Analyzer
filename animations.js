$(document).ready(function () {

    $('.navigation__link').on('click', function () {
        $('.navigation__checkbox').prop('checked', false);
    });

    $('#kmp').on('click', function() {
        var strSplit;
        var spam = [];
        var command = 'kmp';
        var keywords = $('#inputcolumn').val();
        console.log(keywords);
        console.log(result);

        $.ajax({
            type: "POST",
            url: "./proc.php",
            data: {
                cmd: command,
                key: keywords,
                posts: result
            },
            success: function (response) {
                console.log(response);
                var re = JSON.parse(response);
                console.log(re);

                $('.default-box').each(function (i, obj) {
                    if (re[i] == false) {
                        $(this).attr('class', 'box-not-spam');
                    } else {
                        $(this).attr('class', 'box-spam');
                    }
                });
            }
        });
    });

    $('#bm').on('click', function() {
        var strSplit;
        var spam = [];
        var command = 'bm';
        var keywords = $('#inputcolumn').val();
        console.log(keywords);
        console.log(result);

        $.ajax({
            type: "POST",
            url: "./proc.php",
            data: {
                cmd: command,
                key: keywords,
                posts: result
            },
            success: function (response) {
                console.log(response);
                var re = JSON.parse(response);
                console.log(re);

                $('.default-box').each(function (i, obj) {
                    if (re[i] == false) {
                        $(this).attr('class', 'box-not-spam');
                    } else {
                        $(this).attr('class', 'box-spam');
                    }
                });
            }
        });
    });

    $('#regex').on('click', function() {
        var strSplit;
        var spam = [];
        var command = 'regex';
        var keywords = $('#inputcolumn').val();
        console.log(keywords);
        console.log(result);

        $.ajax({
            type: "POST",
            url: "./proc.php",
            data: {
                cmd: command,
                key: keywords,
                posts: result
            },
            success: function (response) {
                console.log(response);
                var re = JSON.parse(response);
                console.log(re);

                $('.default-box').each(function (i, obj) {
                    if (re[i] == false) {
                        $(this).attr('class', 'box-not-spam');
                    } else {
                        $(this).attr('class', 'box-spam');
                    }
                });
            }
        });
    });

});