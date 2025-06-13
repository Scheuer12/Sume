// API service for dashboard frontend
// Handles all requests to the Python backend

const API_BASE_URL = 'http://localhost:8000'; // Change if backend runs elsewhere

// Fetch dashboard summary data (total sales, revenue, cash, profit)
export async function fetchDashboardData() {
    try {
        const res = await fetch(`${API_BASE_URL}/api/dashboard/summary`);
        if (!res.ok) throw new Error('Failed to fetch dashboard data');
        return await res.json();
    } catch (err) {
        console.error(err);
        return {
            totalSales: '-',
            totalRevenue: '-',
            currentCash: '-',
            projectedProfit: '-'
        };
    }
}

// Fetch recent transactions
export async function fetchTransactions() {
    try {
        const res = await fetch(`${API_BASE_URL}/api/transactions/recent`);
        if (!res.ok) throw new Error('Failed to fetch transactions');
        return await res.json();
    } catch (err) {
        console.error(err);
        return [];
    }
}
