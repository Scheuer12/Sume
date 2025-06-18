// Dashboard main entry point
// This file initializes the dashboard and fetches data from the backend API
import { fetchDashboardData, fetchTransactions } from "../services/api.js";
import {
  renderDashboard,
  renderTransactionsTable,
} from "../components/dashboard.js";

function getFilterParams() {
  const from = document.getElementById("filter-from").value;
  const to = document.getElementById("filter-to").value;
  return { from, to };
}

// Main function to initialize dashboard
async function initDashboard() {
  // Fetch dashboard summary data with filter
  const { from, to } = getFilterParams();
  const dashboardData = await fetchDashboardData(from, to);
  renderDashboard(dashboardData);

  // Fetch recent transactions with filter
  const transactions = await fetchTransactions(from, to);
  renderTransactionsTable(transactions);
}

document.addEventListener("DOMContentLoaded", () => {
  // Filtering
  const filterForm = document.getElementById("dashboard-filter-form");
  if (filterForm) {
    filterForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      await initDashboard();
    });
  }
  // Card click navigation
  document.querySelectorAll(".dashboard-cards .card").forEach((card) => {
    card.addEventListener("click", () => {
      const link = card.getAttribute("data-link");
      if (link) window.location.href = link;
    });
  });
  // Initial load
  initDashboard();
});
