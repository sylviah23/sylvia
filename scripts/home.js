let userValue = "AG CARE";

function selectBrand(event) {
    var userValue = event.target.value;
    var userValue = userValue.toUpperCase();
}

function runEnter() {

    var bra = document.getElementById('brandSelect').value;
    bra = bra.toUpperCase();

    localStorage.setItem("input", bra);
    window.location.href="products.html"
};