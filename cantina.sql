-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: 192.168.5.33    Database: Cantina
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Botte`
--

DROP TABLE IF EXISTS `Botte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Botte` (
  `idBotte` int(11) NOT NULL,
  `contenuto` varchar(20) NOT NULL,
  `tempBotte` double NOT NULL,
  `tempsetBotte` double NOT NULL,
  `idLocale` int(11) NOT NULL,
  PRIMARY KEY (`idBotte`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Botte`
--

LOCK TABLES `Botte` WRITE;
/*!40000 ALTER TABLE `Botte` DISABLE KEYS */;
INSERT INTO `Botte` VALUES (4,'prosecco',4.1,5.1,2),(5,'serprino',5.1,6.1,2),(6,'glera',6.1,7.1,2),(7,'malvasia',7.1,8.1,2),(8,'moscato',8.1,9.1,2),(9,'vuoto',9.1,10.1,2),(10,'pinot',10.1,11.1,2),(11,'chardonnay',11.1,12.1,2),(12,'tai',12.1,13.1,2),(13,'vuota',13.1,14.1,2),(14,'moscato',14.1,15.100000000000001,1),(15,'tai',15.1,16.1,1),(16,'garganego',16.1,17.1,1),(17,'vuota',17.1,18.1,1),(18,'sfuso',18.1,19.1,1),(19,'vuota',19.1,20.1,1),(20,'moscato',20.1,21.1,1),(21,'garganego',21.1,22.1,1),(22,'vuota',22.1,23.1,3),(23,'tai',23.1,24.1,3),(24,'chardonnay',24.1,25.1,3),(25,'moscato',25.1,26.1,3),(26,'tai',26.1,27.1,3),(27,'garganego',27.1,28.1,3),(28,'vuota',28.1,29.1,3),(29,'malvasia',29.1,30.1,3),(30,'sfuso',30.1,31.1,3),(31,'glera',31.1,32.1,3),(32,'glera',32.1,33.1,3),(33,'pinot',33.1,34.1,3);
/*!40000 ALTER TABLE `Botte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Locale`
--

DROP TABLE IF EXISTS `Locale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Locale` (
  `idLocale` int(11) NOT NULL AUTO_INCREMENT,
  `tempLocale` double NOT NULL,
  `tempsetLocale` double NOT NULL,
  PRIMARY KEY (`idLocale`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Locale`
--

LOCK TABLES `Locale` WRITE;
/*!40000 ALTER TABLE `Locale` DISABLE KEYS */;
INSERT INTO `Locale` VALUES (1,1.1,5),(2,2.1,3.1),(3,3.1,4.1);
/*!40000 ALTER TABLE `Locale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StoricoBotte`
--

DROP TABLE IF EXISTS `StoricoBotte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StoricoBotte` (
  `idStoricoBotte` int(11) NOT NULL AUTO_INCREMENT,
  `dataAggB` datetime NOT NULL,
  `contenutoAggB` varchar(20) NOT NULL,
  `tempAggB` double NOT NULL,
  `idBotte` int(11) NOT NULL,
  `tempsetAggB` double NOT NULL,
  PRIMARY KEY (`idStoricoBotte`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StoricoBotte`
--

LOCK TABLES `StoricoBotte` WRITE;
/*!40000 ALTER TABLE `StoricoBotte` DISABLE KEYS */;
INSERT INTO `StoricoBotte` VALUES (1,'2019-04-29 00:00:00','moscato',14.1,14,15.1),(2,'2019-04-29 00:00:00','moscato',14.1,14,15.599999999999998);
/*!40000 ALTER TABLE `StoricoBotte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StoricoLocale`
--

DROP TABLE IF EXISTS `StoricoLocale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StoricoLocale` (
  `idStoricoLocale` int(11) NOT NULL AUTO_INCREMENT,
  `dataAggL` datetime NOT NULL,
  `tempAggL` double NOT NULL,
  `idLocale` int(11) NOT NULL,
  `tempsetAggL` double NOT NULL,
  PRIMARY KEY (`idStoricoLocale`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StoricoLocale`
--

LOCK TABLES `StoricoLocale` WRITE;
/*!40000 ALTER TABLE `StoricoLocale` DISABLE KEYS */;
/*!40000 ALTER TABLE `StoricoLocale` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-29 11:44:30
