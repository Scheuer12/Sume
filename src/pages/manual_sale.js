// Manual Sale Entry Page
import { fetchProducts, submitSale } from "../services/api.js";

function addProductRow(products) {
  const row = document.createElement("div");
  row.className = "sale-row";
  row.innerHTML = `
    <select class="product-select">${products
      .map((p) => `<option value="${p.ProductId}">${p.ProductName}</option>`)
      .join("")}</select>
    <input type="number" min="1" class="product-qty" value="1" style="width:70px;">
    <button type="button" class="remove-row">Remove</button>
  `;
  row.querySelector(".remove-row").onclick = () => row.remove();
  return row;
}

async function renderSaleForm() {
  const main = document.getElementById("main-content");
  const products = await fetchProducts();
  let html = `<form id="sale-form" class="form-modern">
    <label>Date:
      <input type="date" name="date" required value="${new Date()
        .toISOString()
        .slice(0, 10)}">
    </label>
    <div id="sale-products"></div>
    <button type="button" id="add-product">Add Product</button>
    <label>Total Value (R$):
      <input type="number" name="total" min="0" step="0.01" required placeholder="e.g. 25.00">
    </label>
    <button type="submit">Submit Sale</button>
    <div id="sale-msg"></div>
  </form>`;
  main.innerHTML = html;
  const saleProducts = document.getElementById("sale-products");
  const addBtn = document.getElementById("add-product");
  addBtn.onclick = () => saleProducts.appendChild(addProductRow(products));
  // Add one row by default
  saleProducts.appendChild(addProductRow(products));
  document.getElementById("sale-form").onsubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const date = form.date.value;
    // Convert to cents for backend
    const total = Math.round(
      parseFloat(form.total.value.replace(",", ".")) * 100
    );
    const sales = Array.from(saleProducts.children).map((row) => {
      return [
        row.querySelector(".product-select").selectedOptions[0].text,
        parseInt(row.querySelector(".product-qty").value),
      ];
    });
    const res = await submitSale({ date, sales, total });
    document.getElementById("sale-msg").textContent = res.success
      ? "Sale submitted!"
      : "Error submitting sale.";
    if (res.success) form.reset();
  };
}
document.addEventListener("DOMContentLoaded", renderSaleForm);
