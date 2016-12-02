var music = new Audio("music.mp3");
music.loop = true;

var myEvents = {
    ".the-end": {
      init: function($slide) {
        $("button.show", $slide).click(function() {
            var $div = $("#terminal", $slide);
            animate($div);
        });
        $("button.stop", $slide).click(function() {
            music.pause();
        });
      },
    }
}

function animate($div) {
    console.debug("show");
    $div.fadeIn();
    music.play();
}
