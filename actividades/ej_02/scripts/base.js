document.addEventListener('DOMContentLoaded', () => {
    const fechaElemento = document.getElementById('fecha');
    const fechaActual = new Date(document.lastModified);
    const opcionesFecha = { year: 'numeric', month: 'long', day: 'numeric' };
    fechaElemento.textContent = fechaActual.toLocaleDateString('es-ES', opcionesFecha);
});

function controlLED(ledId) {
    fetch(`/led/toggle/${ledId}`);
}

function controlRGB() {
    const r = document.getElementById("redRange").value;
    const g = document.getElementById("greenRange").value;
    const b = document.getElementById("blueRange").value;

    fetch(`/rgbled/change/${r}/${g}/${b}`);
}
