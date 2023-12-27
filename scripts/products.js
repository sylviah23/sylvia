let br = [];
let pr = [];
let ingre = [];
let li = [];

window.onload = function() {
    let userValue = localStorage.getItem("input");
    d3.csv("filtered.csv", function(data) {
        return {
            brand: data.Brand,
            product: data.Product,
            ingredients: data.Ingredients,
            link: data.Link
        }
    }).then(function(data) {
        for (var i = 0; i < data.length; i++) {
            br[i] = data[i].brand;
            ingre[i] = data[i].ingredients;
            pr[i] = data[i].product;
            li[i] = data[i].link;
        }
    })

    .then(function() {
        for (var i=0; i < br.length; i++) {
            if (br[i].toUpperCase() === userValue) {
                if (ingre[i] != "no ingredients") {
                    d3.select("tbody").insert("tr").html(
                        '<td class="td1">' + '<p style="font-size:25px;">' + (pr[i]) + '</p>' + '<p>' + li[i] + '</p>' + '</td>' +
                        '<td class="td2">' + (ingre[i]) + '</td>'
                    )				
                }
            }
        }
    });
    localStorage.clear();
}

let userValue = "AG Care"
function selectBrand(event) {
    userValue = event.target.value;
    userValue = userValue.toUpperCase();
}

function runEnter() {
    $("#outTable > tbody > tr").remove();
    for (var i=0; i < br.length; i++) {
        if (br[i].toUpperCase() === userValue) {
            if (ingre[i] != "no ingredients") {
                d3.select("tbody").insert("tr").html(
                    '<td class="td1">' + '<p style="font-size:25px;">' + (pr[i]) + '</p>' + '<p>' + li[i] + '</p>' + '</td>' +
                    '<td class="td2">' + (ingre[i]) + '</td>'
                )	
            }
        }
    }
};