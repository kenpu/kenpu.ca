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

    // [!](note)
    // Gets the previous sibling, and wrap $a parent
    // in a two column row with fixed ratio
    function processNote($a, ratio) {
        var noteWidth = ratio ? parseInt(ratio, 10) : 4;
        var mainWidth = 12 - noteWidth;
        // assume blockquote being the note container
        var note = $a.closest("blockquote");
        // default to the parent
        if(note.size() == 0) note = $a.parent();
        var sibling = note.prev();
        var row = $("<div>").addClass("row");
        var c1 = $("<div>").addClass("col-md-" + mainWidth).appendTo(row);
        var c2 = $("<div>").addClass("col-md-" + noteWidth).appendTo(row);
        note.after(row);
        note.detach().appendTo(c2);
        sibling.detach().appendTo(c1);
        note.css({
            fontSize: "85%",
            marginLeft: 20,
        });
    }

    function processCmd($a) {
        var cmd = ($a.attr('href') || "").split(/\s+/);
        // =========================================
        if(cmd[0].startsWith("comfort")) {
            $a.closest("ul,ol").children().css({
                marginBottom: 20,
            });
            $a.closest("li").detach();
        }
        // =========================================
        else if(cmd[0].startsWith("---")) {
            var n = cmd[0].length;
            $a.after($("<hr>").css({
                marginTop: 10*n,
                marginBottom: 10*n,
            }));
            $a.detach();
        }
        // =========================================
        else if(cmd[0] == "highlight") {
            var div = $("<div>").css({
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: 600,
                padding: 20,
            }).append("<div>");

            $a.closest("section").css({
                background: "#888",
                color: "white",
            }).wrapInner(div);
            $a.detach();
        }
        // =========================================
        else if(cmd[0] == "box") {
            $a.parent().css({
                border: "thin solid #aaa",
                padding: 20,
            });
            $a.detach();
        }
        // =========================================
        else if(cmd[0] == "note") {
            processNote($a, (cmd.length > 1) ? cmd[1] : "");
            $a.detach();
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
