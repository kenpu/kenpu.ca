function say() {
    alert("Ding");
}
function say2() {
    alert("Dong");
}

var counter = 0;

var myEvents = {
    ".my-first-slide": {
      init: function($slide) {
        $('#click', $slide).click(function(e) {
            alert("Ding");
        });
      },
      once: function($slide) {
        alert("Bye, forever.");
      },
      enter: function($slide) {
                 $("#click", $slide).text("Click " + counter);
                 counter += 1;
             },
    },
};
