header_elem = document.getElementById("header");

let change_color = async function() {
    header_elem.style.color = `rgb(${Math.random()*255}, ${Math.random()*255}, ${Math.random()*255})`
}

setInterval(change_color, 100);
