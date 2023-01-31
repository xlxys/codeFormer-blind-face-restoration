
document.onreadystatechange = function () {
    var loading = document.getElementById("loading");
    if (document.readyState !== "complete") {
        loading.style.display = "block";
    } else {
        loading.style.display = "none";
    }
};
