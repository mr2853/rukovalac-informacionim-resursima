-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: model_projekat
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
  `ustanova` char(2) NOT NULL,
  `oznaka_predmeta` varchar(6) NOT NULL,
  `naziv` varchar(120) NOT NULL,
  `ESPB` int NOT NULL,
  PRIMARY KEY (`oznaka_predmeta`,`ustanova`),
  KEY `fk_Nastavni predmet_Visokoskolska ustanova1_idx` (`ustanova`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nastavni_predmet`
--

LOCK TABLES `nastavni_predmet` WRITE;
/*!40000 ALTER TABLE `nastavni_predmet` DISABLE KEYS */;
INSERT INTO `nastavni_predmet` VALUES ('IR','ARR','Arhitektura racunara',8),('TF','DIM','Diskretna matematika',8),('IR','MAT','Matematika',8),('TF','WED','Web Dizajn',8);
/*!40000 ALTER TABLE `nastavni_predmet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nivo_studija`
--

DROP TABLE IF EXISTS `nivo_studija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nivo_studija` (
  `oznaka` int NOT NULL,
  `naziv` varchar(80) NOT NULL,
  PRIMARY KEY (`oznaka`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `program_ustanove` char(2) NOT NULL,
  `oznaka_programa` varchar(3) NOT NULL,
  `blok` int NOT NULL,
  `pozicija` int NOT NULL,
  `oznaka_predmeta` varchar(6) NOT NULL,
  `Ustanova predmet` char(2) NOT NULL,
  PRIMARY KEY (`program_ustanove`,`blok`,`pozicija`,`oznaka_programa`),
  KEY `fk_Plan studijske grupe_Studijski programi1_idx` (`oznaka_programa`,`program_ustanove`),
  KEY `fk_Plan studijske grupe_Nastavni predmet1_idx` (`oznaka_predmeta`,`Ustanova predmet`),
  CONSTRAINT `fk_Plan studijske grupe_Nastavni predmet1` FOREIGN KEY (`oznaka_predmeta`, `Ustanova predmet`) REFERENCES `nastavni_predmet` (`oznaka_predmeta`, `ustanova`),
  CONSTRAINT `fk_Plan studijske grupe_Studijski programi1` FOREIGN KEY (`oznaka_programa`, `program_ustanove`) REFERENCES `studijski_programi` (`oznaka_programa`, `ustanova`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_studijske_grupe`
--

LOCK TABLES `plan_studijske_grupe` WRITE;
/*!40000 ALTER TABLE `plan_studijske_grupe` DISABLE KEYS */;
INSERT INTO `plan_studijske_grupe` VALUES ('IR','IT',2,3,'ARR','IR'),('TF','SI',1,2,'DIM','TF'),('TF','SI',1,1,'WED','TF');
/*!40000 ALTER TABLE `plan_studijske_grupe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studenti`
--

DROP TABLE IF EXISTS `studenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studenti` (
  `ustanova` char(2) NOT NULL,
  `struka` char(2) NOT NULL,
  `broj_indeksa` varchar(6) NOT NULL,
  `prezime` varchar(20) NOT NULL,
  `ime_roditelja` varchar(20) DEFAULT NULL,
  `ime` varchar(20) NOT NULL,
  `pol` char(1) DEFAULT NULL,
  `adresa_stanovanja` varchar(80) DEFAULT NULL,
  `Telefon` varchar(20) DEFAULT NULL,
  `JMBG` char(13) DEFAULT NULL,
  `datum_rodjenja` date DEFAULT NULL,
  PRIMARY KEY (`struka`,`broj_indeksa`,`ustanova`),
  KEY `fk_Studenti_Visokoskolska ustanova_idx` (`ustanova`),
  CONSTRAINT `fk_Studenti_Visokoskolska ustanova` FOREIGN KEY (`ustanova`) REFERENCES `visokoskolska_ustanova` (`oznaka`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `ustanova` char(2) NOT NULL,
  `nivo_studija` int NOT NULL,
  `oznaka_programa` varchar(3) NOT NULL,
  `naziv_programa` varchar(120) NOT NULL,
  PRIMARY KEY (`oznaka_programa`,`ustanova`),
  KEY `fk_Studijski programi_Nivo studija1_idx` (`nivo_studija`),
  CONSTRAINT `fk_Studijski programi_Nivo studija1` FOREIGN KEY (`nivo_studija`) REFERENCES `nivo_studija` (`oznaka`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `ustanova` char(2) NOT NULL,
  `oznaka_programa` varchar(3) NOT NULL,
  `student_iz_ustanove` char(2) NOT NULL,
  `struka` char(2) NOT NULL,
  `broj_indeksa` varchar(6) NOT NULL,
  `skolska_godina` int NOT NULL,
  `godina_studija` int NOT NULL,
  `blok` int NOT NULL,
  `redni_broj_upisa` int NOT NULL,
  `datum_upisa` date NOT NULL,
  `datum_overe` date DEFAULT NULL,
  `ESPB_pocetni` int NOT NULL,
  `ESPB_krajnji` int NOT NULL,
  PRIMARY KEY (`ustanova`,`oznaka_programa`,`student_iz_ustanove`,`struka`,`broj_indeksa`,`skolska_godina`,`godina_studija`,`blok`,`redni_broj_upisa`),
  KEY `fk_Tok studija_Studijski programi1_idx` (`oznaka_programa`,`ustanova`),
  KEY `fk_Tok studija_Studenti1_idx` (`struka`,`broj_indeksa`,`student_iz_ustanove`),
  CONSTRAINT `fk_Tok studija_Studenti1` FOREIGN KEY (`struka`, `broj_indeksa`, `student_iz_ustanove`) REFERENCES `studenti` (`struka`, `broj_indeksa`, `ustanova`),
  CONSTRAINT `fk_Tok studija_Studijski programi1` FOREIGN KEY (`oznaka_programa`, `ustanova`) REFERENCES `studijski_programi` (`oznaka_programa`, `ustanova`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `oznaka` char(2) NOT NULL,
  `naziv` varchar(80) NOT NULL,
  `adresa` varchar(80) NOT NULL,
  PRIMARY KEY (`oznaka`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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

-- Dump completed on 2021-01-05 14:10:31
