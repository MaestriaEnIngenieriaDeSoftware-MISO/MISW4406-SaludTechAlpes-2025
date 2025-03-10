window.addEventListener("DOMContentLoaded", () => {
    const messages = document.getElementById("mensajes");

    if (typeof(EventSource) !== "undefined") {
        var source = new EventSource("http://localhost:5002/stream");
        console.log(source); //deberia cambiar dependiendo de la ruta de la api

        source.onopen = function(event) {
            console.log("Connection to server opened.");
        };

        source.onerror = function(event) {
            if (event.readyState == EventSource.CLOSED) {
                console.log("Connection to server closed.");
            } else {
                console.log("Error occurred:", event);
            }
        };

        source.onmessage = function(event) {
            const message = document.createElement("li");
            const content = document.createTextNode(event.data);
            console.log("Message received:", event.data);
            message.appendChild(content);
            messages.appendChild(message);
        };
    } else {
        messages.innerHTML = "EventSource not supported by this browser.";
    }
});