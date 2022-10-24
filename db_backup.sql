-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `disease` text,
  `doctor` text,
  `admission_on` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `medicines` text,
  `known_diseases` text,
  `medicines_in_dosage` text,
  `bed` varchar(12) DEFAULT 'NOT PROVIDED',
  `billed` int NOT NULL DEFAULT '0',
  `initial_amount` int NOT NULL DEFAULT '1500',
  `init_paid` char(1) DEFAULT 'n',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'huehue','asdd','sdfs','2022-10-22 19:30:12','sdf',NULL,NULL,'NOT PROVIDED',0,1500,'n'),(2,'Yuvraj Sinha',NULL,NULL,'2022-10-23 08:24:42','','Bavaseer, Kabz',NULL,'NULL',0,1500,'n'),(3,'HEHEHE',NULL,NULL,'2022-10-23 08:26:22','','kabz',NULL,NULL,0,1500,'n'),(4,'sdzf',NULL,NULL,'2022-10-23 08:27:11','dsf','sdf',NULL,'adf',0,1500,'n'),(5,'',NULL,NULL,'2022-10-23 08:28:25',NULL,NULL,NULL,'',0,1500,'n'),(6,'',NULL,NULL,'2022-10-23 08:28:36',NULL,NULL,NULL,NULL,0,1500,'n'),(7,'Yuvraj Sinha',NULL,'34,357','2022-10-23 08:34:03',NULL,'kabz, bavaseer','','A32',0,1500,'n'),(8,'dxf',NULL,'sd','2022-10-23 08:53:50',NULL,'sf','sdf','as',0,1500,'n'),(9,'sdsd',NULL,'asd','2022-10-23 09:00:00',NULL,'sdsd','asd','a32',0,15000,'y'),(10,'Paurush',NULL,'','2022-10-23 09:01:26',NULL,'','',NULL,0,15000,'n');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Paurush Sinha','admin','hari',10000000);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-23 14:34:44