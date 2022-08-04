header_elem = document.getElementById("header");

let change_color = async function() {
    header_elem.style.color = `rgb(${Math.random()*255}, ${Math.random()*255}, ${Math.random()*255})`
}

setInterval(change_color, 100);

//starts confetti
const start = () => {
    setTimeout(function(){
      confetti.start();
    }, 1000); //indicates time, so 1 second
  };

  //stops confetti
  const stop = () => {
    setTimeout(function(){
      confetti.stop()
    }, 5000) //indicates time, so 5 seconds
  }

  start();
  stop();