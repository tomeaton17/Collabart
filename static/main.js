var canvas, flag = false,
    currX = 0,
    currY = 0,
    prevX = 0,
    prevY = 0,
    dot_flag = false;
var x = "#0C0C0C",
    y = 20;

$(document).ready(function(){
    $("#slidecontainer").slider();
    var startPos = $("#slidecontainer").slider("value");

    $("#slidecontainer").on("slidestop", function(event, ui) {
            y = ui.value;
	});		

    $('.redbutton').click(function() {
	    x = "#ff0000";
    });
    $('.bluebutton').click(function() {
	    x = "#0000ff";
    });
    $('.greenbutton').click(function() {
	    x = "#008000";
    });
    $('.blackbutton').click(function() {
	    x = "#000000";
    });
    $('.eraser').click(function() {
	    x = "#ffffff";
    });
    canvas = document.getElementById('can');
    ctx = canvas.getContext("2d");
    w = canvas.width;
    h = canvas.height;

    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false); 
});



function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineCap = 'round';
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
}

function findxy(res, e) {
    if (res == 'down') {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        currY = e.clientY - canvas.offsetTop;

        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            dot_flag = false;
        }
    }
    if (res == 'up' || res == "out") {
        flag = false;
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            draw();
        }
    }
}
