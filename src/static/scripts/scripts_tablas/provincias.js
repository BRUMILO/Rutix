document.addEventListener('DOMContentLoaded', function() {
    const buscador = document.getElementById('buscadorProvincia');
    const tabla = document.getElementById('tablaProvincias');
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

    $('#modalEditarProvincia').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var provinciaId = button.data('id');
        var provinciaNombre = button.data('nombre');
        
        var modal = $(this);
        modal.find('#edit_provincia_id').val(provinciaId);
        modal.find('#nuevo_nombre_provincia').val(provinciaNombre);
    });
});