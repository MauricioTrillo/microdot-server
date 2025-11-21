document.addEventListener('DOMContentLoaded', () => {
    const fechaElemento = document.getElementById('fecha');
    const fechaActual = new Date(document.lastModified);
    const opcionesFecha = { year: 'numeric', month: 'long', day: 'numeric' };
    fechaElemento.textContent = fechaActual.toLocaleDateString('es-ES', opcionesFecha);
});

async function readTemperature() {
    const resp = await fetchData('/sensors/ds18b20/read');
    const tempOut = document.getElementById("mostrar-temperatura");

    if (resp) {
        tempOut.innerText = resp.temperatura;
    } else {
        tempOut.innerText = "Error";
    }
}

async function sendSetpoint() {
    const val = Number(document.getElementById("setpoint-slider").value);
    const resp = await fetchData(`/setpoint/set/${val}`);
    const buz = document.getElementById("estado-buzzer");

    if (resp) {
        buz.innerText = resp.buzzer;
    } else {
        buz.innerText = "Error";
    }
}

function updateSetpointValue(v) {
    document.getElementById("setpoint-value").innerText = v;
    sendSetpoint();
}

setInterval(readTemperature, 1000);

readTemperature();
