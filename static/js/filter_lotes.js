document.addEventListener('DOMContentLoaded', function() {
    const manzanaSelect = document.getElementById('id_id_manzana');
    const loteSelect = document.getElementById('id_id_lote');

    manzanaSelect.addEventListener('change', function() {
        const manzanaId = this.value;

        if (!manzanaId) {
            loteSelect.innerHTML = '<option value="">---------</option>';
            return;
        }

        fetch(`/api/lotes/${manzanaId}/`)
            .then(response => response.json())
            .then(data => {
                loteSelect.innerHTML = '<option value="">---------</option>';
                data.forEach(lote => {
                    const option = document.createElement('option');
                    option.value = lote.id_lote;
                    option.textContent = `Lote ${lote.numero_lote}`;
                    loteSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching lotes:', error));
    });
});
