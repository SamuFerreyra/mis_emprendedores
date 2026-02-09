let indiceActual = 0;
let listaImagenes = [];

// Esta función se ejecutará apenas cargue la página
function inicializarGaleria(imagenes) {
    listaImagenes = imagenes;
}

function seleccionar(url, elemento) {
    const imgPrincipal = document.getElementById('grande');
    if (!imgPrincipal) return;

    imgPrincipal.style.opacity = '0.3';

    setTimeout(() => {
        imgPrincipal.src = url;
        imgPrincipal.style.opacity = '1';
        indiceActual = listaImagenes.indexOf(url);

        // Limpiar estilos de las miniaturas
        document.querySelectorAll('.thumb').forEach(t => {
            t.style.border = "none";
            t.classList.remove('active');
        });

        if (elemento) {
            elemento.style.border = "2px solid #000";
            elemento.classList.add('active');
        }
    }, 150);
}

function cambiar(direccion) {
    if (listaImagenes.length <= 1) return;

    indiceActual += direccion;

    if (indiceActual >= listaImagenes.length) indiceActual = 0;
    if (indiceActual < 0) indiceActual = listaImagenes.length - 1;

    const nuevaUrl = listaImagenes[indiceActual];
    const todasLasThumbs = document.querySelectorAll('.thumb');

    seleccionar(nuevaUrl, todasLasThumbs[indiceActual]);
}