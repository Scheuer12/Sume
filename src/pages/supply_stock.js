// Supply Stock Management Page
import {
  fetchSupplies,
  updateSupplyStock,
  fetchSupplyWarnings,
  fetchShoppingSuggestions,
  fetchProducts,
  updateProductStock,
  addProduct,
  addSupply,
} from "../services/api.js";

function renderSuppliesTable(supplies) {
  const main = document.getElementById("main-content");
  if (!supplies || supplies.length === 0) {
    main.innerHTML = "<p>No supplies found.</p>";
    return;
  }
  let html = `<h2 class="section-title">Current Stock</h2><table class="supply-table">
    <thead><tr><th>Name</th><th>Available</th><th>Unit</th><th>Update</th></tr></thead><tbody>`;
  for (const s of supplies) {
    html += `<tr>
      <td>${s.supplyName}</td>
      <td><input type="number" min="0" value="${s.availableAmount}" data-id="${
      s.supplyID
    }" class="supply-amount-input"></td>
      <td>${s.unit || ""}</td>
      <td><button class="update-supply-btn" data-id="${
        s.supplyID
      }">Update</button></td>
    </tr>`;
  }
  html += '</tbody></table><div id="supply-update-msg"></div>';
  main.innerHTML = html;
  document.querySelectorAll(".update-supply-btn").forEach((btn) => {
    btn.onclick = async () => {
      const id = btn.getAttribute("data-id");
      const val = document.querySelector(`input[data-id='${id}']`).value;
      const res = await updateSupplyStock(id, val);
      document.getElementById("supply-update-msg").textContent = res.success
        ? "Updated!"
        : "Error updating.";
    };
  });
}

function renderProductsTable(products) {
  const main = document.getElementById("main-content");
  let html = `<h2 class="section-title">Products</h2><table class="supply-table">
    <thead><tr><th>Name</th><th>Stock</th><th>Update</th></tr></thead><tbody>`;
  for (const p of products) {
    html += `<tr>
      <td>${p.ProductName}</td>
      <td><input type="number" min="0" value="${p.availableAmount}" data-id="${p.ProductId}" class="supply-amount-input"></td>
      <td><button class="update-product-btn" data-id="${p.ProductId}">Update</button></td>
    </tr>`;
  }
  html += '</tbody></table><div id="product-update-msg"></div>';
  main.insertAdjacentHTML("beforeend", html);
  document.querySelectorAll(".update-product-btn").forEach((btn) => {
    btn.onclick = async () => {
      const id = btn.getAttribute("data-id");
      const val = document.querySelector(`input[data-id='${id}']`).value;
      const res = await updateProductStock(id, val);
      document.getElementById("product-update-msg").textContent = res.success
        ? "Updated!"
        : "Error updating.";
    };
  });
}

function renderAddProductForm() {
  const main = document.getElementById("main-content");
  let html = `<form id="add-product-form" class="form-modern">
    <h3>Add New Product</h3>
    <label>Name: <input type="text" name="name" required></label>
    <label>Initial Stock: <input type="number" name="stock" min="0" required></label>
    <button type="submit">Add Product</button>
    <div id="add-product-msg"></div>
  </form>`;
  main.insertAdjacentHTML("beforeend", html);
  document.getElementById("add-product-form").onsubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const name = form.name.value;
    const stock = form.stock.value;
    const res = await addProduct({ name, stock });
    document.getElementById("add-product-msg").textContent = res.success
      ? "Product added!"
      : "Error adding product.";
    if (res.success) form.reset();
  };
}

function renderAddSupplyForm() {
  const main = document.getElementById("main-content");
  let html = `<form id="add-supply-form" class="form-modern">
    <h3>Add New Supply</h3>
    <label>Name: <input type="text" name="name" required></label>
    <label>Unit: <input type="text" name="unit" required></label>
    <label>Initial Stock: <input type="number" name="stock" min="0" required></label>
    <button type="submit">Add Supply</button>
    <div id="add-supply-msg"></div>
  </form>`;
  main.insertAdjacentHTML("beforeend", html);
  document.getElementById("add-supply-form").onsubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const name = form.name.value;
    const unit = form.unit.value;
    const stock = form.stock.value;
    const res = await addSupply({ name, unit, stock });
    document.getElementById("add-supply-msg").textContent = res.success
      ? "Supply added!"
      : "Error adding supply.";
    if (res.success) form.reset();
  };
}

function renderWarnings(warnings) {
  const main = document.getElementById("main-content");
  if (warnings && warnings.length > 0) {
    let html = '<div class="supply-warning"><b>Low Stock:</b> ';
    html += warnings.map((w) => `${w[0]} (${w[1]})`).join(", ");
    html += "</div>";
    main.insertAdjacentHTML("afterbegin", html);
  }
}

function renderShoppingSuggestions(suggestions) {
  const main = document.getElementById("main-content");
  if (suggestions && suggestions.length > 0) {
    let html =
      '<div class="shopping-suggestions"><b>Shopping Suggestions:</b><ul>';
    for (const s of suggestions) {
      html += `<li><span class="suggestion-name">${
        s.supplyName
      }</span>: <span class="suggestion-buy">Buy <b>${Math.ceil(
        s.suggested_purchase
      )}</b></span> <span class="suggestion-meta">(avg used: ${s.avg_monthly_used.toFixed(
        1
      )}, in stock: ${s.availableAmount})</span></li>`;
    }
    html += "</ul></div>";
    main.insertAdjacentHTML("beforeend", html);
  }
}

async function init() {
  const supplies = await fetchSupplies();
  renderSuppliesTable(supplies);
  const warnings = await fetchSupplyWarnings();
  renderWarnings(warnings);
  const suggestions = await fetchShoppingSuggestions();
  renderShoppingSuggestions(suggestions);
  const products = await fetchProducts();
  renderProductsTable(products);
  renderAddProductForm();
  renderAddSupplyForm();
}

document.addEventListener("DOMContentLoaded", init);
