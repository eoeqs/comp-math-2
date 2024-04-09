function toggleEquationFields() {
    var equationType = document.getElementById("equation_type").value;
    var singleEquationFields = document.getElementById("single_equation_fields");
    var systemEquationFields = document.getElementById("system_equation_fields");

    if (equationType === "single") {
        singleEquationFields.style.display = "block";
        systemEquationFields.style.display = "none";
        // Устанавливаем required для полей одного уравнения
        document.getElementById("lower_limit").setAttribute("required", "required");
        document.getElementById("upper_limit").setAttribute("required", "required");
        document.getElementById("initial_guess").setAttribute("required", "required");
        document.getElementById("epsilon").setAttribute("required", "required");
        // Удаляем required для полей системы уравнений
        document.getElementById("system_initial_guess_x").removeAttribute("required");
        document.getElementById("system_initial_guess_y").removeAttribute("required");
    } else {
        singleEquationFields.style.display = "none";
        systemEquationFields.style.display = "block";
        // Устанавливаем required для полей системы уравнений
        document.getElementById("system_initial_guess_x").setAttribute("required", "required");
        document.getElementById("system_initial_guess_y").setAttribute("required", "required");
        // Удаляем required для полей одного уравнения
        document.getElementById("lower_limit").removeAttribute("required");
        document.getElementById("upper_limit").removeAttribute("required");
        document.getElementById("initial_guess").removeAttribute("required");
        document.getElementById("epsilon").removeAttribute("required");
    }
}

function handleSubmit(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    // Отправляем AJAX-запрос на сервер
    fetch('/solve', {
        method: 'POST',
        body: new FormData(document.getElementById('equationForm')), // Данные формы
    })
    .then(response => response.json()) // Преобразуем ответ в JSON
    .then(data => {
        if (data.error) {
            // Если есть ошибка, выводим её сообщение под формой
            document.getElementById('error-message').innerHTML = `<p class="error">${data.error}</p>`;
        } else {
            // Если нет ошибки, очищаем блок сообщений об ошибке
            document.getElementById('error-message').innerHTML = '';
            // Выводим результаты вычислений
            document.getElementById('result-container').innerHTML = `<h1>Results</h1><p>${data.result}</p><img src="/static/plot.png" alt="Graph of the Function">`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


document.getElementById('equationForm').addEventListener('submit', handleSubmit);