
// document.onreadystatechange = function () {
//     var loading = document.getElementById("loading");
//     if (document.readyState !== "complete") {
//         loading.style.display = "block";
//     } else {
//         loading.style.display = "none";
//     }
// };


var myVar;



function myFunction() {

  myVar = setTimeout(showPage, 3000);

}



function showPage() {

  document.getElementById("loader").style.display = "none";

  document.getElementById("myDiv").style.display = "block";

}