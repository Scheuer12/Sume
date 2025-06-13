// Dashboard main entry point
// This file initializes the dashboard and fetches data from the backend API
import { fetchDashboardData, fetchTransactions } from '../services/api.js';
import { renderDashboard, renderTransactionsTable } from '../components/dashboard.js';

// Main function to initialize dashboard
document.addEventListener('DOMContentLoaded', async () => {
    // Fetch dashboard summary data
    const dashboardData = await fetchDashboardData();
    renderDashboard(dashboardData);

    // Fetch recent transactions
    const transactions = await fetchTransactions();
    renderTransactionsTable(transactions);
});
