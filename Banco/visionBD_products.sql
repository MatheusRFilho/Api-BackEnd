-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: visionBD
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

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
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `price` varchar(20) NOT NULL,
  `description` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'\"Lenovo V110-15IAP\"','\"$321.94\"','\"Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(2,'\"Lenovo V110-15IAP\"','\"$356.49\"','\"Asus VivoBook 15 X540NA-GQ008T Chocolate Black, 15.6\" HD, Pentium N4200, 4GB, 500GB, Windows 10 Home, En kbd\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(3,'\"Lenovo ThinkPad E31-80\"','\"$404.23\"','\"Lenovo ThinkPad E31-80, 13.3\" HD, Celeron 3855U 1.6GHz, 4GB, 128GB SSD, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(4,'\"Lenovo V110-15ISK\"','\"$409.63\"','\"Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 8GB, 128GB SSD, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(5,'\"Lenovo V110-15ISK\"','\"$454.73\"','\"Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Pro\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(6,'\"Lenovo V110-15IKB\"','\"$465.95\"','\"Lenovo V110-15IKB, 15.6\" HD, Core i5-7200U, 4GB, 500GB, DOS\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(7,'\"Lenovo V510 Black\"','\"$484.23\"','\"Lenovo V510 Black, 14\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(8,'\"Lenovo V510 Black\"','\"$487.80\"','\"Lenovo V510 Black, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(9,'\"Lenovo V510 Black\"','\"$498.23\"','\"Lenovo V510 Black, 15.6\" FHD, Core i3-7100U, 4GB, 128GB SSD, Windows 10 Pro\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(10,'\"Lenovo ThinkPad L570\"','\"$999.00\"','\"Lenovo ThinkPad L570, 15.6\" FHD, Core i7-7500U, 8GB, 256GB SSD, Windows 10 Pro\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(11,'\"Lenovo ThinkPad L460\"','\"$1096.02\"','\"Lenovo ThinkPad L460, 14\" FHD IPS, Core i7-6600U, 8GB, 256GB SSD, Windows 10 Pro\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(12,'\"Lenovo Legion Y520-15IKBM\"','\"$1112.91\"','\"Lenovo Legion Y520-15IKBM, Black, 15.6\" FHD IPS, Core i5-7300HQ, 8 GB, 128GB SSD + 2 TB HDD, NVIDIA GeForce GTX 1060 6 GB, FreeDOS + Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(13,'\"Lenovo Legion Y520\"','\"$1133.91\"','\"Lenovo Legion Y520, 15.6\" FHD, Core i7-7700HQ, 8GB, 128 GB SSD + 1TB HDD, GTX 1050 4GB, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(14,'\"Lenovo Legion Y520-15IKBM\"','\"$1149.00\"','\"Lenovo Legion Y520-15IKBM, 15.6\" FHD IPS, Core i7-7700HQ, 8GB, 128GB SSD + 1TB, GeForce GTX 1060 Max-Q 6GB, DOS\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(15,'\"Lenovo Yoga 720 Grey\"','\"$1149.73\"','\"Lenovo Yoga 720 Grey, 15.6\" FHD IPS, Core i5-7300HQ, 8GB, 256GB SSD, GeForce GTX 1050 2GB, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(16,'\"Lenovo Yoga 910 Grey\"','\"$1199.73\"','\"Lenovo Yoga 910 Grey, 13.9\" FHD Touch, Core i5-7200U, 8GB, 256GB SSD, Windows 10 Home\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(17,'\"Lenovo IdeaPad Miix 510 Platinum Silver\"','\"$1212.16\"','\"Lenovo IdeaPad Miix 510 Platinum Silver, 12.2\" IPS Touch, Core i5-7200U, 8GB, 256GB SSD, 4G, Windows 10 Pro\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(18,'\"Lenovo ThinkPad T470\"','\"$1349.23\"','\"Lenovo ThinkPad T470, 14\" FHD IPS, Core i5-7200U, 8GB, 256GB SSD, Windows 10 Pro\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(19,'\"Lenovo ThinkPad Yoga 370 Black\"','\"$1362.24\"','\"Lenovo ThinkPad Yoga 370 Black, 13.3\" FHD IPS Touch, Core i5-7200U, 8GB, 256GB SSD, 4G, Windows 10 Pro\"','\"/images/test-sites/e-commerce/items/cart2.png\"'),(20,'\"Lenovo Legion Y720\"','\"$1399.00\"','\"Lenovo Legion Y720, 15.6\" FHD IPS, Core i7-7700HQ, 8GB, 128GB SSD + 2TB HDD, GeForce GTX 1060 6GB, DOS, RGB backlit keyboard\"','\"/images/test-sites/e-commerce/items/cart2.png\"');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-16 20:22:01
