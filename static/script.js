window.addEventListener('DOMContentLoaded', (event) => {
    var singleEquationForm = document.getElementById('equationForm');
    var systemEquationsForm = document.getElementById('system_equations_form');

    singleEquationForm.addEventListener('change', function () {
        document.getElementById('equation_type_single').checked = true;
        document.getElementById('equation_type_system').checked = false;
        updateDesmos();
    });

    systemEquationsForm.addEventListener('change', function () {
        document.getElementById('equation_type_single').checked = false;
        document.getElementById('equation_type_system').checked = true;
        updateDesmos();
    });

    updateDesmos();
});

function updateDesmos() {
    var equationSelect = document.getElementById("equation");
    var singleEquationTypeField = document.getElementById("equation_type_single");
    var systemEquationTypeField = document.getElementById("equation_type_system");
    var equationType = singleEquationTypeField.checked ? singleEquationTypeField.value : systemEquationTypeField.value;
    var equationValue = equationSelect.options[equationSelect.selectedIndex].value;
    console.log("Equation Type:", equationType);
    var desmosIframe = document.getElementById("desmos-iframe");
    var equationUrl = "";

    if (equationType === "single") {
        if (equationValue === "1") {
            equationUrl = "https://www.desmos.com/calculator/eneau5xqiz?embed";
        } else if (equationValue === "2") {
            equationUrl = "https://www.desmos.com/calculator/4b1gzc0lmt?embed";
        } else if (equationValue === "3") {
            equationUrl = "https://www.desmos.com/calculator/xgctgmqybd?embed";
        }
    } else if (equationType === "system") {
        var systemEquationValue = document.getElementById("system_equation").value;
        console.log(systemEquationValue)
        if (systemEquationValue === "system1") {
            equationUrl = "https://www.desmos.com/calculator/qzspdezgar?embed";
        } else if (systemEquationValue === "system2") {
            equationUrl = "https://www.desmos.com/calculator/5ogtf2rvyb?embed";
        }
    }

    desmosIframe.src = equationUrl;
}

document.getElementById("equation_type_single").addEventListener("change", updateDesmos);
document.getElementById("equation_type_system").addEventListener("change", updateDesmos);
document.getElementById("system_equation").addEventListener("change", updateDesmos);
document.getElementById("equation").addEventListener("change", updateDesmos);
