-- MySQL dump 10.13  Distrib 5.7.33, for Win64 (x86_64)
--
-- Host: localhost    Database: cursos
-- ------------------------------------------------------
-- Server version	5.7.33

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
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pais` varchar(100) DEFAULT 'Perú',
  `nota` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
INSERT INTO `alumno` VALUES (1,'Cordelia','Robey','crobey0@abc.net.au','Brazil',15),(2,'Camey','Newbigging','cnewbigging1@infoseek.co.jp','Brazil',18),(3,'Amby','McCombe','amccombe2@eventbrite.com','Peru',10),(4,'Page','Dowman','pdowman3@theglobeandmail.com','Brazil',16),(5,'Launce','Jirek','ljirek4@army.mil','Brazil',16),(6,'Pail','Ells','pells5@liveinternet.ru','Brazil',20),(7,'Kala','Jurgenson','kjurgenson6@adobe.com','Chile',16),(8,'Carmita','Antognelli','cantognelli7@tinypic.com','Brazil',19),(9,'Conrado','Davidy','cdavidy8@stanford.edu','Brazil',18),(10,'Wilden','Cafferty','wcafferty9@multiply.com','Brazil',12),(11,'Steward','Learmonth','slearmontha@hostgator.com','Brazil',20),(12,'Anallise','Jouanny','ajouannyb@desdev.cn','Brazil',20),(13,'Vonny','Iacovone','viacovonec@flavors.me','Peru',18),(14,'Sonia','Tampion','stampiond@deliciousdays.com','Bolivia',17),(15,'Alden','Meneo','ameneoe@squarespace.com','Colombia',17),(16,'Karlene','Revely','krevelyf@ehow.com','Brazil',10),(17,'Jackie','Pestor','jpestorg@spiegel.de','Brazil',11),(18,'Pepita','Harmes','pharmesh@tiny.cc','Brazil',19),(19,'Elane','Freund','efreundi@wix.com','Brazil',16),(20,'Rhetta','Antonat','rantonatj@is.gd','Peru',16),(21,'Suzann','Arrowsmith','sarrowsmithk@pen.io','Brazil',16),(22,'Yulma','Le - Count','ylecountl@instagram.com','Colombia',15),(23,'Ortensia','Baldinotti','obaldinottim@taobao.com','Chile',19),(24,'Hugibert','Tschierse','htschiersen@goo.ne.jp','Peru',16),(25,'Kathye','Caves','kcaveso@ning.com','Colombia',14),(26,'Terri-jo','Braunroth','tbraunrothp@smugmug.com','Peru',13),(27,'Valentine','Rudwell','vrudwellq@behance.net','Bolivia',13),(28,'Morena','Buntain','mbuntainr@dailymail.co.uk','Colombia',14),(29,'Friederike','Brownell','fbrownells@blog.com','Brazil',16),(30,'Perl','Aymer','paymert@google.com.br','Brazil',15),(31,'Caddric','Avramovsky','cavramovskyu@blinklist.com','Colombia',20),(32,'Wright','Matchitt','wmatchittv@google.de','Brazil',11),(33,'Orsola','Beckley','obeckleyw@usgs.gov','Colombia',15),(34,'Keeley','Retchless','kretchlessx@ustream.tv','Brazil',17),(35,'Bryon','MacSkeaghan','bmacskeaghany@jigsy.com','Bolivia',16),(36,'Denice','Linfield','dlinfieldz@washington.edu','Brazil',13),(37,'Mireille','Palfreyman','mpalfreyman10@devhub.com','Brazil',19),(38,'Emmey','Tappington','etappington11@wired.com','Brazil',16),(39,'Dew','Craisford','dcraisford12@linkedin.com','Colombia',10),(40,'Vincents','Proske','vproske13@bravesites.com','Peru',14),(41,'Mandy','Muggleston','mmuggleston14@diigo.com','Colombia',18),(42,'Corrine','Oloshin','coloshin15@tiny.cc','Peru',16),(43,'Fanchon','Moloney','fmoloney16@dropbox.com','Brazil',14),(44,'Skell','Rutty','srutty17@github.io','Brazil',20),(45,'Beret','Manntschke','bmanntschke18@sciencedirect.com','Colombia',17),(46,'Madeline','Luney','mluney19@pagesperso-orange.fr','Colombia',11),(47,'Hally','Fronczak','hfronczak1a@furl.net','Colombia',19),(48,'Corena','Peddar','cpeddar1b@ox.ac.uk','Peru',13),(49,'Libby','Deesly','ldeesly1c@imgur.com','Bolivia',18),(50,'Lanae','Marquiss','lmarquiss1d@bigcartel.com','Brazil',11),(51,'Beatriz','Stollwerck','bstollwerck1e@booking.com','Peru',16),(52,'Edwina','Osan','eosan1f@ask.com','Peru',19),(53,'Thekla','Ternent','tternent1g@unicef.org','Colombia',12),(54,'Vannie','Ritson','vritson1h@flickr.com','Brazil',20),(55,'Moreen','Gaiford','mgaiford1i@wix.com','Brazil',12),(56,'Anabal','Pittford','apittford1j@bigcartel.com','Brazil',12),(57,'Tatiania','Berntsson','tberntsson1k@auda.org.au','Brazil',10),(58,'Alex','Binnes','abinnes1l@ucoz.com','Brazil',20),(59,'Archaimbaud','Jaycocks','ajaycocks1m@ca.gov','Venezuela',18),(60,'Darlene','Glazer','dglazer1n@cafepress.com','Brazil',12),(61,'Alan','Moodycliffe','amoodycliffe1o@home.pl','Colombia',20),(62,'Cchaddie','Laytham','claytham1p@blogtalkradio.com','Peru',18),(63,'Essy','Bellis','ebellis1q@youtube.com','Brazil',15),(64,'Dallas','Beevor','dbeevor1r@goo.gl','Brazil',12),(65,'Carr','Vermer','cvermer1s@webnode.com','Venezuela',12),(66,'Thayne','Legen','tlegen1t@harvard.edu','Brazil',17),(67,'Nicola','Peverell','npeverell1u@seattletimes.com','Brazil',11),(68,'Ariela','Simmgen','asimmgen1v@slideshare.net','Chile',12),(69,'Zara','Verillo','zverillo1w@ebay.com','Brazil',17),(70,'Giovanna','Castano','gcastano1x@wikia.com','Brazil',19),(71,'Keriann','Syce','ksyce1y@smh.com.au','Brazil',11),(72,'Winslow','Makiver','wmakiver1z@opensource.org','Peru',15),(73,'Vannie','Goffe','vgoffe20@netlog.com','Chile',12),(74,'Marleah','Bohlin','mbohlin21@quantcast.com','Colombia',18),(75,'Rayner','Giraux','rgiraux22@shutterfly.com','Peru',16),(76,'Warner','Railton','wrailton23@tmall.com','Colombia',20),(77,'Carlita','Hanne','channe24@eepurl.com','Brazil',15),(78,'Carolyne','Grebner','cgrebner25@ezinearticles.com','Brazil',16),(79,'Andree','Warrick','awarrick26@toplist.cz','Peru',14),(80,'Zena','Garley','zgarley27@yahoo.co.jp','Colombia',19),(81,'Ladonna','Bowdidge','lbowdidge28@geocities.com','Brazil',15),(82,'Ludovico','Leif','lleif29@baidu.com','Brazil',14),(83,'Amy','Fedorski','afedorski2a@technorati.com','Venezuela',18),(84,'Janenna','Rainey','jrainey2b@webmd.com','Brazil',12),(85,'Shellysheldon','Iuorio','siuorio2c@acquirethisname.com','Brazil',15),(86,'Rafe','Sparsholt','rsparsholt2d@newyorker.com','Brazil',15),(87,'Maria','Schohier','mschohier2e@java.com','Brazil',14),(88,'Gaile','McIlvenny','gmcilvenny2f@smh.com.au','Brazil',18),(89,'Georgianne','Szymaniak','gszymaniak2g@tumblr.com','Peru',18),(90,'Frederich','Lempel','flempel2h@slate.com','Peru',19),(91,'Augustin','Woodrough','awoodrough2i@blogspot.com','Peru',16),(92,'Jasmina','Grinov','jgrinov2j@webs.com','Colombia',17),(93,'Valenka','Dalziell','vdalziell2k@sakura.ne.jp','Brazil',11),(94,'Dela','Felgat','dfelgat2l@europa.eu','Chile',11),(95,'Erl','Teodori','eteodori2m@usnews.com','Bolivia',12),(96,'Celestine','Gaunt','cgaunt2n@oracle.com','Brazil',19),(97,'Reuben','Shingles','rshingles2o@list-manage.com','Brazil',18),(98,'Faythe','MacGee','fmacgee2p@cam.ac.uk','Brazil',13),(99,'Malia','Amori','mamori2q@deviantart.com','Peru',18),(100,'Estrella','Graves','egraves2r@cbslocal.com','Brazil',20);
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26 22:53:27
