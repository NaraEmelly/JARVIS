const output = document.getElementById("output");
const startButton = document.getElementById("startButton");
const statusText = document.getElementById("status");

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = "pt-BR";
recognition.continuous = true;
recognition.interimResults = false;

startButton.addEventListener("click", () => {

    output.textContent = "";
    statusText.textContent = "Ouvindo...";

    recognition.start();
});

recognition.addEventListener("result", (event) => {

    const transcript = Array.from(event.results)
        .map(result => result[0].transcript)
        .join("");

    output.textContent = transcript;

});

recognition.addEventListener("end", () => {

    statusText.textContent = "Reconectando...";
    recognition.start();

});

recognition.addEventListener("start", () => {

    statusText.textContent = "🎤 Microfone ativo";

});

recognition.addEventListener("error", (event) => {

    statusText.textContent =
        "Erro: " + event.error;

});