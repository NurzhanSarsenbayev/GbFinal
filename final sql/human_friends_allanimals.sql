-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: human_friends
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
-- Table structure for table `allanimals`
--

DROP TABLE IF EXISTS `allanimals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allanimals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `animal_name` varchar(45) DEFAULT NULL,
  `animal_type` varchar(45) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `list_of_commands` varchar(45) DEFAULT NULL,
  `old_table` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allanimals`
--

LOCK TABLES `allanimals` WRITE;
/*!40000 ALTER TABLE `allanimals` DISABLE KEYS */;
INSERT INTO `allanimals` VALUES (1,'Fido','Dog','2020-01-01','Sit, Stay, Pounce','From Dogs table'),(2,'Buddy','Dog','2018-12-10','Sit, Paw, Bark','From Dogs table'),(3,'Bella','Dog','2019-11-11','Sit, Stay, Roll','From Dogs table'),(4,'Whiskers','Cat','2019-05-15','Sit, Pounce','From Cats table'),(5,'Smudge','Cat','2020-02-20','Sit, Pounce, Scratch','From Cats table'),(6,'Oliver','Cat','2020-06-30','Meow, Scratch, Jump','From Cats table'),(7,'Hammy','Hamster','2021-03-10','Roll, Hide','From Hamsters table'),(8,'Peanut','Hamster','2021-08-01','Roll, Spin','From Hamsters table'),(9,'Thunder','Horse','2015-07-21','Trot, Canter, Gallop','From Horses table'),(10,'Storm','Horse','2014-05-05','Trot, Canter','From Horses table'),(11,'Blaze','Horse','2016-02-29','Trot, Jump, Gallop','From Horses table'),(12,'Eeyore','Donkey','2017-09-18','Walk, Carry Load, Bray','From Donkeys table'),(13,'Burro','Donkey','2019-01-23','Walk, Bray, Kick','From Donkeys table'),(14,'Sandy','Camel','2016-11-03','Walk, Carry Load','From Camels table'),(15,'Dune','Camel','2018-12-12','Walk, Sit','From Camels table'),(16,'Sahara','Camel','2015-08-14','Walk, Run','From Camels table');
/*!40000 ALTER TABLE `allanimals` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-04  9:22:25
