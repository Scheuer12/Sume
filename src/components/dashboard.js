// Dashboard rendering logic
// Renders summary cards and transactions table

// Render the summary cards with dashboard data
export function renderDashboard(data) {
    document.querySelector('#total-sales .value').textContent = data.totalSales ?? '-';
    document.querySelector('#total-revenue .value').textContent = data.totalRevenue ?? '-';
    document.querySelector('#current-cash .value').textContent = data.currentCash ?? '-';
    document.querySelector('#projected-profit .value').textContent = data.projectedProfit ?? '-';
}

// Render the transactions table
export function renderTransactionsTable(transactions) {
    const tbody = document.querySelector('#transactions-table tbody');
    tbody.innerHTML = '';
    if (!transactions || transactions.length === 0) {
        const tr = document.createElement('tr');
        const td = document.createElement('td');
        td.colSpan = 4;
        td.textContent = 'No transactions found.';
        tr.appendChild(td);
        tbody.appendChild(tr);
        return;
    }
    transactions.forEach(tx => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${tx.date || '-'}</td>
            <td>${tx.description || '-'}</td>
            <td>${tx.type || '-'}</td>
            <td>${tx.amount || '-'}</td>
        `;
        tbody.appendChild(tr);
    });
}
