document.addEventListener('DOMContentLoaded', function() {
    const buscador = document.getElementById('buscadorProvincia');
    const tabla = document.getElementById('tablaCiudades');
    buscador.addEventListener('keyup', function() {
      const filtro = buscador.value.toLowerCase();
      const filas = tabla.getElementsByTagName('tr');
      for (let i = 1; i < filas.length; i++) {
        const provincia = filas[i].querySelector('.provincia-col');
        if (provincia) {
          const texto = provincia.textContent.toLowerCase();
          filas[i].style.display = texto.includes(filtro) ? '' : 'none';
        }
      }
    });

    $('#modalEditarCiudad').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var ciudadId = button.data('id');
        var ciudadNombre = button.data('nombre');
        var provinciaId = button.data('provincia-id');
        var costera = button.data('costera');
        
        var modal = $(this);
        modal.find('#edit_ciudad_id').val(ciudadId);
        modal.find('#nuevo_nombre_ciudad').val(ciudadNombre);
        modal.find('#nueva_provincia_id').val(provinciaId);
        modal.find('#nueva_costera').val(costera ? '1' : '0');
    });
});