// API service for dashboard frontend
// Handles all requests to the Python backend

const API_BASE_URL = "http://localhost:8000"; // Change if backend runs elsewhere

// Fetch dashboard summary data (total sales, revenue, cash, profit) with optional date filter
export async function fetchDashboardData(from, to) {
  let url = `${API_BASE_URL}/api/dashboard/summary`;
  if (from || to) {
    const params = [];
    if (from) params.push(`from=${from}`);
    if (to) params.push(`to=${to}`);
    url += `?${params.join("&")}`;
  }
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error("Failed to fetch dashboard data");
    return await res.json();
  } catch (err) {
    console.error(err);
    return {
      totalSales: "-",
      totalRevenue: "-",
      currentCash: "-",
      projectedProfit: "-",
    };
  }
}

// Fetch recent transactions with optional date filter
export async function fetchTransactions(from, to) {
  let url = `${API_BASE_URL}/api/transactions/recent`;
  if (from || to) {
    const params = [];
    if (from) params.push(`from=${from}`);
    if (to) params.push(`to=${to}`);
    url += `?${params.join("&")}`;
  }
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error("Failed to fetch transactions");
    return await res.json();
  } catch (err) {
    console.error(err);
    return [];
  }
}

// SUPPLY STOCK API
export async function fetchSupplies() {
  try {
    const res = await fetch(`${API_BASE_URL}/api/supplies`);
    if (!res.ok) throw new Error("Failed to fetch supplies");
    return await res.json();
  } catch (err) {
    console.error(err);
    return [];
  }
}

export async function updateSupplyStock(supplyID, newAmount) {
  try {
    const res = await fetch(`${API_BASE_URL}/api/supplies/update`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ supplyID, newAmount }),
    });
    return await res.json();
  } catch (err) {
    console.error(err);
    return { success: false };
  }
}

export async function fetchSupplyWarnings() {
  try {
    const res = await fetch(`${API_BASE_URL}/api/supplies/warnings`);
    if (!res.ok) throw new Error("Failed to fetch warnings");
    return await res.json();
  } catch (err) {
    console.error(err);
    return [];
  }
}

export async function fetchShoppingSuggestions() {
  try {
    const res = await fetch(
      `${API_BASE_URL}/api/supplies/shopping_suggestions`
    );
    if (!res.ok) throw new Error("Failed to fetch suggestions");
    return await res.json();
  } catch (err) {
    console.error(err);
    return [];
  }
}

// MANUAL SALE API
export async function fetchProducts() {
  try {
    const res = await fetch(`${API_BASE_URL}/api/products`);
    if (!res.ok) throw new Error("Failed to fetch products");
    return await res.json();
  } catch (err) {
    console.error(err);
    return [];
  }
}

export async function submitSale({ date, sales, total }) {
  try {
    const res = await fetch(`${API_BASE_URL}/api/sales`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ date, sales, total }),
    });
    return await res.json();
  } catch (err) {
    console.error(err);
    return { success: false };
  }
}

// MANUAL EXPENSE API
export async function submitExpense({ date, desc, amount }) {
  try {
    const res = await fetch(`${API_BASE_URL}/api/expenses`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ date, desc, amount }),
    });
    return await res.json();
  } catch (err) {
    console.error(err);
    return { success: false };
  }
}

// PRODUCTS API
export async function fetchProducts() {
  try {
    const res = await fetch(`${API_BASE_URL}/api/products`);
    if (!res.ok) throw new Error("Failed to fetch products");
    return await res.json();
  } catch (err) {
    console.error(err);
    return [];
  }
}

export async function updateProductStock(productID, newAmount) {
  try {
    const res = await fetch(`${API_BASE_URL}/api/products/update`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ productID, newAmount }),
    });
    return await res.json();
  } catch (err) {
    console.error(err);
    return { success: false };
  }
}

export async function addProduct({ name, stock }) {
  try {
    const res = await fetch(`${API_BASE_URL}/api/products`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, stock }),
    });
    return await res.json();
  } catch (err) {
    console.error(err);
    return { success: false };
  }
}

// SUPPLIES API
export async function addSupply({ name, unit, stock }) {
  try {
    const res = await fetch(`${API_BASE_URL}/api/supplies`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, unit, stock }),
    });
    return await res.json();
  } catch (err) {
    console.error(err);
    return { success: false };
  }
}
