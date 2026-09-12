# Sume

Finance and inventory management for small businesses. An early prototype built around a practical question: **what do today's sales mean for cash flow and tomorrow's stock?**

I started this project for a small-business use case, with a focus on products, recipes, supplies, and daily sales. It also gave me a place to work on relational modeling and the connection between a Python backend and a JavaScript interface.

**Status:** development prototype. The repository contains database models, backend modules, API routes, and interface pages. Several parts still need to be connected and validated before the application can run end to end.

## The problem

For a small food business, selling a product also consumes ingredients. Looking only at revenue misses part of the picture: which supplies were used, what remains in stock, and what needs to be purchased next.

Sume brings those pieces into one model:

- Products and the supplies required to make them.
- Daily sales and their effect on inventory.
- Supply usage and purchasing suggestions.
- Expenses and a financial dashboard.

## What's in the repository

| Area | Implementation | Current state |
|---|---|---|
| Database | MySQL, SQL exports, and a Workbench model | Products, supplies, suppliers, sales, and recipe relationships |
| Backend | Python, FastAPI, and pyodbc | API routes and modules for sales, supplies, and balances; integration is incomplete |
| Interface | JavaScript, HTML, and CSS | Dashboard, manual sales, expenses, and stock pages |
| Receipt import | OCR experiments | Early work; not a complete import pipeline |

Start with the [database notes](docs/DB_SCHEMA.md), [API entry point](backend/main.py), and [supply calculations](backend/supplymanager.py). The [frontend API service](src/services/api.js) shows how the pages are intended to communicate with the backend.

## Design choices

**Recipes as relationships.** A product can use several supplies, and the same supply can belong to several products. The `suppliesbyproduct` table connects them and stores the quantity needed for each recipe entry.

**Separate backend and interface.** I chose a JavaScript interface to work on API integration alongside the Python logic. A server-rendered interface would have been a smaller starting point, but building the connection was part of the project.

**Sales as an input to stock planning.** The supply module uses recorded sales and recipe quantities to estimate consumption and purchasing needs. These calculations still need integration tests before they can be relied on.

## Exploring the code

| Path | Contents |
|---|---|
| `backend/` | API entry point, database access, and business logic |
| `src/html/` | Interface pages |
| `src/pages/` | Page behavior |
| `src/services/` | HTTP calls to the backend |
| `src/styles/` | Interface styling |
| `data/` | SQL exports and the Workbench model |

The code currently expects a local MySQL database accessed through an ODBC driver. The connection settings are in `backend/database_handler.py`; the frontend API URL is in `src/services/api.js`.

There is no verified one-command setup yet. The product manager module is empty while the API imports functions from it, and some routes reference methods that are not implemented in the corresponding modules. Importing a database alone will not make this snapshot runnable.

The two SQL files also differ. See [schema versions and gaps](docs/DB_SCHEMA.md#schema-versions-and-gaps) before using either as a starting point.

## Verification

The current automated check covers the database insert path with test doubles, so it does not require a local MySQL instance or ODBC driver:

```bash
python -m unittest discover -s tests -v
```

This is a focused regression test, not an end-to-end application test.

## Next steps

- [ ] Complete the product module and align API routes with the backend methods.
- [ ] Reconcile the database exports and document the setup with sample data.
- [ ] Move connection settings into environment configuration and validate API inputs.
- [ ] Test sales recording, recipe-based stock deduction, and supply calculations.
- [ ] Connect and verify the interface flows.
- [ ] Expand automated checks when the first complete flow is working.

## Author

Carlos Scheuer — developer, process and project management professional, and founder of Epyatis.

[LinkedIn](https://www.linkedin.com/in/carlosscheuer/)

## License

[MIT](LICENSE).
