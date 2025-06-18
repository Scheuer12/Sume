// Manual Expense Entry Page
import { submitExpense } from "../services/api.js";

function renderExpenseForm() {
  const main = document.getElementById("main-content");
  let html = `<form id="expense-form" class="form-modern">
    <label>Date:
      <input type="date" name="date" required value="${new Date()
        .toISOString()
        .slice(0, 10)}">
    </label>
    <label>Description:
      <input type="text" name="desc" required placeholder="e.g. Electricity bill, Supplies, ...">
    </label>
    <label>Amount (R$):
      <input type="number" name="amount" min="0" step="0.01" required placeholder="e.g. 12.00">
    </label>
    <button type="submit">Submit Expense</button>
    <div id="expense-msg"></div>
  </form>`;
  main.innerHTML = html;
  document.getElementById("expense-form").onsubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const date = form.date.value;
    const desc = form.desc.value;
    // Convert to cents for backend
    const amount = Math.round(
      parseFloat(form.amount.value.replace(",", ".")) * 100
    );
    const res = await submitExpense({ date, desc, amount });
    document.getElementById("expense-msg").textContent = res.success
      ? "Expense submitted!"
      : "Error submitting expense.";
    if (res.success) form.reset();
  };
}
document.addEventListener("DOMContentLoaded", renderExpenseForm);
