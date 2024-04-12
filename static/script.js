function updateDesmos() {
    var equationSelect = document.getElementById("equation");
    var equationValue = equationSelect.options[equationSelect.selectedIndex].value;
    var lowerLimit = parseFloat(document.getElementById("lower_limit").value);
    var upperLimit = parseFloat(document.getElementById("upper_limit").value);

    var desmosIframe = document.getElementById("desmos-iframe");
    var equationUrl = "";

    if (equationValue === "1") {
        equationUrl = "https://www.desmos.com/calculator/eneau5xqiz?embed";
    } else if (equationValue === "2") {
        equationUrl = "https://www.desmos.com/calculator/4b1gzc0lmt?embed";
    } else if (equationValue === "3") {
        equationUrl = "https://www.desmos.com/calculator/xgctgmqybd?embed";
    }

    desmosIframe.src = equationUrl;
}


