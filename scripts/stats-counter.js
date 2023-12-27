let counts = setInterval(updated);
let upto = 0;
function updated() {
    let count = document.getElementById("counter-brands");
    count.innerHTML = ++upto;
    if (upto === 105) {
        clearInterval(counts);
    }
}

let counts2 = setInterval(updated2);
let upto2 = 0;
function updated2() {
    let count2 = document.getElementById("counter-products");
    count2.innerHTML = ++upto2;
    if (upto2 === 698) {
        clearInterval(counts2);
    }
}
