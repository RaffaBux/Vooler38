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
  `tempBotte` double DEFAULT NULL,
  `tempsetBotte` double DEFAULT NULL,
  `idLocale` int(11) NOT NULL,
  PRIMARY KEY (`idBotte`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Botte`
--

LOCK TABLES `Botte` WRITE;
/*!40000 ALTER TABLE `Botte` DISABLE KEYS */;
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
  `tempLocale` double DEFAULT NULL,
  `tempsetLocale` double DEFAULT NULL,
  PRIMARY KEY (`idLocale`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Locale`
--

LOCK TABLES `Locale` WRITE;
/*!40000 ALTER TABLE `Locale` DISABLE KEYS */;
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
  `dataAggB` date NOT NULL,
  `contenutoAggB` varchar(20) DEFAULT NULL,
  `tempAggB` double NOT NULL,
  `idBotte` int(11) NOT NULL,
  PRIMARY KEY (`idStoricoBotte`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StoricoBotte`
--

LOCK TABLES `StoricoBotte` WRITE;
/*!40000 ALTER TABLE `StoricoBotte` DISABLE KEYS */;
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
  `dataAggL` date NOT NULL,
  `tempAggL` double NOT NULL,
  `idLocale` int(11) NOT NULL,
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

-- Dump completed on 2019-04-11 10:42:47
