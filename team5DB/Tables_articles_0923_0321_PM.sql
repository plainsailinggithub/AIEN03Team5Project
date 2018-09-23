-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: dbteam5
-- ------------------------------------------------------
-- Server version	5.7.19-log

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
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `last_modified_time` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` VALUES (1,'測試1','第一篇文章','2018-09-20 07:56:36.641570','2018-09-21 20:27:10.641570'),(2,'測試2','第2篇文章','2018-09-22 12:57:06.766471','2018-09-21 12:57:06.766471'),(5,'測試3','送出後關閉','2018-09-22 13:03:15.964895','2018-09-22 13:03:15.964895'),(7,'Test4 ','送出後關閉，\n而且還要改變按鈕的文字','2018-09-22 13:10:12.839805','2018-09-22 13:10:12.840800'),(8,'Test5','送出後 要清空文字','2018-09-22 13:14:40.747871','2018-09-22 13:14:40.747871'),(9,'test5','送出後清空文字','2018-09-22 13:15:25.084918','2018-09-22 13:15:25.084918'),(10,'改變Class','alter table name to articles','2018-09-22 13:17:02.959496','2018-09-22 13:17:02.959496'),(11,'After migrate','GOOD','2018-09-22 13:19:03.001563','2018-09-22 13:19:03.001563'),(12,'QQQQ','12345','2018-09-22 13:24:27.936736','2018-09-22 13:24:27.936736'),(13,'嘿嘿','測試時間','2018-09-22 17:14:38.153971','2018-09-22 17:14:38.153971'),(14,'明天醒來要測試時間','測試時間哦','2018-09-22 17:42:45.380171','2018-09-22 17:42:45.380171'),(15,'完成了~時間測試!!  ','不曉得天數如何耶!','2018-09-22 18:01:59.332960','2018-09-22 18:01:59.332960'),(16,'測試 json1','json','2018-09-23 01:57:06.966612','2018-09-23 01:57:06.966612'),(17,'Testing json2','json2','2018-09-23 02:00:44.249881','2018-09-23 02:00:44.249881'),(61,'完成ajax技術發佈文章','可以發佈訊息並且不用刷新整個頁面','2018-09-23 03:20:09.536687','2018-09-23 03:20:09.536687'),(62,'修正~','待會要修改 ajax刷新後的顯示時間','2018-09-23 03:24:58.964827','2018-09-23 03:24:58.964827'),(77,'沒想到serializers...','序列化只能直接操作資料庫裡面的資料，沒辦法把資料庫資料先讀取出來做加工再以加工過的資料去序列化。\n我只好再Javascript再轉換一次時間了...','2018-09-23 06:02:42.312277','2018-09-23 06:02:42.312277'),(78,'完成前端的時間計算','都是serializers 不能對資料庫的資料加工，所以我完成了前端對於資料庫裡面的UTC時間 做轉換再去計算時間差，方能正確顯示發佈文章是多久以前。','2018-09-23 07:07:54.939116','2018-09-23 07:07:54.939116'),(79,'測試不滿1分鐘的文章','如何??','2018-09-23 07:11:19.448343','2018-09-23 07:11:19.448343'),(80,'為了ajax','為了不刷新整個頁面來更新文章，server端的資料庫資訊沒辦法加工好再以序列化的方式傳送到client端，因此在client端接收好資訊再去對時間做處理加工!','2018-09-23 07:13:49.098207','2018-09-23 07:13:49.098207'),(81,'倒數60秒','看看分鐘有沒有加1','2018-09-23 07:16:51.722479','2018-09-23 07:16:51.722479'),(83,'時間刷新 有問題!','解決.. \n因為原本把now 放到function外面， 所以now 不會因為執行到function而被更新，難怪顯示還是舊的時間。','2018-09-23 07:21:00.716183','2018-09-23 07:21:00.716183');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-23 15:22:15
