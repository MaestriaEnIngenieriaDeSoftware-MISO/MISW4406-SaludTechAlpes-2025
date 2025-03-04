window.addEventListener("DOMContentLoaded", () => {
    const messages = document.getElementById("mensajes");

    if (typeof(EventSource) !== "undefined") {
        var source = new EventSource("/stream"); //deberia cambiar dependiendo de la ruta de la api
        source.onmessage = function(event) {
            const message = document.createElement("li");
            const content = document.createTextNode(event.data);
            message.appendChild(content);
            messages.appendChild(message);
        }
    } else {
        messages.innerHTML = "EventSource not supported by this browser.";
    }
});