-- MySQL dump 10.16  Distrib 10.1.37-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: Esterno
-- ------------------------------------------------------
-- Server version	10.1.37-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Esterno`
--

DROP TABLE IF EXISTS `Esterno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Esterno` (
  `idEsterno` int(11) NOT NULL AUTO_INCREMENT,
  `tempEsterno` double NOT NULL,
  PRIMARY KEY (`idEsterno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Esterno`
--

LOCK TABLES `Esterno` WRITE;
/*!40000 ALTER TABLE `Esterno` DISABLE KEYS */;
/*!40000 ALTER TABLE `Esterno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StoricoEsterno`
--

DROP TABLE IF EXISTS `StoricoEsterno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StoricoEsterno` (
  `idStoricoEsterno` int(11) NOT NULL AUTO_INCREMENT,
  `dataAggE` date NOT NULL,
  `tempAggE` double NOT NULL,
  `idEsterno` int(11) NOT NULL,
  PRIMARY KEY (`idStoricoEsterno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StoricoEsterno`
--

LOCK TABLES `StoricoEsterno` WRITE;
/*!40000 ALTER TABLE `StoricoEsterno` DISABLE KEYS */;
/*!40000 ALTER TABLE `StoricoEsterno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-18 14:15:57
