
var RE = /col:md=(\d+)/;

var parse = function(text) {
    var m = RE.exec(text);
    if(m) {
        console.debug(m[1]);
    }
};

$(function() {
    $("a").each(function() {
        var text = $(this).text();
        parse(text);
    });
});
