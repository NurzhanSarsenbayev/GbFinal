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
-- Table structure for table `younganimals`
--

DROP TABLE IF EXISTS `younganimals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `younganimals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `animal_name` varchar(45) DEFAULT NULL,
  `animal_type` varchar(45) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `list_of_commands` varchar(45) DEFAULT NULL,
  `age_in_months` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `younganimals`
--

LOCK TABLES `younganimals` WRITE;
/*!40000 ALTER TABLE `younganimals` DISABLE KEYS */;
INSERT INTO `younganimals` VALUES (1,'Fido','Dog','2020-01-01','Sit, Stay, Pounce',51),(2,'Bella','Dog','2019-11-11','Sit, Stay, Roll',52),(3,'Whiskers','Cat','2019-05-15','Sit, Pounce',58),(4,'Smudge','Cat','2020-02-20','Sit, Pounce, Scratch',49),(5,'Oliver','Cat','2020-06-30','Meow, Scratch, Jump',45),(6,'Hammy','Hamster','2021-03-10','Roll, Hide',36),(7,'Peanut','Hamster','2021-08-01','Roll, Spin',32);
/*!40000 ALTER TABLE `younganimals` ENABLE KEYS */;
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
