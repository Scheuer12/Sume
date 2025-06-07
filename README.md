# Shaman

# 🧾 Finance & Supply Management System

This project is a full-stack, real-world-oriented and actual-demand-originated system for **finance and inventory management**, built with clean database modeling and scalable architecture. It's designed for small businesses (especially in food/production sectors) that need to track sales, supplies (ingredients), and associated costs efficiently with 1 - 5 workers on the compaany only.

> Important Note: As this project was designed both as a usable tool and a technical showcase or fullstach skills, python API readiness aand relational modeling, I chose to build it using JavaScript instead of Streamlit or Jinja, even though this first release is simple enough to be built in such a simpler way.

---

## 🎯 Purpose

- Track products and their associated supplies (recipes).
- Automatically update stock levels of products and raw materials after each sales day.
- Store daily sales data (initially from OCR of printed receipts).
- Provide cash flow simple management and a good level of data on dashboards for financial management.
- Showcase full understanding of SQL-based architecture and backend development practices.

---

## 🧠 Tech Stack & Concepts

| Layer        | Technology / Concept      | Description                                         |
|--------------|---------------------------|-----------------------------------------------------|
| 💾 Database   | MySQL + MySQL Workbench   | Visual and relational modeling with foreign keys    |
| 🧱 Modeling   | Normalized schema         | Use of junction tables for many-to-many and one-to-many relations   |
| 🔐 Integrity  | Foreign Keys              | Enforced referential integrity at the DB level      |
| 📊 Reporting  | SQL JOIN-ready structure  | Prepared for dashboards and aggregations            |
| 🧠 Backend    | (Planned) FastAPI + SQLAlchemy | Future API and ORM support                         |
| 🧾 OCR Layer  | (Planned) pytest + Cypress + GitHub Actions | Automatic testings for each commit and pull request after the software is ready   |

---

## 🧱 Database Overview

The database is built with normalized relationships and structured for extensibility. It includes:

- Products
- Supplies
- Product recipes (junction table)
- Daily Sales
- Financial transactions

> 📘 For a complete breakdown of tables, fields, and relationships, see  
> [`docs/DB_SCHEMA.md`](docs/DB_SCHEMA.md)

---

## 🚀 Roadmap

- [x] Core entity modeling (products, supplies, recipes)
- [ ] Stock deduction and simple metrics calculation background
- [ ] OCR pipeline for importing sales data
- [ ] Sales and transaction models
- [ ] Backend individual autotesters
- [ ] Financial dashboard (sales, costs, margins)
- [ ] Frontend UI
- [ ] End-to-end auto testers
- [ ] GitHub Actions for test runs on every next pull request on main branch

---

## 📂 Planned Code Structure

/backend
└── app/
├── models/
├── routers/
├── schemas/
└── main.py
/frontend
└── src/
├── components/
├── pages/
├── services/
└── App.jsx
/data
└── DB_SCHEMA.md

---

## 🧪 How to Use

1. Clone this repository.
2. Open the `.mwb` file in MySQL Workbench (or use the provided SQL script).
3. Forward engineer to your local MySQL server.
4. (Planned) Run .exe to access the interface.

[Installer Assistant planned for a soon future]

---

## 📜 License

This project is public and open for educational or professional use.  
Feel free to contribute, fork, or adapt with attribution.

---

## 👤 Author

**Carlos Scheuer**  
Dev by heart, senior process maanaager and founder of [Epyatis](https://www.linkedin.com/in/carlosscheuer/) — dedicated to improving organizational performance and creating technology that delivers real business results.


