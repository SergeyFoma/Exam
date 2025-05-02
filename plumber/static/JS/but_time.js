
function printMessage() { 
    alert("Время вышло!");
    //window.location.replace("http://127.0.0.1:8000/answer/");   
    document.getElementById('button').click();
    }
    setTimeout(printMessage, {{que.count}}000+5000);
    //button.onclick=printMessage

