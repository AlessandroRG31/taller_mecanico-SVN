/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.11-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: taller_mecanico
-- ------------------------------------------------------
-- Server version	10.11.11-MariaDB-0+deb12u1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add mantenimiento',7,'add_mantenimiento'),
(26,'Can change mantenimiento',7,'change_mantenimiento'),
(27,'Can delete mantenimiento',7,'delete_mantenimiento'),
(28,'Can view mantenimiento',7,'view_mantenimiento'),
(29,'Can add vehiculo',8,'add_vehiculo'),
(30,'Can change vehiculo',8,'change_vehiculo'),
(31,'Can delete vehiculo',8,'delete_vehiculo'),
(32,'Can view vehiculo',8,'view_vehiculo'),
(33,'Can add repuesto mantenimiento',9,'add_repuestomantenimiento'),
(34,'Can change repuesto mantenimiento',9,'change_repuestomantenimiento'),
(35,'Can delete repuesto mantenimiento',9,'delete_repuestomantenimiento'),
(36,'Can view repuesto mantenimiento',9,'view_repuestomantenimiento'),
(37,'Can add proximo mantenimiento',10,'add_proximomantenimiento'),
(38,'Can change proximo mantenimiento',10,'change_proximomantenimiento'),
(39,'Can delete proximo mantenimiento',10,'delete_proximomantenimiento'),
(40,'Can view proximo mantenimiento',10,'view_proximomantenimiento'),
(41,'Can add empresa',11,'add_empresa'),
(42,'Can change empresa',11,'change_empresa'),
(43,'Can delete empresa',11,'delete_empresa'),
(44,'Can view empresa',11,'view_empresa'),
(45,'Can add repuesto',12,'add_repuesto'),
(46,'Can change repuesto',12,'change_repuesto'),
(47,'Can delete repuesto',12,'delete_repuesto'),
(48,'Can view repuesto',12,'view_repuesto'),
(49,'Can add empresa',13,'add_empresa'),
(50,'Can change empresa',13,'change_empresa'),
(51,'Can delete empresa',13,'delete_empresa'),
(52,'Can view empresa',13,'view_empresa'),
(53,'Can add cliente',14,'add_cliente'),
(54,'Can change cliente',14,'change_cliente'),
(55,'Can delete cliente',14,'delete_cliente'),
(56,'Can view cliente',14,'view_cliente');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES
(1,'pbkdf2_sha256$1000000$cEOy08BTdGzsUwAiDsEkGz$ZJ+x6aqJAj7gadoJ8TiyoVo6af+4ZmRT7XrIfc7+QEs=','2025-06-11 23:14:33.931575',0,'alessandro1331','','','',0,1,'2025-06-08 23:36:31.275757');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes_cliente`
--

DROP TABLE IF EXISTS `clientes_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes_cliente` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `dui` varchar(9) NOT NULL,
  `licencia_conducir` varchar(30) DEFAULT NULL,
  `licencia_circulacion` varchar(30) DEFAULT NULL,
  `telefono` varchar(8) NOT NULL,
  `direccion` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dui` (`dui`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes_cliente`
--

LOCK TABLES `clientes_cliente` WRITE;
/*!40000 ALTER TABLE `clientes_cliente` DISABLE KEYS */;
INSERT INTO `clientes_cliente` VALUES
(1,'Daniel','asd','1234567-8','12312312312','123123123','12312312','123 asdsa d'),
(2,'Alessadro','Gonzalez','0638718-6','1231231245','123123431','78784788','12 calle poniente'),
(3,'asdasd','asdasd','0638118-6','213123123','123123','12312312','asd 123e'),
(4,'dadasd','rsasd','2332322-2','asdas','1234566','12345678','asdasd'),
(5,'nuevo','cliente','1234567-1','213213','23323','12345678','asdasd');
/*!40000 ALTER TABLE `clientes_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_empresa`
--

DROP TABLE IF EXISTS `core_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_empresa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_empresa`
--

LOCK TABLES `core_empresa` WRITE;
/*!40000 ALTER TABLE `core_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(14,'clientes','cliente'),
(5,'contenttypes','contenttype'),
(13,'core','empresa'),
(7,'mantenimiento','mantenimiento'),
(10,'mantenimiento','proximomantenimiento'),
(9,'mantenimiento','repuestomantenimiento'),
(8,'mantenimiento','vehiculo'),
(11,'repuestos','empresa'),
(12,'repuestos','repuesto'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-06-08 23:01:29.649663'),
(2,'auth','0001_initial','2025-06-08 23:01:29.751138'),
(3,'admin','0001_initial','2025-06-08 23:01:29.766729'),
(4,'admin','0002_logentry_remove_auto_add','2025-06-08 23:01:29.770281'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-06-08 23:01:29.773672'),
(6,'contenttypes','0002_remove_content_type_name','2025-06-08 23:01:29.788293'),
(7,'auth','0002_alter_permission_name_max_length','2025-06-08 23:01:29.796891'),
(8,'auth','0003_alter_user_email_max_length','2025-06-08 23:01:29.803409'),
(9,'auth','0004_alter_user_username_opts','2025-06-08 23:01:29.806620'),
(10,'auth','0005_alter_user_last_login_null','2025-06-08 23:01:29.815083'),
(11,'auth','0006_require_contenttypes_0002','2025-06-08 23:01:29.815618'),
(12,'auth','0007_alter_validators_add_error_messages','2025-06-08 23:01:29.818955'),
(13,'auth','0008_alter_user_username_max_length','2025-06-08 23:01:29.824623'),
(14,'auth','0009_alter_user_last_name_max_length','2025-06-08 23:01:29.829706'),
(15,'auth','0010_alter_group_name_max_length','2025-06-08 23:01:29.834826'),
(16,'auth','0011_update_proxy_permissions','2025-06-08 23:01:29.838326'),
(17,'auth','0012_alter_user_first_name_max_length','2025-06-08 23:01:29.844491'),
(18,'core','0001_initial','2025-06-08 23:01:29.850934'),
(19,'core','0002_empresa_delete_mantenimiento_delete_repuesto_and_more','2025-06-08 23:01:29.857149'),
(20,'repuestos','0001_initial','2025-06-08 23:01:29.879522'),
(21,'repuestos','0002_alter_empresa_options_alter_repuesto_options_and_more','2025-06-08 23:01:29.912361'),
(22,'mantenimiento','0001_initial','2025-06-08 23:01:29.948335'),
(23,'mantenimiento','0002_vehiculo_fecha_proxima_revision_and_more','2025-06-08 23:01:30.003324'),
(24,'sessions','0001_initial','2025-06-08 23:01:30.009997'),
(25,'clientes','0001_initial','2025-06-08 23:28:12.868458'),
(26,'mantenimiento','0003_fix_cliente_field','2025-06-10 04:36:22.363255'),
(27,'mantenimiento','0004_alter_vehiculo_fecha_registro','2025-06-10 05:08:33.081953');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('9iu0k13bi0xmqmpa22wcluc5td3f00gx','.eJxVjEEOwiAQRe_C2hBgCAWX7j0DmWFAqgaS0q6Md9cmXej2v_f-S0Tc1hq3kZc4szgLLU6_G2F65LYDvmO7dZl6W5eZ5K7Igw557Zyfl8P9O6g46re2eUrBW0VgPCTixIy2-KC9cUbbom0ATQExUCCFWQE4BZbRYJnAgXh_AN-WN5Q:1uPSR5:HYsyQxrdk9swxffCAZptQOoR7Ttz1gHb0R3ax1Tppxg','2025-06-25 20:52:39.340294'),
('dqg00nbb0yf3k9g30lhif4pjyym6wbot','.eJxVjEEOwiAQRe_C2hBgCAWX7j0DmWFAqgaS0q6Md9cmXej2v_f-S0Tc1hq3kZc4szgLLU6_G2F65LYDvmO7dZl6W5eZ5K7Igw557Zyfl8P9O6g46re2eUrBW0VgPCTixIy2-KC9cUbbom0ATQExUCCFWQE4BZbRYJnAgXh_AN-WN5Q:1uPUeP:d0_IzA8p77TKsUi74fjAG35ap-WbPEegZf6-lVRxigg','2025-06-25 23:14:33.932899');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantenimiento_mantenimiento`
--

DROP TABLE IF EXISTS `mantenimiento_mantenimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mantenimiento_mantenimiento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tipo_mantenimiento` varchar(100) NOT NULL,
  `fecha_mantenimiento` date NOT NULL,
  `costo` decimal(10,2) NOT NULL,
  `vehiculo_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mantenimiento_manten_vehiculo_id_11b3a504_fk_mantenimi` (`vehiculo_id`),
  CONSTRAINT `mantenimiento_manten_vehiculo_id_11b3a504_fk_mantenimi` FOREIGN KEY (`vehiculo_id`) REFERENCES `mantenimiento_vehiculo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantenimiento_mantenimiento`
--

LOCK TABLES `mantenimiento_mantenimiento` WRITE;
/*!40000 ALTER TABLE `mantenimiento_mantenimiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `mantenimiento_mantenimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantenimiento_proximomantenimiento`
--

DROP TABLE IF EXISTS `mantenimiento_proximomantenimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mantenimiento_proximomantenimiento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_programada` date NOT NULL,
  `vehiculo_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mantenimiento_proxim_vehiculo_id_a2525bc8_fk_mantenimi` (`vehiculo_id`),
  CONSTRAINT `mantenimiento_proxim_vehiculo_id_a2525bc8_fk_mantenimi` FOREIGN KEY (`vehiculo_id`) REFERENCES `mantenimiento_vehiculo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantenimiento_proximomantenimiento`
--

LOCK TABLES `mantenimiento_proximomantenimiento` WRITE;
/*!40000 ALTER TABLE `mantenimiento_proximomantenimiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `mantenimiento_proximomantenimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantenimiento_repuestomantenimiento`
--

DROP TABLE IF EXISTS `mantenimiento_repuestomantenimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mantenimiento_repuestomantenimiento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cantidad` int(10) unsigned NOT NULL CHECK (`cantidad` >= 0),
  `mantenimiento_id` bigint(20) NOT NULL,
  `repuesto_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mantenimiento_repues_mantenimiento_id_b8a62ab9_fk_mantenimi` (`mantenimiento_id`),
  KEY `mantenimiento_repues_repuesto_id_24af5170_fk_repuestos` (`repuesto_id`),
  CONSTRAINT `mantenimiento_repues_mantenimiento_id_b8a62ab9_fk_mantenimi` FOREIGN KEY (`mantenimiento_id`) REFERENCES `mantenimiento_mantenimiento` (`id`),
  CONSTRAINT `mantenimiento_repues_repuesto_id_24af5170_fk_repuestos` FOREIGN KEY (`repuesto_id`) REFERENCES `repuestos_repuesto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantenimiento_repuestomantenimiento`
--

LOCK TABLES `mantenimiento_repuestomantenimiento` WRITE;
/*!40000 ALTER TABLE `mantenimiento_repuestomantenimiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `mantenimiento_repuestomantenimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantenimiento_vehiculo`
--

DROP TABLE IF EXISTS `mantenimiento_vehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mantenimiento_vehiculo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cliente` varchar(100) NOT NULL,
  `placa` varchar(20) NOT NULL,
  `foto_placa` varchar(100) DEFAULT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `anio` smallint(5) unsigned NOT NULL CHECK (`anio` >= 0),
  `tipo` varchar(50) NOT NULL,
  `costo` decimal(10,2) NOT NULL,
  `foto_frente` varchar(100) DEFAULT NULL,
  `foto_trasera` varchar(100) DEFAULT NULL,
  `foto_lateral1` varchar(100) DEFAULT NULL,
  `foto_lateral2` varchar(100) DEFAULT NULL,
  `fecha_proxima_revision` date DEFAULT NULL,
  `fecha_registro` date NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `placa` (`placa`),
  KEY `mantenimiento_vehicu_cliente_id_c8819982_fk_clientes_` (`cliente_id`),
  CONSTRAINT `mantenimiento_vehicu_cliente_id_c8819982_fk_clientes_` FOREIGN KEY (`cliente_id`) REFERENCES `clientes_cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantenimiento_vehiculo`
--

LOCK TABLES `mantenimiento_vehiculo` WRITE;
/*!40000 ALTER TABLE `mantenimiento_vehiculo` DISABLE KEYS */;
/*!40000 ALTER TABLE `mantenimiento_vehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repuestos_empresa`
--

DROP TABLE IF EXISTS `repuestos_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `repuestos_empresa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repuestos_empresa_nombre_51aa9453_uniq` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repuestos_empresa`
--

LOCK TABLES `repuestos_empresa` WRITE;
/*!40000 ALTER TABLE `repuestos_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `repuestos_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repuestos_repuesto`
--

DROP TABLE IF EXISTS `repuestos_repuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `repuestos_repuesto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int(10) unsigned NOT NULL,
  `empresa_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repuestos_repuesto_empresa_id_nombre_24863cb9_uniq` (`empresa_id`,`nombre`),
  CONSTRAINT `repuestos_repuesto_empresa_id_c7444406_fk_repuestos_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `repuestos_empresa` (`id`),
  CONSTRAINT `repuestos_repuesto_stock_7bae9a9c_check` CHECK (`stock` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repuestos_repuesto`
--

LOCK TABLES `repuestos_repuesto` WRITE;
/*!40000 ALTER TABLE `repuestos_repuesto` DISABLE KEYS */;
/*!40000 ALTER TABLE `repuestos_repuesto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-11 18:58:22
