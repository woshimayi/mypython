const searchInput = document.getElementById('searchInput');
const tableBody = document.querySelector('tbody');

searchInput.addEventListener('input', filterTable);

function filterTable() {
    const searchTerm = searchInput.value.toLowerCase();
    const rows = tableBody.querySelectorAll('tr');

    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        let foundMatch = false;

        cells.forEach(cell => {
            const cellText = cell.textContent.toLowerCase();
            if (cellText.includes(searchTerm)) {
                foundMatch = true;
                break;
            }
        });

        if (foundMatch) {
            row.style.display = 'table-row';
        } else {
            row.style.display = 'none';
        }
    });
}
