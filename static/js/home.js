$(document).ready(function (e) {
    // Aguardando ocorrer o submit no id: runModel
    $('#runModel').submit(function (event) {
        // Assim que ocorrer o submit, limpar a tag com id: hfResult
        $('#hfResult').empty();

        // Coleta dos valores do formulário.
        var age = $('#age').val();
        var sex = $('#sex').val();
        var cp = $('#cp').val();
        var trestbps = $('#trestbps').val();
        var chol = $('#chol').val();
        var fbs = $('#fbs').val();
        var restecg = $('#restecg').val();
        var thalach = $('#thalach').val();
        var exang = $('#exang').val();
        var oldpeak = $('#oldpeak').val();
        var slope = $('#slope').val();
        var ca = $('#ca').val();
        var thal = $('#thal').val();


        // Inserção dos valores em um objeto javascript
        var inputData = {
            'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal
        };

        // Requisição assincrona para o backend
        $.ajax({
            url: this.action,  // /main/api/run_model
            type: this.method, // POST
            data: inputData,
        })
        .done(function (response) { // Assim que feita a requisição assincrona e der sucesso, será executado o comando abaixo
            if(response.pred == 0) {
                $('#hfResult').append(`<p>The Pacient does not have a Heart Disease</p>`) // Retorno para o frontend se a "predict" for 0
            } else {
                $('#hfResult').append(`<p>The Pacient has Heart Disease</p>`) // Retorno para o frontend se a "predict" for 1
            }
        });
        // Cancela evento default de refresh de página
        event.preventDefault();
    });
});