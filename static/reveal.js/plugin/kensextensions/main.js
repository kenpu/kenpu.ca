(function () {
    function processCopyBtn($section) {
        if($section.is(".copybtned"))
            return;

        $section.addClass("copybtned");
        $("code.clipboard", $section).each(function() {
            var code = $(this);
            var btn = $('<button class="btn btn-sm">Copy</button>')
                .css({
                    position: "absolute",
                    right: 0,
                    top: 0,
                });
            code.after(btn);
            code.parent().css('position', 'relative');
            new Clipboard(btn[0], {
                text: function(trigger) {
                    return code.text();
                }
            });
        });
    }

    function processCmd($a) {
        var cmd = ($a.attr('href') || "").split();
        console.debug("cmd:", cmd);
        if(cmd[0].startsWith("comfort")) {
            console.debug("ding");
            $a.closest("ul,ol").children().css({
                marginBottom: 20,
            });
            $a.closest("li").detach();
        }
    }

    $(".slides section").each(function() {
        processCopyBtn($(this));
    });

    $(".slides section a").each(function() {
        var $a = $(this);
        if($a.text() == "!") {
            processCmd($a);
        }
    });
})();
