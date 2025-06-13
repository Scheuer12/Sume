-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 13, 2025 at 06:47 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `financecontrol`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `ProductId` int NOT NULL,
  `ProductName` varchar(255) NOT NULL,
  `ProductSalePrice` int DEFAULT NULL,
  `productInternalId` varchar(45) DEFAULT NULL,
  `productCost` int DEFAULT NULL,
  `availableAmount` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`ProductId`, `ProductName`, `ProductSalePrice`, `productInternalId`, `productCost`, `availableAmount`) VALUES
(1, 'Pão Francês', 100, 'P001', 0, 86),
(2, 'Bolo Chocolate', 1500, 'P002', 8, 25),
(3, 'Torta Frango', 2000, 'P003', 10, 68),
(4, 'Pão Integral', 200, 'P004', 1, 65),
(5, 'Coxinha', 600, 'P005', 3, 124),
(6, 'Pastel Carne', 700, 'P006', 3, 23),
(7, 'Pizza Mussarela', 3500, 'P007', 18, 146),
(8, 'Esfiha', 400, 'P008', 1, 60),
(9, 'Empadão', 2200, 'P009', 12, 62),
(10, 'Quiche', 1800, 'P010', 10, 131);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `idSalesDay` int NOT NULL,
  `dateSales` date NOT NULL,
  `salesData` json NOT NULL,
  `salesValue` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`idSalesDay`, `dateSales`, `salesData`, `salesValue`) VALUES
(1, '2025-06-01', '{\"Pão Francês\": 30, \"Bolo Chocolate\": 5}', 823),
(2, '2025-06-02', '{\"Coxinha\": 10, \"Torta Frango\": 2}', 959),
(3, '2025-06-03', '{\"Pastel Carne\": 8, \"Pão Integral\": 20}', 1827),
(4, '2025-06-04', '{\"Esfiha\": 10, \"Pizza Mussarela\": 3}', 1260),
(5, '2025-06-05', '{\"Quiche\": 2, \"Empadão\": 1}', 4817),
(6, '2025-06-06', '{\"Bolo Chocolate\": 10}', 1803),
(7, '2025-06-07', '{\"Pão Francês\": 40}', 3068),
(8, '2025-06-08', '{\"Esfiha\": 4, \"Coxinha\": 6}', 4928),
(9, '2025-06-09', '{\"Quiche\": 2}', 1435),
(10, '2025-06-10', '{\"Pastel Carne\": 6, \"Pizza Mussarela\": 2}', 892),
(11, '2025-06-11', '{\"Bolo Chocolate\": 3}', 4156),
(12, '2025-05-12', '{\"Pão Integral\": 25}', 4104),
(13, '2025-05-13', '{\"Torta Frango\": 3}', 3050),
(14, '2025-05-14', '{\"Quiche\": 1, \"Empadão\": 2}', 2439),
(15, '2025-05-15', '{\"Pizza Mussarela\": 4}', 2546),
(16, '2025-05-16', '{\"Esfiha\": 15}', 4914),
(17, '2025-04-17', '{\"Coxinha\": 7}', 2930),
(18, '2025-04-18', '{\"Pão Francês\": 50}', 3909),
(19, '2025-04-04', '{\"Pastel Carne\": 9}', 1252),
(20, '2025-04-20', '{\"Empadão\": 1, \"Bolo Chocolate\": 5}', 3035);

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `idSuppliers` int NOT NULL,
  `supplierName` mediumtext NOT NULL,
  `supplierCNPJ` varchar(255) NOT NULL,
  `supplierActive` tinyint DEFAULT NULL,
  `supplierStatus` enum('OK','Dívida','Aberto') DEFAULT NULL,
  `supplierBirth` datetime DEFAULT CURRENT_TIMESTAMP,
  `supplierLastActive` datetime DEFAULT NULL,
  `supplierObs` varchar(255) DEFAULT NULL,
  `Supplierscol` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`idSuppliers`, `supplierName`, `supplierCNPJ`, `supplierActive`, `supplierStatus`, `supplierBirth`, `supplierLastActive`, `supplierObs`, `Supplierscol`) VALUES
(1, 'Fornecedor A', '123456', 1, 'OK', '2025-06-09 11:48:47', '2025-06-01 12:00:00', 'Entrega pontual', NULL),
(2, 'Fornecedor B', '234567', 1, 'Aberto', '2025-06-09 11:48:47', '2025-05-20 15:45:00', 'Novo fornecedor', NULL),
(3, 'Fornecedor C', '345678', 0, 'Dívida', '2025-06-09 11:48:47', '2025-04-10 08:30:00', 'Pagamentos em atraso', NULL),
(4, 'Fornecedor D', '456789', 1, 'OK', '2025-06-09 11:48:47', '2025-06-01 10:00:00', 'Principal parceiro', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `supplies`
--

CREATE TABLE `supplies` (
  `supplyID` int NOT NULL,
  `supplyName` varchar(255) DEFAULT NULL,
  `supplyMeasure` varchar(255) DEFAULT NULL,
  `availableAmount` int DEFAULT NULL,
  `monthlyAmount` int DEFAULT NULL,
  `pricebyUnit` int DEFAULT NULL,
  `amountbyUnit` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `supplies`
--

INSERT INTO `supplies` (`supplyID`, `supplyName`, `supplyMeasure`, `availableAmount`, `monthlyAmount`, `pricebyUnit`, `amountbyUnit`) VALUES
(1, 'Farinha de Trigo', 'kg', 100, 40, 3, 1),
(2, 'Açúcar', 'kg', 80, 25, 3, 1),
(3, 'Ovos', 'dúzia', 50, 20, 6, 1),
(4, 'Leite', 'litro', 70, 30, 4, 1),
(5, 'Margarina', 'kg', 60, 25, 8, 1),
(6, 'Fermento Químico', 'g', 200, 100, 0, 5),
(7, 'Fermento Biológico', 'g', 100, 50, 0, 5),
(8, 'Chocolate em Pó', 'kg', 40, 15, 12, 1),
(9, 'Cacau', 'kg', 30, 10, 15, 1),
(10, 'Frango', 'kg', 100, 50, 12, 1),
(11, 'Tomate', 'kg', 80, 30, 4, 1),
(12, 'Cebola', 'kg', 90, 35, 4, 1),
(13, 'Alho', 'kg', 20, 10, 12, 1),
(14, 'Milho', 'kg', 60, 20, 5, 1),
(15, 'Presunto', 'kg', 40, 15, 18, 1),
(16, 'Queijo', 'kg', 60, 25, 22, 1),
(17, 'Orégano', 'g', 300, 100, 0, 1),
(18, 'Molho de Tomate', 'ml', 400, 150, 0, 10),
(19, 'Requeijão', 'kg', 50, 20, 20, 1),
(20, 'Papel Manteiga', 'metro', 100, 40, 1, 1),
(21, 'Água', 'litro', 500, 200, 1, 1),
(22, 'Sal', 'kg', 90, 30, 1, 1),
(23, 'Óleo', 'litro', 120, 40, 6, 1),
(24, 'Creme de Leite', 'ml', 300, 100, 2, 10),
(25, 'Essência Baunilha', 'ml', 100, 50, 1, 5),
(26, 'Páprica', 'g', 200, 70, 0, 1),
(27, 'Salsinha', 'g', 150, 50, 0, 1),
(28, 'Manjericão', 'g', 100, 40, 0, 1),
(29, 'Carne Moída', 'kg', 60, 20, 20, 1),
(30, 'Calabresa', 'kg', 70, 30, 18, 1),
(31, 'Batata', 'kg', 100, 50, 3, 1),
(32, 'Cenoura', 'kg', 90, 30, 3, 1),
(33, 'Chimichurri', 'g', 80, 25, 0, 1),
(34, 'Azeitona', 'g', 250, 100, 0, 1),
(35, 'Massa de Pizza', 'unidade', 120, 50, 2, 1),
(36, 'Farinha de Rosca', 'kg', 70, 20, 4, 1),
(37, 'Goiabada', 'kg', 30, 15, 10, 1),
(38, 'Doce de Leite', 'kg', 40, 15, 12, 1),
(39, 'Uva Passa', 'kg', 20, 10, 15, 1),
(40, 'Banana', 'kg', 60, 30, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `suppliesbyproduct`
--

CREATE TABLE `suppliesbyproduct` (
  `productFK` int NOT NULL,
  `qty` int DEFAULT NULL,
  `supplyFK` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `suppliesbyproduct`
--

INSERT INTO `suppliesbyproduct` (`productFK`, `qty`, `supplyFK`) VALUES
(1, 85, 19),
(1, 30, 15),
(1, 97, 13),
(1, 94, 14),
(2, 78, 25),
(2, 6, 18),
(2, 98, 11),
(2, 69, 10),
(2, 51, 14),
(3, 49, 11),
(3, 90, 9),
(3, 1, 22),
(3, 35, 22),
(4, 73, 18),
(4, 61, 16),
(4, 82, 21),
(5, 29, 11),
(5, 97, 25),
(5, 99, 10),
(6, 5, 7),
(6, 25, 16),
(6, 11, 13),
(7, 79, 13),
(7, 62, 19),
(7, 72, 9),
(7, 74, 22),
(8, 53, 18),
(8, 45, 17),
(8, 63, 24),
(9, 78, 8),
(9, 2, 15),
(9, 77, 10),
(9, 76, 15),
(10, 50, 22),
(10, 23, 21),
(10, 63, 13),
(10, 45, 14),
(10, 34, 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ProductId`),
  ADD UNIQUE KEY `ProductId_UNIQUE` (`ProductId`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`idSalesDay`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`idSuppliers`);

--
-- Indexes for table `supplies`
--
ALTER TABLE `supplies`
  ADD PRIMARY KEY (`supplyID`);

--
-- Indexes for table `suppliesbyproduct`
--
ALTER TABLE `suppliesbyproduct`
  ADD KEY `fk_suppliesByProduct_Supplies_idx` (`supplyFK`),
  ADD KEY `fk_suppliesByProduct_Products1_idx` (`productFK`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `ProductId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `idSuppliers` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `supplies`
--
ALTER TABLE `supplies`
  MODIFY `supplyID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `suppliesbyproduct`
--
ALTER TABLE `suppliesbyproduct`
  ADD CONSTRAINT `fk_suppliesByProduct_Products1` FOREIGN KEY (`productFK`) REFERENCES `products` (`ProductId`),
  ADD CONSTRAINT `fk_suppliesByProduct_Supplies` FOREIGN KEY (`supplyFK`) REFERENCES `supplies` (`supplyID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
