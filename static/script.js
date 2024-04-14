function toggleInputFields() {
    var dataSource = document.getElementById('data_source').value;
    var fileInputFields = document.getElementById('file_input_fields');
    var keyboardInputFields = document.getElementById('keyboard_input_fields');

    if (dataSource === 'file') {
        fileInputFields.style.display = 'block';
        keyboardInputFields.style.display = 'none';
        document.getElementById('file_input').setAttribute('required', 'required');
    } else {
        fileInputFields.style.display = 'none';
        keyboardInputFields.style.display = 'block';
        document.getElementById('file_input').removeAttribute('required');
    }
}

document.getElementById('data_source').addEventListener('change', toggleInputFields);

toggleInputFields();

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
    var desmosIframe = document.getElementById("desmos-iframe");
    var equationUrl = "";

    if (equationType === "single") {
        if (equationValue === "1") {
            equationUrl = "https://www.desmos.com/calculator/eneau5xqiz?embed";
        } else if (equationValue === "2") {
            equationUrl = "https://www.desmos.com/calculator/4b1gzc0lmt?embed";
        } else if (equationValue === "3") {
            equationUrl = "https://www.desmos.com/calculator/v414nxrvce?embed";
        }
    } else if (equationType === "system") {
        var systemEquationValue = document.getElementById("system_equation").value;
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
