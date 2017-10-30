/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50624
 Source Host           : localhost
 Source Database       : ShoppingDb

 Target Server Type    : MySQL
 Target Server Version : 50624
 File Encoding         : utf-8

 Date: 09/19/2016 09:38:40 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(8) COLLATE utf8_bin DEFAULT NULL,
  `favor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `favor_id` (`favor_id`),
  KEY `ix_category_name` (`name`),
  CONSTRAINT `category_ibfk_1` FOREIGN KEY (`favor_id`) REFERENCES `upper_category` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `category`
-- ----------------------------
BEGIN;
INSERT INTO `category` VALUES ('1', '床', '1'), ('2', '床垫', '1'), ('3', '床头柜', '1'), ('4', '衣柜', '1'), ('5', '沙发', '2'), ('6', '电视柜', '2'), ('7', '鞋柜', '2'), ('8', '屏风', '2'), ('9', '餐桌', '3'), ('10', '餐椅', '3'), ('11', '餐边柜', '3'), ('12', '吊灯', '4'), ('13', '壁灯', '4'), ('14', '吸顶灯', '4'), ('15', '台灯', '4'), ('16', '落地灯', '4'), ('17', '厨房龙头', '5'), ('18', '沥水篮', '5'), ('19', '角阀', '5'), ('20', '锁具', '6'), ('21', '门吸', '6'), ('22', '合页', '6'), ('23', '除湿机', '7'), ('24', '电子秤', '7'), ('25', '面包机', '7'), ('26', '按摩器', '7'), ('27', '净化器', '7'), ('28', '床单', '8'), ('29', '枕套', '8'), ('30', '凉席', '8'), ('31', '置物架', '9'), ('32', '挂钩', '9'), ('33', '简易衣柜', '9'), ('34', '纸巾盒', '9'), ('35', '毛巾家纺', '10'), ('36', '抱枕', '10'), ('37', '桌布', '10'), ('38', '毛巾家纺', '10');
COMMIT;

-- ----------------------------
--  Table structure for `city`
-- ----------------------------
DROP TABLE IF EXISTS `city`;
CREATE TABLE `city` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `province_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `province_id` (`province_id`),
  KEY `ix_city_caption` (`caption`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`province_id`) REFERENCES `province` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `city`
-- ----------------------------
BEGIN;
INSERT INTO `city` VALUES ('6', '石家庄', '1'), ('8', '邯郸', '1'), ('9', '大通', '9'), ('10', '0', '8'), ('11', '朝阳', '11');
COMMIT;

-- ----------------------------
--  Table structure for `comment`
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `content` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  `fine` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `product_id` (`product_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`nid`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `comment`
-- ----------------------------
BEGIN;
INSERT INTO `comment` VALUES ('1', '1', '2', '好，太好了', '2016-09-06 06:05:51', '1');
COMMIT;

-- ----------------------------
--  Table structure for `county`
-- ----------------------------
DROP TABLE IF EXISTS `county`;
CREATE TABLE `county` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `city_id` (`city_id`),
  KEY `ix_county_caption` (`caption`),
  CONSTRAINT `county_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `city` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `county`
-- ----------------------------
BEGIN;
INSERT INTO `county` VALUES ('1', '无名县', '6'), ('5', '鹿泉', '6'), ('6', '无极县', '6'), ('9', '天通苑', '11');
COMMIT;

-- ----------------------------
--  Table structure for `merchant`
-- ----------------------------
DROP TABLE IF EXISTS `merchant`;
CREATE TABLE `merchant` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `domain` char(8) COLLATE utf8_bin DEFAULT NULL,
  `business_mobile` char(11) COLLATE utf8_bin DEFAULT NULL,
  `qq` char(16) COLLATE utf8_bin DEFAULT NULL,
  `backend_mobile` char(11) COLLATE utf8_bin DEFAULT NULL,
  `county_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `business_phone` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `backend_phone` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `address` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `domain` (`domain`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `name` (`name`),
  KEY `county_id` (`county_id`),
  CONSTRAINT `merchant_ibfk_1` FOREIGN KEY (`county_id`) REFERENCES `county` (`nid`),
  CONSTRAINT `merchant_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `userinfo` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `merchant`
-- ----------------------------
BEGIN;
INSERT INTO `merchant` VALUES ('1', '1', '1', '3', '1', '1', '2', '奔驰中国', '3', '1', 'sdf'), ('10', '123', '123', '123', '123', '6', '1', 'python经销商', '123', '123', 'afsd'), ('14', 'jd', '123', '123', '123', '5', '3', 'JD自营', '123', '123', 'sdf');
COMMIT;

-- ----------------------------
--  Table structure for `price`
-- ----------------------------
DROP TABLE IF EXISTS `price`;
CREATE TABLE `price` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `standard` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `selling_price` decimal(10,0) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `price_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `price`
-- ----------------------------
BEGIN;
INSERT INTO `price` VALUES ('1', '进取版', '30', '28', '1'), ('2', '尊享版', '38', '35', '1'), ('9', '时尚版', '25000', '23000', '1'), ('10', '1*12', '19', '18', '20'), ('11', '2*20', '20', '18', '20'), ('12', '3*20', '40', '28', '20'), ('13', '1ML', '30', '30', '22');
COMMIT;

-- ----------------------------
--  Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `img` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `merchant_id` int(11) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  `memo` text COLLATE utf8_bin,
  PRIMARY KEY (`nid`),
  KEY `category_id` (`category_id`),
  KEY `merchant_id` (`merchant_id`),
  KEY `ix_product_title` (`title`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`nid`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`merchant_id`) REFERENCES `merchant` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `product`
-- ----------------------------
BEGIN;
INSERT INTO `product` VALUES ('1', '[卡富亚] 现代风格', 'Statics/Admin/Upload/1.jpg', '1', '14', '2016-09-14 13:51:10', null), ('20', '[彼岸阳光] 地中海风格 ', 'Statics/Admin/Upload/99141f6778a95b3dd31674d12ba0274c', '38', '14', '2016-09-14 00:00:00', null), ('21', '[凯撒豪庭] 欧式田园', 'Statics/Admin/Upload/99141f6778a95b3dd31674d12ba0274c', '27', '14', '2016-09-14 00:00:00', null), ('22', '[韩菲尔] 韩式田园', 'Statics/Admin/Upload/59eff2593defac76b5a93a7c05ff203d', '18', '14', '2016-09-16 00:00:00', null);
COMMIT;

-- ----------------------------
--  Table structure for `product_detail`
-- ----------------------------
DROP TABLE IF EXISTS `product_detail`;
CREATE TABLE `product_detail` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `value` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `product_detail_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `product_detail`
-- ----------------------------
BEGIN;
INSERT INTO `product_detail` VALUES ('13', 'asdfasdf', 'asdfasdf', '20'), ('14', 'asdfasasdf11df', 'asdfasdf', '20'), ('15', 'asdfasdf', 'asdfasdf', '21'), ('16', 'asdfasasdf11df', 'asdfasdf', '21'), ('17', 'test', 'b', '22');
COMMIT;

-- ----------------------------
--  Table structure for `product_img`
-- ----------------------------
DROP TABLE IF EXISTS `product_img`;
CREATE TABLE `product_img` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `src` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `product_img_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `product_img`
-- ----------------------------
BEGIN;
INSERT INTO `product_img` VALUES ('5', '20', 'Statics/Admin/Upload/928563a4c9b7404fa22337f4ece0fdcc'), ('6', '21', 'Statics/Admin/Upload/928563a4c9b7404fa22337f4ece0fdcc'), ('7', '22', 'Statics/Admin/Upload/d02ea21381591869a99785a91c0669a5'), ('8', '22', 'Statics/Admin/Upload/ec8dd2afe0650394cfe5ff3547d8994b');
COMMIT;

-- ----------------------------
--  Table structure for `product_view`
-- ----------------------------
DROP TABLE IF EXISTS `product_view`;
CREATE TABLE `product_view` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `ctime` date DEFAULT NULL,
  `timespan` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `product_id` (`product_id`),
  KEY `ix_product_view_ctime` (`ctime`),
  CONSTRAINT `product_view_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `product_view`
-- ----------------------------
BEGIN;
INSERT INTO `product_view` VALUES ('1', '1.1.1.1', '1', '2016-09-12', '1473868800000'), ('3', '1.1.1.1', '20', '2016-09-12', '1473868800000'), ('4', '1.1.1.2', '20', '2016-09-13', '1473868800000'), ('5', '1.1.1.2', '21', '2016-09-12', '1473868800000'), ('6', '1.1.1.12', '1', '2016-09-15', '1473868800000'), ('7', '1.1.1.11', '1', '2016-09-15', '1473868800000'), ('8', '1.1.1.1', '1', '2016-09-15', '1473868800000'), ('10', '1.1.1.1', '21', '2016-09-15', '1473868800000'), ('11', '1.1.1.1', '21', '2016-09-15', '1473868800000'), ('12', '1.1.1.1', '1', '2016-09-15', '1473868800000'), ('13', '127.0.0.1', '1', '2016-09-15', '1473868800000'), ('14', '127.0.0.1', '1', '2016-09-15', '1473955200000'), ('16', '127.0.0.1', '1', '2016-09-15', '1473955200000'), ('17', '127.0.0.1', '21', '2016-09-15', '1473955200000');
COMMIT;

-- ----------------------------
--  Table structure for `province`
-- ----------------------------
DROP TABLE IF EXISTS `province`;
CREATE TABLE `province` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `ix_province_caption` (`caption`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `province`
-- ----------------------------
BEGIN;
INSERT INTO `province` VALUES ('11', '北京'), ('9', '山东'), ('10', '山西'), ('1', '河北'), ('7', '河南'), ('8', '甘肃'), ('6', '陕西');
COMMIT;

-- ----------------------------
--  Table structure for `subsite`
-- ----------------------------
DROP TABLE IF EXISTS `subsite`;
CREATE TABLE `subsite` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(8) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `ix_subsite_caption` (`caption`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `subsite`
-- ----------------------------
BEGIN;
INSERT INTO `subsite` VALUES ('1', '家具城'), ('3', '家具家装'), ('2', '建材城');
COMMIT;

-- ----------------------------
--  Table structure for `super_product`
-- ----------------------------
DROP TABLE IF EXISTS `super_product`;
CREATE TABLE `super_product` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `price_id` int(11) DEFAULT NULL,
  `super_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `price_id` (`price_id`),
  CONSTRAINT `super_product_ibfk_1` FOREIGN KEY (`price_id`) REFERENCES `price` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `super_product`
-- ----------------------------
BEGIN;
INSERT INTO `super_product` VALUES ('1', '1', '1'), ('2', '2', '2');
COMMIT;

-- ----------------------------
--  Table structure for `upper_category`
-- ----------------------------
DROP TABLE IF EXISTS `upper_category`;
CREATE TABLE `upper_category` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(8) COLLATE utf8_bin DEFAULT NULL,
  `favor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `favor_id` (`favor_id`),
  KEY `ix_upper_category_caption` (`caption`),
  CONSTRAINT `upper_category_ibfk_1` FOREIGN KEY (`favor_id`) REFERENCES `subsite` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `upper_category`
-- ----------------------------
BEGIN;
INSERT INTO `upper_category` VALUES ('1', '卧室', '1'), ('2', '客厅', '1'), ('3', '餐厅', '1'), ('4', '灯饰照明', '2'), ('5', '厨房用品', '2'), ('6', '家装五金', '2'), ('7', '生活电器', '2'), ('8', '床上用品', '3'), ('9', '居家日用', '3'), ('10', '布艺织物', '3');
COMMIT;

-- ----------------------------
--  Table structure for `userinfo`
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `user_type` int(11) DEFAULT NULL,
  `vip` int(11) DEFAULT NULL,
  `username` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `password` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `email` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `ix_email_pwd` (`email`,`password`),
  KEY `ix_user_pwd` (`username`,`password`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `userinfo`
-- ----------------------------
BEGIN;
INSERT INTO `userinfo` VALUES ('1', '1', '1', 'wupeiqi1', '123', 'wupeiqi@live.com', '2016-09-06 23:27:25', '2016-09-04 23:27:31'), ('2', '1', '1', 'seven2', '123123', 'sfa@qq.com', '2016-09-12 16:15:56', '2016-09-05 16:16:03'), ('3', '1', '1', 'jd', '123123', 'jd@qq.com', null, null);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
