-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: medical_store
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `ID` char(9) NOT NULL,
  `A_username` varchar(50) NOT NULL,
  `A_password` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('11','admin','password');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_id` int NOT NULL AUTO_INCREMENT,
  `C_Fname` varchar(20) NOT NULL,
  `C_Lname` varchar(20) DEFAULT NULL,
  `C_gender` enum('Male','Female') DEFAULT NULL,
  `C_phno` char(10) DEFAULT NULL,
  `C_Mail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cust_id`),
  CONSTRAINT `chk_cust_email` CHECK (regexp_like(`C_Mail`,_utf8mb4'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Safia','Malik','Female','9632587415','safia@gmail.com'),(2,'Varun','Ilango','Male','9987565423','varun@gmail.com'),(3,'Suja','Suresh','Female','7896541236','suja@hotmail.com'),(4,'Agatha','Elizabeth','Female','7845129635','agatha@gmail.com'),(5,'Zayed','Shah','Male','6789541235','zshah@hotmail.com'),(6,'Vijay','Kumar','Male','8996574123','vijayk@yahoo.com'),(7,'Meera','Das','Female','7845963259','meera@gmail.com'),(8,'ab','cd','Male','6393177536','abcd@gmail.com'),(9,'ef','gh','Male','6945678952','efgh@gmail.com');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `customer_view_page`
--

DROP TABLE IF EXISTS `customer_view_page`;
/*!50001 DROP VIEW IF EXISTS `customer_view_page`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `customer_view_page` AS SELECT 
 1 AS `cust_id`,
 1 AS `C_Fname`,
 1 AS `C_Lname`,
 1 AS `C_gender`,
 1 AS `C_phno`,
 1 AS `C_Mail`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `emp_login`
--

DROP TABLE IF EXISTS `emp_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_login` (
  `E_username` varchar(50) NOT NULL,
  `E_password` varchar(50) DEFAULT NULL,
  `E_ID` char(9) DEFAULT NULL,
  PRIMARY KEY (`E_username`),
  KEY `fk5` (`E_ID`),
  CONSTRAINT `fk5` FOREIGN KEY (`E_ID`) REFERENCES `employee` (`E_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_login`
--

LOCK TABLES `emp_login` WRITE;
/*!40000 ALTER TABLE `emp_login` DISABLE KEYS */;
INSERT INTO `emp_login` VALUES ('Harishraja01','emp@1','1'),('helloworld','ae-1265','2');
/*!40000 ALTER TABLE `emp_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `E_Fname` varchar(20) NOT NULL,
  `E_Lname` varchar(20) DEFAULT NULL,
  `Bdate` date DEFAULT NULL,
  `E_gender` enum('Male','Female') DEFAULT NULL,
  `E_JDate` date DEFAULT NULL,
  `E_ADD` varchar(255) DEFAULT NULL,
  `E_phno` bigint DEFAULT NULL,
  `E_Salary` int DEFAULT NULL,
  `E_ID` char(9) NOT NULL,
  PRIMARY KEY (`E_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('Harish','Raja','1998-02-01','Male','2019-07-06','T.Nagar',7894532165,21000,'1'),('hello','world','1987-02-25','Male','1999-02-02','ahbjhcjndkjnksmk',4568523235,2000,'2');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `employee_view_page`
--

DROP TABLE IF EXISTS `employee_view_page`;
/*!50001 DROP VIEW IF EXISTS `employee_view_page`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `employee_view_page` AS SELECT 
 1 AS `E_ID`,
 1 AS `E_Fname`,
 1 AS `E_Lname`,
 1 AS `Bdate`,
 1 AS `E_gender`,
 1 AS `E_JDate`,
 1 AS `E_ADD`,
 1 AS `E_phno`,
 1 AS `E_Salary`,
 1 AS `E_username`,
 1 AS `E_password`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `meds`
--

DROP TABLE IF EXISTS `meds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meds` (
  `med_id` int NOT NULL,
  `med_name` varchar(255) NOT NULL,
  `med_qty` int DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `med_price` decimal(10,2) DEFAULT NULL,
  `location_rack` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`med_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meds`
--

LOCK TABLES `meds` WRITE;
/*!40000 ALTER TABLE `meds` DISABLE KEYS */;
INSERT INTO `meds` VALUES (1,'Dolo 650 MG',1525,'Tablet',1.00,'rack 5');
/*!40000 ALTER TABLE `meds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `meds_view_page`
--

DROP TABLE IF EXISTS `meds_view_page`;
/*!50001 DROP VIEW IF EXISTS `meds_view_page`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `meds_view_page` AS SELECT 
 1 AS `med_id`,
 1 AS `med_name`,
 1 AS `med_qty`,
 1 AS `category`,
 1 AS `med_price`,
 1 AS `location_rack`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase` (
  `purchase_id` int NOT NULL,
  `med_id` int DEFAULT NULL,
  `supplier_id` char(9) DEFAULT NULL,
  `p_qty` int DEFAULT NULL,
  `p_cost` decimal(10,2) DEFAULT NULL,
  `p_date` date DEFAULT NULL,
  `mfg_date` date DEFAULT NULL,
  `exp_date` date DEFAULT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `fk3` (`med_id`),
  KEY `fk4` (`supplier_id`),
  CONSTRAINT `fk3` FOREIGN KEY (`med_id`) REFERENCES `meds` (`med_id`),
  CONSTRAINT `fk4` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`sup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (1,1,'1',1200,1000.00,'2024-04-24','2024-02-21','2026-04-23');
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `Sale_ID` int NOT NULL AUTO_INCREMENT,
  `S_Date` date DEFAULT NULL,
  `S_Time` time DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `employee_id` char(9) DEFAULT NULL,
  PRIMARY KEY (`Sale_ID`),
  KEY `fk1` (`customer_id`),
  KEY `fk2` (`employee_id`),
  CONSTRAINT `fk1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`cust_id`),
  CONSTRAINT `fk2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`E_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,'2024-04-24','08:29:40',226.00,8,'1'),(2,'2024-04-24','18:05:37',126.00,9,'1');
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_items`
--

DROP TABLE IF EXISTS `sales_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_items` (
  `med_id` int DEFAULT NULL,
  `sale_id` int DEFAULT NULL,
  `sale_Qty` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_items`
--

LOCK TABLES `sales_items` WRITE;
/*!40000 ALTER TABLE `sales_items` DISABLE KEYS */;
INSERT INTO `sales_items` VALUES (1,2,100);
/*!40000 ALTER TABLE `sales_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `sales_view_page`
--

DROP TABLE IF EXISTS `sales_view_page`;
/*!50001 DROP VIEW IF EXISTS `sales_view_page`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `sales_view_page` AS SELECT 
 1 AS `Sale_ID`,
 1 AS `S_Date`,
 1 AS `S_Time`,
 1 AS `total_amount`,
 1 AS `customer_id`,
 1 AS `employee_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `stock_purchase_view_page`
--

DROP TABLE IF EXISTS `stock_purchase_view_page`;
/*!50001 DROP VIEW IF EXISTS `stock_purchase_view_page`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `stock_purchase_view_page` AS SELECT 
 1 AS `purchase_id`,
 1 AS `med_id`,
 1 AS `supplier_id`,
 1 AS `p_qty`,
 1 AS `p_cost`,
 1 AS `p_date`,
 1 AS `mfg_date`,
 1 AS `exp_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `sup_id` char(9) NOT NULL,
  `sup_name` varchar(125) DEFAULT NULL,
  `sup_Add` varchar(255) DEFAULT NULL,
  `sup_phno` bigint DEFAULT NULL,
  PRIMARY KEY (`sup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES ('1','Yash','Noida 63,A',6393177536);
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!50001 DROP VIEW IF EXISTS `transaction`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `transaction` AS SELECT 
 1 AS `med_id`,
 1 AS `sale_id`,
 1 AS `sale_qty`,
 1 AS `med_name`,
 1 AS `med_price`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `customer_view_page`
--

/*!50001 DROP VIEW IF EXISTS `customer_view_page`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `customer_view_page` AS select `customer`.`cust_id` AS `cust_id`,`customer`.`C_Fname` AS `C_Fname`,`customer`.`C_Lname` AS `C_Lname`,`customer`.`C_gender` AS `C_gender`,`customer`.`C_phno` AS `C_phno`,`customer`.`C_Mail` AS `C_Mail` from `customer` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `employee_view_page`
--

/*!50001 DROP VIEW IF EXISTS `employee_view_page`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `employee_view_page` AS select `employee`.`E_ID` AS `E_ID`,`employee`.`E_Fname` AS `E_Fname`,`employee`.`E_Lname` AS `E_Lname`,`employee`.`Bdate` AS `Bdate`,`employee`.`E_gender` AS `E_gender`,`employee`.`E_JDate` AS `E_JDate`,`employee`.`E_ADD` AS `E_ADD`,`employee`.`E_phno` AS `E_phno`,`employee`.`E_Salary` AS `E_Salary`,`emp_login`.`E_username` AS `E_username`,`emp_login`.`E_password` AS `E_password` from (`employee` join `emp_login` on((`employee`.`E_ID` = `emp_login`.`E_ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `meds_view_page`
--

/*!50001 DROP VIEW IF EXISTS `meds_view_page`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `meds_view_page` AS select `meds`.`med_id` AS `med_id`,`meds`.`med_name` AS `med_name`,`meds`.`med_qty` AS `med_qty`,`meds`.`category` AS `category`,`meds`.`med_price` AS `med_price`,`meds`.`location_rack` AS `location_rack` from `meds` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `sales_view_page`
--

/*!50001 DROP VIEW IF EXISTS `sales_view_page`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `sales_view_page` AS select `sales`.`Sale_ID` AS `Sale_ID`,`sales`.`S_Date` AS `S_Date`,`sales`.`S_Time` AS `S_Time`,`sales`.`total_amount` AS `total_amount`,`sales`.`customer_id` AS `customer_id`,`sales`.`employee_id` AS `employee_id` from `sales` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `stock_purchase_view_page`
--

/*!50001 DROP VIEW IF EXISTS `stock_purchase_view_page`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `stock_purchase_view_page` AS select `purchase`.`purchase_id` AS `purchase_id`,`purchase`.`med_id` AS `med_id`,`purchase`.`supplier_id` AS `supplier_id`,`purchase`.`p_qty` AS `p_qty`,`purchase`.`p_cost` AS `p_cost`,`purchase`.`p_date` AS `p_date`,`purchase`.`mfg_date` AS `mfg_date`,`purchase`.`exp_date` AS `exp_date` from `purchase` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `transaction`
--

/*!50001 DROP VIEW IF EXISTS `transaction`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `transaction` AS select `e`.`med_id` AS `med_id`,`e`.`sale_id` AS `sale_id`,`e`.`sale_Qty` AS `sale_qty`,`e`.`med_name` AS `med_name`,`e`.`med_price` AS `med_price` from (select `sales_items`.`med_id` AS `med_id`,`sales_items`.`sale_id` AS `sale_id`,`sales_items`.`sale_Qty` AS `sale_Qty`,`meds`.`med_name` AS `med_name`,`meds`.`med_qty` AS `med_qty`,`meds`.`category` AS `category`,`meds`.`med_price` AS `med_price`,`meds`.`location_rack` AS `location_rack` from (`sales_items` join `meds` on((`sales_items`.`med_id` = `meds`.`med_id`)))) `e` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-25  5:11:17
