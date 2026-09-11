# Database notes

The model connects daily sales to the products sold and the supplies used to make them. This document describes the SQL files currently in the repository; it is not a migration or a verified installation guide.

## Tables

The names below follow [data/financecontrol.sql](../data/financecontrol.sql).

| Table | Key | Purpose |
|---|---|---|
| `products` | `ProductId` | Product name, price, cost, internal identifier, and available quantity |
| `supplies` | `supplyID` | Supply name, unit of measure, available quantity, and purchasing fields |
| `suppliers` | `idSuppliers` | Supplier details and status |
| `sales` | `idSalesDay` | Date, sales data stored as JSON, and sales value |
| `suppliesbyproduct` | No primary key declared | Recipe entries connecting a product to a supply and quantity |

## Recipe relationships

`suppliesbyproduct.productFK` references `products.ProductId`. `suppliesbyproduct.supplyFK` references `supplies.supplyID`. The `qty` column records the quantity for that recipe entry.

Both foreign keys are declared in the SQL exports. The relationship table has indexes, but no unique constraint on the product/supply pair. Repeated entries are therefore possible and need an explicit rule before stock deductions are reliable.

Supplier records are present, but neither export declares a foreign key linking suppliers to supplies.

## Sales and quantities

`salesData` is a JSON field rather than a separate sales-line table. The current Python analysis reads product names and amounts from that payload. Product references inside it are not enforced by a database foreign key.

Recipe quantities and stock fields use integers in these exports. Fractional quantities and conversions between units need a defined policy. Prices and costs also use integers; the monetary unit should be made explicit and consistent before financial calculations are validated.

## Schema versions and gaps

| Detail | `data/Sume.sql` | `data/financecontrol.sql` |
|---|---|---|
| Naming | Qualified names such as `FinanceControl.Products` | Lowercase table names such as `products` |
| Product stock | No `availableAmount` column on products | Includes `availableAmount` |
| Sales value | No `salesValue` column | Includes `salesValue` |
| Recipe link | `suppliesByProduct` | `suppliesbyproduct` |
| Financial transactions | No expense or transaction table declared | No expense or transaction table declared |

The backend uses the `financecontrol` database and lowercase table names. The exports need to be reconciled into one maintained schema before documenting a reproducible setup. Table and database name casing should be checked on the target MySQL installation.

Neither export defines the complete financial model suggested by the API routes. The presence of expense and balance routes should not be read as evidence that the corresponding storage is ready.

## Follow-up work

1. Choose a canonical schema and add migrations.
2. Define recipe uniqueness, units, monetary representation, and sales-line structure.
3. Align the backend queries and transaction handling with that schema.
4. Provide a small, explicitly synthetic dataset and verify the sales-to-stock flow.

[Back to the project](../README.md)
