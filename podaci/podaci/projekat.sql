-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: projekat
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `nastavni_predmet`
--

DROP TABLE IF EXISTS `nastavni_predmet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nastavni_predmet` (
  `VU_OZNAKA` char(2) NOT NULL,
  `NP_OZNAKA` varchar(6) NOT NULL,
  `NP_NAZIV` varchar(120) NOT NULL,
  `NP_ESPB` decimal(2,0) NOT NULL,
  PRIMARY KEY (`VU_OZNAKA`,`NP_OZNAKA`),
  CONSTRAINT `FK_IZVODI_PREDMETE` FOREIGN KEY (`VU_OZNAKA`) REFERENCES `visokoskolska_ustanova` (`VU_OZNAKA`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nastavni_predmet`
--

LOCK TABLES `nastavni_predmet` WRITE;
/*!40000 ALTER TABLE `nastavni_predmet` DISABLE KEYS */;
INSERT INTO `nastavni_predmet` VALUES ('IR','ARR','Arhitektura racunara',8),('IR','MAT','Matematika',8),('TF','DIM','Diskretna matematika',8),('TF','WED','Web Dizajn',8);
/*!40000 ALTER TABLE `nastavni_predmet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nivo_studija`
--

DROP TABLE IF EXISTS `nivo_studija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nivo_studija` (
  `NIV_OZNAKA` decimal(2,0) NOT NULL,
  `NIV_NAZIV` varchar(80) NOT NULL,
  PRIMARY KEY (`NIV_OZNAKA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nivo_studija`
--

LOCK TABLES `nivo_studija` WRITE;
/*!40000 ALTER TABLE `nivo_studija` DISABLE KEYS */;
INSERT INTO `nivo_studija` VALUES (1,'Osnovne strukovne studije'),(2,'Osnovne akademske studije'),(3,'Specijalisticke akademske studije'),(4,'Master akademske studije'),(5,'Doktorske akademske studije');
/*!40000 ALTER TABLE `nivo_studija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plan_studijske_grupe`
--

DROP TABLE IF EXISTS `plan_studijske_grupe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plan_studijske_grupe` (
  `STU_VU_OZNAKA` char(2) NOT NULL,
  `SP_OZNAKA` varchar(3) NOT NULL,
  `SPB_BLOK` decimal(2,0) NOT NULL,
  `SPB_POZICIJA` decimal(2,0) NOT NULL,
  `VU_OZNAKA` char(2) NOT NULL,
  `NP_OZNAKA` varchar(6) NOT NULL,
  PRIMARY KEY (`STU_VU_OZNAKA`,`SP_OZNAKA`,`SPB_BLOK`,`SPB_POZICIJA`),
  KEY `FK_NA_POZICIJI` (`VU_OZNAKA`,`NP_OZNAKA`),
  CONSTRAINT `FK_NA_POZICIJI` FOREIGN KEY (`VU_OZNAKA`, `NP_OZNAKA`) REFERENCES `nastavni_predmet` (`VU_OZNAKA`, `NP_OZNAKA`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_STRUKTURA_PO_BLOKOVIMA` FOREIGN KEY (`STU_VU_OZNAKA`, `SP_OZNAKA`) REFERENCES `studijski_programi` (`VU_OZNAKA`, `SP_OZNAKA`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_studijske_grupe`
--

LOCK TABLES `plan_studijske_grupe` WRITE;
/*!40000 ALTER TABLE `plan_studijske_grupe` DISABLE KEYS */;
INSERT INTO `plan_studijske_grupe` VALUES ('IR','IT',2,3,'IR','ARR'),('TF','SI',1,1,'TF','DIM'),('TF','SI',1,2,'TF','WED');
/*!40000 ALTER TABLE `plan_studijske_grupe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studenti`
--

DROP TABLE IF EXISTS `studenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studenti` (
  `VU_OZNAKA` char(2) NOT NULL,
  `STU_STRUKA` char(2) NOT NULL,
  `STU_BROJ_INDEKSA` varchar(6) NOT NULL,
  `STU_PREZIME` varchar(20) NOT NULL,
  `STU_IME_RODITELJA` varchar(20) DEFAULT NULL,
  `STU_IME` varchar(20) NOT NULL,
  `STU_POL` char(1) NOT NULL DEFAULT 'N',
  `STU_ADRESA_STANOVANJA` varchar(80) DEFAULT NULL,
  `STU_TELEFON` varchar(20) DEFAULT NULL,
  `STU_JMBG` char(13) DEFAULT NULL,
  `STU_DATUM_RODJENJA` date DEFAULT NULL,
  PRIMARY KEY (`VU_OZNAKA`,`STU_STRUKA`,`STU_BROJ_INDEKSA`),
  CONSTRAINT `FK_STUDIRAJU_NA` FOREIGN KEY (`VU_OZNAKA`) REFERENCES `visokoskolska_ustanova` (`VU_OZNAKA`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studenti`
--

LOCK TABLES `studenti` WRITE;
/*!40000 ALTER TABLE `studenti` DISABLE KEYS */;
INSERT INTO `studenti` VALUES ('IR','IT','120000','Ivanovic','Jovan','Milica','Z','Bulevar 4','064000111','0111999154566','1999-11-01'),('IR','IT','130000','Popovic','Ranko','Lazar','M','Bulevar 3','066111222','0101999154567','1999-01-01'),('TF','SI','100000','Petrovic','Petar','Ana','Z','Bulevar 1','065000111','2910000612345','2000-10-19'),('TF','SI','110000','Maric','Marko','Ivan','M','Bulevar 2','065000444','2410000612345','2000-10-24');
/*!40000 ALTER TABLE `studenti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studijski_programi`
--

DROP TABLE IF EXISTS `studijski_programi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studijski_programi` (
  `VU_OZNAKA` char(2) NOT NULL,
  `NIV_OZNAKA` decimal(2,0) NOT NULL,
  `SP_OZNAKA` varchar(3) NOT NULL,
  `SP_NAZIV` varchar(120) NOT NULL,
  PRIMARY KEY (`VU_OZNAKA`,`SP_OZNAKA`),
  KEY `FK_KLASIFIKACIJA_PO_NIVOU` (`NIV_OZNAKA`),
  CONSTRAINT `FK_KLASIFIKACIJA_PO_NIVOU` FOREIGN KEY (`NIV_OZNAKA`) REFERENCES `nivo_studija` (`NIV_OZNAKA`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_OBRAZUJE_ZA` FOREIGN KEY (`VU_OZNAKA`) REFERENCES `visokoskolska_ustanova` (`VU_OZNAKA`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studijski_programi`
--

LOCK TABLES `studijski_programi` WRITE;
/*!40000 ALTER TABLE `studijski_programi` DISABLE KEYS */;
INSERT INTO `studijski_programi` VALUES ('IR',3,'IT','Informatika'),('TF',3,'SI','Softversko inzenjerstvo');
/*!40000 ALTER TABLE `studijski_programi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tok_studija`
--

DROP TABLE IF EXISTS `tok_studija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tok_studija` (
  `STU_VU_OZNAKA` char(2) NOT NULL,
  `SP_OZNAKA` varchar(3) NOT NULL,
  `VU_OZNAKA` char(2) NOT NULL,
  `STU_STRUKA` char(2) NOT NULL,
  `STU_BROJ_INDEKSA` varchar(6) NOT NULL,
  `TOK_SKOLSKA_GODINA` decimal(4,0) NOT NULL,
  `TOK_GODINA_STUDIJA` decimal(1,0) NOT NULL,
  `TOK_BLOK` decimal(2,0) NOT NULL,
  `TOK_REDNI_BROJ_UPISA` decimal(2,0) NOT NULL,
  `TOK_DATUM_UPISA` date NOT NULL,
  `TOK_DATUM_OVERE` date DEFAULT NULL,
  `TOK_ESPB_POCETNI` decimal(3,0) NOT NULL DEFAULT '0',
  `TOK_ESPB_KRAJNJI` decimal(3,0) NOT NULL,
  PRIMARY KEY (`STU_VU_OZNAKA`,`SP_OZNAKA`,`VU_OZNAKA`,`STU_STRUKA`,`STU_BROJ_INDEKSA`,`TOK_SKOLSKA_GODINA`,`TOK_GODINA_STUDIJA`,`TOK_REDNI_BROJ_UPISA`,`TOK_BLOK`),
  KEY `FK_STUDIRANJE` (`VU_OZNAKA`,`STU_STRUKA`,`STU_BROJ_INDEKSA`),
  CONSTRAINT `FK_KO_STUDIRA` FOREIGN KEY (`STU_VU_OZNAKA`, `SP_OZNAKA`) REFERENCES `studijski_programi` (`VU_OZNAKA`, `SP_OZNAKA`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_STUDIRANJE` FOREIGN KEY (`VU_OZNAKA`, `STU_STRUKA`, `STU_BROJ_INDEKSA`) REFERENCES `studenti` (`VU_OZNAKA`, `STU_STRUKA`, `STU_BROJ_INDEKSA`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tok_studija`
--

LOCK TABLES `tok_studija` WRITE;
/*!40000 ALTER TABLE `tok_studija` DISABLE KEYS */;
INSERT INTO `tok_studija` VALUES ('IR','IT','IR','IT','120000',2021,2,2,4,'2021-01-08',NULL,0,52),('IR','IT','IR','IT','130000',2021,1,1,2,'2021-01-04',NULL,0,0),('TF','SI','TF','SI','100000',2021,1,1,1,'2021-01-01',NULL,0,0),('TF','SI','TF','SI','110000',2021,2,2,3,'2021-01-06',NULL,0,60);
/*!40000 ALTER TABLE `tok_studija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visokoskolska_ustanova`
--

DROP TABLE IF EXISTS `visokoskolska_ustanova`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visokoskolska_ustanova` (
  `VU_OZNAKA` char(2) NOT NULL,
  `VU_NAZIV` varchar(80) NOT NULL,
  `VU_ADRESA` varchar(80) NOT NULL,
  PRIMARY KEY (`VU_OZNAKA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visokoskolska_ustanova`
--

LOCK TABLES `visokoskolska_ustanova` WRITE;
/*!40000 ALTER TABLE `visokoskolska_ustanova` DISABLE KEYS */;
INSERT INTO `visokoskolska_ustanova` VALUES ('IR','Informatika i Racunarstvo','Danijelova2'),('TF','Tehnicki Fakultet','Danijelova 2');
/*!40000 ALTER TABLE `visokoskolska_ustanova` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-07 20:23:30
