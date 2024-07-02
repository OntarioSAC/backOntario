document.addEventListener('DOMContentLoaded', function() {
    const proyectoSelect = document.getElementById('id_id_proyecto');
    const manzanaSelect = document.getElementById('id_id_manzana');

    proyectoSelect.addEventListener('change', function() {
        const proyectoId = this.value;

        if (!proyectoId) {
            manzanaSelect.innerHTML = '<option value="">---------</option>';
            return;
        }

        fetch(`/api/manzanas/${proyectoId}/`)
            .then(response => response.json())
            .then(data => {
                manzanaSelect.innerHTML = '<option value="">---------</option>';
                data.forEach(manzana => {
                    const option = document.createElement('option');
                    option.value = manzana.id_manzana;
                    option.textContent = manzana.nombre_manzana;
                    manzanaSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching manzanas:', error));
    });
});
