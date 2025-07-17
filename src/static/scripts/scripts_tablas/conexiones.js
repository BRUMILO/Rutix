document.addEventListener('DOMContentLoaded', function() {
  const buscador = document.getElementById('buscadorConexion');
  const tabla = document.getElementById('tablaConexiones');
  buscador.addEventListener('keyup', function() {
    const filtro = buscador.value.toLowerCase();
    const filas = tabla.getElementsByTagName('tr');
    for (let i = 1; i < filas.length; i++) {
      const origen = filas[i].querySelector('.ciudad-origen-col');
      const destino = filas[i].querySelector('.ciudad-destino-col');
      let mostrar = false;
      if (origen && origen.textContent.toLowerCase().includes(filtro)) {
        mostrar = true;
      }
      if (destino && destino.textContent.toLowerCase().includes(filtro)) {
        mostrar = true;
      }
      filas[i].style.display = mostrar ? '' : 'none';
    }
  });

  $('#modalEditarConexion').on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget);
      var conexionId = button.data('id');
      var origenId = button.data('origen-id');
      var destinoId = button.data('destino-id');
      var distancia = button.data('distancia');
      
      var modal = $(this);
      modal.find('#edit_conexion_id').val(conexionId);
      modal.find('#nuevo_origen_id').val(origenId);
      modal.find('#nuevo_destino_id').val(destinoId);
      modal.find('#nueva_distancia').val(distancia);
  });
});