/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : web

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2017-06-03 10:18:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` tinyint(3) NOT NULL AUTO_INCREMENT,
  `adminname` varchar(20) DEFAULT NULL,
  `password` char(32) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------

-- ----------------------------
-- Table structure for album
-- ----------------------------
DROP TABLE IF EXISTS `album`;
CREATE TABLE `album` (
  `id` int(10) NOT NULL,
  `itemid` int(10) DEFAULT NULL,
  `albumPath` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of album
-- ----------------------------
INSERT INTO `album` VALUES ('1', '1', 'https://img14.360buyimg.com/n1/s200x200_jfs/t1705/189/702227414/177982/cc8c12f0/55dab54dN5271c377.jpg');
INSERT INTO `album` VALUES ('2', '2', 'https://img13.360buyimg.com/n1/s200x200_jfs/t3649/55/395326731/88171/1b30b84c/580828d5Nec0f968a.jpg');
INSERT INTO `album` VALUES ('3', '3', 'https://img14.360buyimg.com/n1/s200x200_jfs/t3379/335/581340649/736534/40f9b36f/580f2909N8dd47a7f.jpg');
INSERT INTO `album` VALUES ('4', '4', 'https://img10.360buyimg.com/n1/jfs/t4480/31/2124371143/141939/2b6ba304/58ec53f0Nb54303b7.jpg');
INSERT INTO `album` VALUES ('5', '5', 'https://img11.360buyimg.com/n2/jfs/t5446/105/2223917803/564305/22d30663/591922a1N97297e79.jpg');
INSERT INTO `album` VALUES ('6', '6', 'http://img3x5.ddimg.cn/69/27/463785-1_b_0.jpg');
INSERT INTO `album` VALUES ('7', '7', 'https://img10.360buyimg.com/n1/s200x200_jfs/t5806/356/2315783905/94993/64de3327/592f8178N34961a13.jpg');
INSERT INTO `album` VALUES ('8', '8', 'https://img14.360buyimg.com/n1/s200x200_jfs/t163/72/264335581/216774/13cdbb3c/5385a3caNed165ce7.jpg');
INSERT INTO `album` VALUES ('9', '9', 'https://img14.360buyimg.com/n1/s200x200_g13/M08/03/10/rBEhVFHSI4wIAAAAAAbgPuMWOA0AAAr8wAp0m8ABuBW472.jpg');
INSERT INTO `album` VALUES ('10', '10', 'https://img10.360buyimg.com/n1/s200x200_jfs/t4213/272/2285652491/415515/a70671b8/58cf7dfdN9ab53328.jpg');
INSERT INTO `album` VALUES ('11', '11', 'https://img10.360buyimg.com/n1/s200x200_jfs/t1450/110/854073223/57979/60415019/55af62a2N7a243064.jpg');
INSERT INTO `album` VALUES ('12', '12', 'https://img10.360buyimg.com/n1/s200x200_16016/64420535-281c-4a3a-903f-a3af2866ae12.jpg');
INSERT INTO `album` VALUES ('13', '13', 'https://img11.360buyimg.com/n1/s200x200_jfs/t3109/313/6277362508/244668/dea10b5b/58a179d7N59d818d8.jpg');
INSERT INTO `album` VALUES ('14', '14', 'https://img13.360buyimg.com/n1/s200x200_jfs/t3010/156/2082219212/384816/5a17b189/57d25dc9N447dead0.jpg');
INSERT INTO `album` VALUES ('15', '15', 'https://img12.360buyimg.com/n1/s200x200_jfs/t4069/152/953837445/478256/9775ba91/58638cc4N33cecbec.jpg');
INSERT INTO `album` VALUES ('16', '16', 'https://img13.360buyimg.com/n1/s200x200_jfs/t5203/171/1861884096/266161/3665c35c/59157fe5Na627a36e.jpg');
INSERT INTO `album` VALUES ('17', '17', 'https://img11.360buyimg.com/n1/s200x200_jfs/t6001/119/615927963/120287/463d86e/592aa30cN80007ac2.jpg');
INSERT INTO `album` VALUES ('18', '18', 'https://img13.360buyimg.com/n1/s200x200_jfs/t5518/119/2393591974/306451/f61ba8fe/591a6d4aN8880cf45.jpg');
INSERT INTO `album` VALUES ('19', '19', 'https://img14.360buyimg.com/n7/jfs/t3268/288/6363948392/318439/4496f6b6/58a568dcN5f020ef8.jpg');
INSERT INTO `album` VALUES ('20', '20', 'https://img10.360buyimg.com/n1/s200x200_jfs/t1072/360/753920079/115195/ab0de181/55417f83Nac1cef84.jpg');
INSERT INTO `album` VALUES ('21', '21', 'https://img11.360buyimg.com/n1/s200x200_jfs/t4777/304/1380337673/474287/2b0b9e70/58f025a9N8eec6013.jpg');
INSERT INTO `album` VALUES ('22', '22', 'https://img14.360buyimg.com/n1/s200x200_jfs/t2332/358/2131899640/158649/cec8e44c/56a9ca1cNe783b6e9.jpg');
INSERT INTO `album` VALUES ('23', '23', 'https://img13.360buyimg.com/n1/s200x200_jfs/t2929/86/851647888/279537/6e1b4c96/576b3628N2d6066b0.jpg');
INSERT INTO `album` VALUES ('24', '24', 'https://img10.360buyimg.com/n1/s200x200_jfs/t547/214/600175092/450649/24f1046b/5476935dN004b868e.jpg');
INSERT INTO `album` VALUES ('25', '25', 'https://img14.360buyimg.com/n2/jfs/t5044/82/1250612303/880769/32a544e1/58ef15f3N133108bb.jpg');
INSERT INTO `album` VALUES ('26', '26', 'https://img13.360buyimg.com/n1/s200x200_jfs/t3253/112/5098298194/133307/8a3047d7/586292cbNb47cb9e4.jpg');
INSERT INTO `album` VALUES ('27', '27', 'https://img12.360buyimg.com/n1/s200x200_jfs/t913/311/845504058/222616/c0045e14/554fff90N943f7b2e.jpg');
INSERT INTO `album` VALUES ('28', '28', 'https://img11.360buyimg.com/n1/s200x200_jfs/t3898/83/1395808102/266936/31550647/5878229cN4ca55d86.jpg');
INSERT INTO `album` VALUES ('29', '29', 'https://img12.360buyimg.com/n7/jfs/t1978/278/1069164635/252628/33977a68/563c6928Nc8010b2d.jpg');
INSERT INTO `album` VALUES ('30', '30', 'https://img14.360buyimg.com/n2/jfs/t1024/259/910297718/226016/cd2f2cbf/5566b579Nb8d89281.jpg');
INSERT INTO `album` VALUES ('31', '31', 'https://img11.360buyimg.com/n2/jfs/t4978/97/1060920952/653844/43e883da/58ec77faN242cae8c.jpg');
INSERT INTO `album` VALUES ('32', '32', 'https://img13.360buyimg.com/n1/s200x200_jfs/t6019/209/14441049/100016/48767e78/59250cafNdfe5a947.jpg');
INSERT INTO `album` VALUES ('33', '33', 'https://img11.360buyimg.com/n2/jfs/t3169/225/1946473045/156501/8c5db6f1/57d79a06N53644292.jpg');
INSERT INTO `album` VALUES ('34', '34', 'https://img11.360buyimg.com/n2/jfs/t3967/195/1872770277/306842/ed0b12/589bd67cN02716f4d.jpg');
INSERT INTO `album` VALUES ('35', '35', 'https://img11.360buyimg.com/n2/jfs/t2449/32/1904624605/116943/b48c0d6e/567ca124N41e89187.jpg');
INSERT INTO `album` VALUES ('36', '36', 'https://img13.360buyimg.com/n2/jfs/t148/102/66196953/408648/c490cd41/537d9094N892888f6.jpg');
INSERT INTO `album` VALUES ('37', '37', 'https://img11.360buyimg.com/n7/jfs/t2017/24/1670616343/820024/3b2b4346/566e5c81N619ec708.jpg');
INSERT INTO `album` VALUES ('38', '38', 'https://img13.360buyimg.com/n1/jfs/t2704/183/52516008/423718/cda81acc/56fe1020Nd281ae5c.jpg');
INSERT INTO `album` VALUES ('39', '39', 'https://img13.360buyimg.com/n1/s200x200_jfs/t5455/365/383900597/543696/b464fcf5/58febcbaN74dfae1c.jpg');
INSERT INTO `album` VALUES ('40', '40', 'https://img11.360buyimg.com/n1/s200x200_g5/M00/02/09/rBEIDE_QFwsIAAAAAAE4PF5pELMAAActAFRcoIAAThU532.jpg');

-- ----------------------------
-- Table structure for item
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` varchar(10) DEFAULT NULL,
  `pName` varchar(50) DEFAULT NULL,
  `writer` varchar(20) DEFAULT NULL,
  `pSn` varchar(10) DEFAULT NULL,
  `cld` varchar(5) DEFAULT NULL,
  `pNum` varchar(10) DEFAULT NULL,
  `mPrice` float(20,0) DEFAULT NULL,
  `iPrice` float(20,0) DEFAULT NULL,
  `pDesc` varchar(10000) DEFAULT NULL,
  `plmg` varchar(5000) DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `pubTime` varchar(30) DEFAULT NULL,
  `descpic` varchar(5000) DEFAULT NULL,
  `isHot` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of item
-- ----------------------------
INSERT INTO `item` VALUES ('21', '《三国演义》', '罗贯中', '21', '1', '49', '38', '30', '三国时期是个激动人心的时代。陈寿的《三国志》和裴松之的注是纪录这一时代的最原始材料。从晋朝到唐宋，民间关于三国的传说就一直没有中断过，以各种形式不停歇地上演着、评说着刘备和曹操的故事，男女老幼无不喜欢，流传极广。元末明初，山西太原人罗贯中以正史为框架，在十分丰富的民间传说的基础上，创作了《三国演义》这部不朽的巨著。', 'https://img11.360buyimg.com/n1/s200x200_jfs/t4777/304/1380337673/474287/2b0b9e70/58f025a9N8eec6013.jpg', '人民文学出版社', '2010-09-01', 'https://img30.360buyimg.com/vc/jfs/t2422/224/2101999009/142998/83bece94/56b049d4Ne0279c92.jpg', '101');
INSERT INTO `item` VALUES ('22', '《彷徨》', '鲁迅', '22', '2', '999', '23', '15', '', 'https://img14.360buyimg.com/n1/s200x200_jfs/t2332/358/2131899640/158649/cec8e44c/56a9ca1cNe783b6e9.jpg', '天津人民出版社', '2010/5/13', 'https://img30.360buyimg.com/vc/jfs/t2224/3/2523955772/402532/2f2bb2a1/56de9a63N7145e5a6.jpg', '100');
INSERT INTO `item` VALUES ('23', '《呐喊》', '鲁迅', '23', '2', '999', '23', '15', '', 'https://img13.360buyimg.com/n1/s200x200_jfs/t2929/86/851647888/279537/6e1b4c96/576b3628N2d6066b0.jpg', '陕西师范大学出版社', '2012/3/1', 'https://img30.360buyimg.com/vc/jfs/t3157/6/4157347449/441444/f8c53ba6/58365a0eNd39445a9.jpg', '100');
INSERT INTO `item` VALUES ('24', '《相对论》', '阿尔伯特·爱因斯坦', '24', '3', '999', '34', '27', ' 　　看懂星际穿越的必读读物！<br>　　爱因斯坦上帝式的思维方式永远都是迷人的。<br>　　开启全新宇宙观的巨著永远都能满足人类对宇宙的好奇心。<br>　　《相对论》是爱因斯坦的不朽巨著，包括《狭义相对论》和《广义相对论》都汇集于本书中。本书彻底颠覆了经典物理学，成为现代及未来科学的伟大的奠基之作。开创了物理学、航天科学、天文学等高新学科的新纪元。<br>　　狭义相对论。<br>　　广义相对论<br>　　宇宙空间的体积是有限的，是一个弯曲封闭体，类似于一个球面，这一封闭体不随时间的推移而变化。<br>　　成功公式：W=X+Y+Z。W代表成功，X代表刻苦，Y代表正确的方法，Z代表少说空话。<br>　　谁是二十世纪zui伟大的人？美国《时代》周刊通过数百位当世名人的甄选，爱因斯坦、富兰克林罗斯福以及甘地得票很高。<br>　　万有引力是由于物质的存在和分布，使时间和空间的性质不均匀所引起的。<br><br>            </div>', 'https://img10.360buyimg.com/n1/s200x200_jfs/t547/214/600175092/450649/24f1046b/5476935dN004b868e.jpg', '江苏人民出版社', '2011-03-01', 'https://img30.360buyimg.com/vc/jfs/t2491/230/1420274918/201578/a7af39a9/56a07624N59ffe484.jpg', '100');
INSERT INTO `item` VALUES ('25', '《薛定谔生命物理学讲义》', '埃尔温·薛定谔 ', '25', '3', '999', '40', '36', '', 'https://img14.360buyimg.com/n2/jfs/t5044/82/1250612303/880769/32a544e1/58ef15f3N133108bb.jpg', '北京联合出版公司', '2017-04-01', 'https://img30.360buyimg.com/vc/jfs/t4678/316/2426362689/741953/68b65f1c/58ef16ecNcc46bf45.jpg', '100');
INSERT INTO `item` VALUES ('26', '《东周列国志》', '司马迁', '26', '4', '99', '40', '32', '', 'https://img13.360buyimg.com/n1/s200x200_jfs/t3253/112/5098298194/133307/8a3047d7/586292cbNb47cb9e4.jpg', '西苑出版社', '2016-04-01', 'https://img30.360buyimg.com/vc/jfs/t3163/286/5147815584/947971/fe3545db/5863d048Na7e4975b.jpg', '101');
INSERT INTO `item` VALUES ('27', '《明史》', '南炳文，汤纲', '27', '4', '99', '40', '32', '　《明史（套装上下册）》较为系统地论述分析了明代政治、经济、军事、民族关系、中外关系的发展状况和明代的阶级状况。明朝是我国历史上的一个重要时期，这一历史时期，社会生产力、社会经济得到了较大的发展，商品经济的发展突破了以往历史上任何一个时代，由此而引起生产关系方面产生了微妙的变化。作者认为这种变化的出现，是资本主义萌芽产生的标志，而这一变化在当时社会和生产部门中都有较为明显的表现。《明史（套装上下册）》以内容丰富、史料翔实见长，在许多史实的阐述方面，其翔实、详细的程度为同类书所不及。', 'https://img12.360buyimg.com/n1/s200x200_jfs/t913/311/845504058/222616/c0045e14/554fff90N943f7b2e.jpg', '上海人民出版社', '2014-12-01', '', '100');
INSERT INTO `item` VALUES ('28', '《实验班》', '《实验班提优训练》编写组，严军', '28', '5', '199', '78', '67', '', 'https://img11.360buyimg.com/n1/s200x200_jfs/t3898/83/1395808102/266936/31550647/5878229cN4ca55d86.jpg', '江苏人民出版社', '2015/3/27', 'https://img10.360buyimg.com/bookdetail/jfs/t5440/225/2001797141/808593/c60becb8/59168753Nac211c9e.jpg', '100');
INSERT INTO `item` VALUES ('29', '《小王子》', '安东尼·德·圣-埃克苏佩里 ', '29', '5', '999', '30', '21', '', 'https://img12.360buyimg.com/n7/jfs/t1978/278/1069164635/252628/33977a68/563c6928Nc8010b2d.jpg', '星球地图出版社', '2015/3/1', 'https://img30.360buyimg.com/vc/jfs/t2467/349/985131162/330838/8c689309/563c6a26Ndaab8485.jpg', '100');
INSERT INTO `item` VALUES ('31', '《智能革命》', '李彦宏', '31', '6', '999', '68', '50', '', 'https://img11.360buyimg.com/n2/jfs/t4978/97/1060920952/653844/43e883da/58ec77faN242cae8c.jpg', '中信出版集团', '2017/4/1 ', 'https://img30.360buyimg.com/vc/jfs/t5440/239/2573554640/422001/4281ab5a/591c1c83N949d200a.jpg', '101');
INSERT INTO `item` VALUES ('30', '《博弈论》', '朱·弗登博格', '30', '6', '999', '28', '19', '', 'https://img14.360buyimg.com/n2/jfs/t1024/259/910297718/226016/cd2f2cbf/5566b579Nb8d89281.jpg', '中国人民大学出版社', '2017/5/1', 'https://img30.360buyimg.com/vc/jfs/t634/106/217413431/110261/c8ca0743/54572340N5dfac7e9.jpg', '103');
INSERT INTO `item` VALUES ('32', '《大满足！就爱锅料理》', '林江', '32', '7', '999', '49', '33', '', 'https://img13.360buyimg.com/n1/s200x200_jfs/t6019/209/14441049/100016/48767e78/59250cafNdfe5a947.jpg', '中信出版集团', '2017/5/25', 'https://img30.360buyimg.com/vc/jfs/t4993/181/739952132/338542/a2c1b7b0/58e75964N6b193f33.jpg', '100');
INSERT INTO `item` VALUES ('33', '《改变你的服装，改变你的生活》', '乔治·布雷西亚', '33', '7', '999', '32', '27', '', 'https://img11.360buyimg.com/n2/jfs/t3169/225/1946473045/156501/8c5db6f1/57d79a06N53644292.jpg', '北京联合出版公司', '2015-09-01', 'https://img30.360buyimg.com/vc/jfs/t3226/25/2387359372/300354/33de428/57e0e310Nb5286035.jpg', '90');
INSERT INTO `item` VALUES ('34', '《任正非和华为 》', '余胜海', '34', '8', '999', '32', '24', '', 'https://img11.360buyimg.com/n2/jfs/t3967/195/1872770277/306842/ed0b12/589bd67cN02716f4d.jpg', '长江文艺出版社', '2017年03月 ', 'https://img30.360buyimg.com/vc/jfs/t3196/140/6047192469/298358/813ef50b/589c008bNba36991a.jpg', '100');
INSERT INTO `item` VALUES ('35', '《世界很大，幸好有你》', '杨澜', '35', '8', '999', '21', '16', '杨澜作品', 'https://img11.360buyimg.com/n2/jfs/t2449/32/1904624605/116943/b48c0d6e/567ca124N41e89187.jpg', '江苏凤凰文艺出版社', '2016-01-01', 'https://img10.360buyimg.com/bookDetail/jfs/t2554/342/1099135146/304925/51e338e3/568a0d85Nd6a8f5ad.jpg', '100');
INSERT INTO `item` VALUES ('36', '《马云：我的世界永不言败》', '张燕', '36', '8', '999', '35', '26', '', 'https://img13.360buyimg.com/n2/jfs/t148/102/66196953/408648/c490cd41/537d9094N892888f6.jpg', '企业管理出版社', '2017年03月 ', 'https://img30.360buyimg.com/vc/jfs/t1852/280/2161976299/179519/f3e2d1c6/56a1f551N7141ff1a.jpg', '101');
INSERT INTO `item` VALUES ('37', '《一品芝麻狐》', '王溥', '37', '9', '999', '45', '30', '', 'https://img11.360buyimg.com/n7/jfs/t2017/24/1670616343/820024/3b2b4346/566e5c81N619ec708.jpg', '中国友谊出版公司', '2016-01-01', 'https://img30.360buyimg.com/vc/jfs/t3277/43/2619208894/402713/8dc96b70/57e398c4N9828c552.jpg', '101');
INSERT INTO `item` VALUES ('38', '《一条狗套装》', '使徒子', '38', '9', '999', '68', '51', '', 'https://img13.360buyimg.com/n1/jfs/t2704/183/52516008/423718/cda81acc/56fe1020Nd281ae5c.jpg', '中国友谊出版公司', '2016-04-01', 'https://img30.360buyimg.com/vc/jfs/t2617/301/222368690/205409/bf53419d/5707ea1cNbf299c74.jpg', '100');
INSERT INTO `item` VALUES ('40', '《诛仙》', '萧鼎', '40', '10', '999', '22', '20', '', 'https://img11.360buyimg.com/n1/s200x200_g5/M00/02/09/rBEIDE_QFwsIAAAAAAE4PF5pELMAAActAFRcoIAAThU532.jpg', '北京联合出版公司', '2012-06-01', 'https://img10.360buyimg.com/bookDetail/g5/M01/02/09/rBEIC0_QF34IAAAAAAGynbhQR0AAAActQLQujwAAbK1365.jpg', '100');
INSERT INTO `item` VALUES ('39', '《大主宰》', '天蚕土豆', '39', '10', '999', '20', '19', '<p>★★★</p>\r\n<p>斗气之上，灵气为王</p>\r\n<p>苍穹之下，唯我主宰</p>\r\n<p>2014第九届作家榜 网络作家榜第三名</p>\r\n<p>天蚕土豆</p>\r\n<p>首创灵气传奇，缔造*荣耀之冕</p>\r\n<p>&nbsp;</p>\r\n<p>★★★</p>\r\n<p>百万畅销榜首</p>\r\n<p>北域争霸，新主耀目，诛魔之王扬威名</p>\r\n<p>白龙灵珠，天尊引动，至尊之路得始成</p>\r\n<p>&nbsp;</p>\r\n<p>★★★</p>\r\n<p><span style=\"font-family: 宋体;\">周洪滨、任翔、</span>JOE</p>\r\n<p>同名改编漫画正在火热连载中。</p>&nbsp;', 'https://img13.360buyimg.com/n1/s200x200_jfs/t5455/365/383900597/543696/b464fcf5/58febcbaN74dfae1c.jpg', '湖南人民出版社', '2017/1/1', 'http://img57.ddimg.cn/99999990000866907.jpg', '100');
INSERT INTO `item` VALUES ('1', '《三体》', '刘慈欣', '1', '1', '49', '93', '86', '慈欣基于科学事实，用大胆的想象和严谨的推断，在三体星系行星中构建了一个外星文明形态，并描绘了该文明不可捉摸的数百次的毁灭和重生。', 'https://img14.360buyimg.com/n1/s200x200_jfs/t1705/189/702227414/177982/cc8c12f0/55dab54dN5271c377.jpg', '重庆出版社', '2014/10/17', 'https://img30.360buyimg.com/vc/jfs/t3139/355/8837750532/3815790/b0172232/58c8fe78N732803e2.jpg', '100');
INSERT INTO `item` VALUES ('2', '《史记》', '司马迁', '2', '4', '99', '98', '75', '陈寅恪先生再传弟子、中国《史记》研究会名誉会长、中国《史记》研究大家韩兆琦先生潜心注释，精装全本，持续畅销，好评如潮。 ', 'https://img13.360buyimg.com/n1/s200x200_jfs/t3649/55/395326731/88171/1b30b84c/580828d5Nec0f968a.jpg', '岳麓书社', '2011年07月 ', 'https://img30.360buyimg.com/popWareDetail/jfs/t3640/318/411641387/84107/6e7359f2/58082a66N68dcaef3.jpg', '100');
INSERT INTO `item` VALUES ('3', '《考点同步解读》', '王后雄', '3', '5', '199', '29', '25', '《考点同步解读：高中物理（必修1 新高考 学考+选考 浙江专用 新课标）》是高中物理知识与初中物理知识的衔接，所讲知识是高中段较为简单易懂的。全书共分为四个章节：运动的描述、匀变速直线运动、相互作用、牛顿运动定律。其中质点的直线运动较为基础，近几年都有考到，相互作用考查共点力平衡、力的合成与分解等知识。牛顿运动定律是高考必考内容，考查学生对惯性的理解及对牛顿第1定律的理解，非常重要，需要牢牢掌握。', 'https://img14.360buyimg.com/n1/s200x200_jfs/t3379/335/581340649/736534/40f9b36f/580f2909N8dd47a7f.jpg', '华中师范大学出版社', '2016-10-01', '', '100');
INSERT INTO `item` VALUES ('4', '《五年高考三年模拟》', '曲一线', '4', '5', '999', '53', '50', '', 'https://img10.360buyimg.com/n1/jfs/t4480/31/2124371143/141939/2b6ba304/58ec53f0Nb54303b7.jpg', '教育科学出版社', '2017-02-01', 'https://img30.360buyimg.com/popWareDetail/jfs/t5017/94/963263315/412376/40a15251/58eb30efNb756c95d.jpg', '100');
INSERT INTO `item` VALUES ('5', '《科学声音.物理之美》', '汪洁，吴京平', '5', '3', '999', '97', '56', '', 'https://img11.360buyimg.com/n2/jfs/t5446/105/2223917803/564305/22d30663/591922a1N97297e79.jpg', '北京时代华文书局', '2017/4/23', 'https://img30.360buyimg.com/vc/jfs/t5524/293/1853892603/624161/ccadf903/59151944Nc987ff69.jpg', '100');
INSERT INTO `item` VALUES ('6', '《时间简史》', '史蒂芬·霍金', '6', '3', '999', '45', '31', '', 'http://img3x5.ddimg.cn/69/27/463785-1_b_0.jpg', '湖南科学技术出版社', '2017/5/1', 'https://img30.360buyimg.com/vc/jfs/t5401/192/2252932765/249011/6bd5a164/5919735fN31cc57fd.jpg', '100');
INSERT INTO `item` VALUES ('7', '《龙族4》', '江南', '7', '1', '99', '35', '16', '《龙族IV奥丁之渊》：路明非成为了卡塞尔学院的新任学生会主席，偶然中路明非发现，楚子航消失了，除了他，其他人都不记得有这个人曾经存在，并怀疑他在任务中脑震荡。路明非在痛苦中挣扎，找到远在小岛上上新娘课程的诺诺。他并不知道在他离开学院的DANG*当天，学院遭受袭击，蒙受重大损失，而他是嫌疑人。这一切充满了诡异，而芬格尔从古巴千里迢迢赶来助阵，由此路明非和芬格尔、诺诺决定回到了楚子航的故乡北京，寻找楚子航曾经留下的痕迹。却在无意中与诺诺闯入楚子航DANG*当年遇过的尼伯龙根。奥丁再次出现，长枪直指诺诺。路明非为了救诺诺，求助路明泽……', 'https://img10.360buyimg.com/n1/s200x200_jfs/t5806/356/2315783905/94993/64de3327/592f8178N34961a13.jpg', '长江出版社', '2017/4/1', '', '90');
INSERT INTO `item` VALUES ('8', '《朝花夕拾》', '鲁迅', '8', '2', '999', '23', '15', '', 'https://img14.360buyimg.com/n1/s200x200_jfs/t163/72/264335581/216774/13cdbb3c/5385a3caNed165ce7.jpg', '陕西师范大学出版社', '2017/5/1', 'https://img30.360buyimg.com/vc/jfs/t3505/70/968931788/469353/cff4ad8f/5819487bN8fd85ca2.jpg', '100');
INSERT INTO `item` VALUES ('9', '《家》', '巴金', '9', '2', '999', '33', '32', '《家》在巴金众多的小说中，由《家》、《春》、《秋》三部长篇组成的《激流三部曲》，是成就高、影响大的一部巨制。作品取材于中国的一个封建的大家庭，通过这个大家庭的没落与分化来描写封建宗法制度的崩溃和革命潮流在青年一代中的激荡，这部作品奠定了巴金在中国文坛中的巨匠地位。', 'https://img14.360buyimg.com/n1/s200x200_g13/M08/03/10/rBEhVFHSI4wIAAAAAAbgPuMWOA0AAAr8wAp0m8ABuBW472.jpg', '人民文学出版社', '2017/5/1', '', '100');
INSERT INTO `item` VALUES ('10', '《资治通鉴》', '司马光', '10', '4', '999', '136', '198', '', 'https://img10.360buyimg.com/n1/s200x200_jfs/t4213/272/2285652491/415515/a70671b8/58cf7dfdN9ab53328.jpg', '北京联合出版公司', '2017/4/11', 'https://img30.360buyimg.com/vc/jfs/t2848/263/3241184492/413858/7b641b09/578345d5N2bbd672c.jpg', '100');
INSERT INTO `item` VALUES ('11', '《资本论》', '马克思', '11', '6', '999', '28', '19', '', 'https://img10.360buyimg.com/n1/s200x200_jfs/t1450/110/854073223/57979/60415019/55af62a2N7a243064.jpg', ' 菁韵创世图书专营店', '2017/5/1', '', '100');
INSERT INTO `item` VALUES ('12', '《经济学人》', 'ECO团队', '12', '6', '999', '25', '24', '《经济学人（MOOK1101）》是英国《经济学人》（TheEconomist）杂志的经济金融、社会类特别报道与精粹文章选集，由ECO团队主编。主要内容简介如下：第一部分是“创业精神的特别报道”；第二部分是“关于世界经济的特别报道”；第三部分是“新兴市场中产阶级的特别报道”。', 'https://img10.360buyimg.com/n1/s200x200_16016/64420535-281c-4a3a-903f-a3af2866ae12.jpg', ' 法律出版社', '2017/4/1 ', '', '100');
INSERT INTO `item` VALUES ('13', '《知音漫客》', '知音漫客', '13', '9', '999', '115', '31', '', 'https://img11.360buyimg.com/n1/s200x200_jfs/t3109/313/6277362508/244668/dea10b5b/58a179d7N59d818d8.jpg', '知音漫客', '2017/4/15', 'https://img30.360buyimg.com/popWaterMark/jfs/t4840/28/2312803908/117649/4968d19f/58fd8d30N433e18f3.jpg', '100');
INSERT INTO `item` VALUES ('14', '《漫画party》', ' 悦刊网', '14', '9', '999', '45', '21', '', 'https://img13.360buyimg.com/n1/s200x200_jfs/t3010/156/2082219212/384816/5a17b189/57d25dc9N447dead0.jpg', '北京', '2017/5/25', 'https://img30.360buyimg.com/popWareDetail/jfs/t1792/150/2119139780/160409/1b7c8ae2/5628805bN462eb48a.jpg', '100');
INSERT INTO `item` VALUES ('15', '《完美世界》', '辰东', '15', '10', '999', '417', '272', '本册中，石昊先是 大败天人族初代，被齐道临高调宣布为Z尊道场W一传人，后又为护清漪大战仙殿传人次身，一时风头尽显。离开火州、天仙州区域后，石昊来到罪州，在此发现了 自己罪血后人这一层身份。随后，石昊与火灵儿感动重逢，却适逢三千州天才大决战正式开启，二人只得依依惜别。石昊在赛中大显神威，成功进入“仙古”，并冒 着生命危险另辟成神之道，终浴火重生、初步成神！此外，石昊还与齐道临共探三世铜棺与仙矿，观得种种异象，似乎预示着璀璨末世的到来……', 'https://img12.360buyimg.com/n1/s200x200_jfs/t4069/152/953837445/478256/9775ba91/58638cc4N33cecbec.jpg', '湖南少年儿童出版社', '2017/1/1', '', '100');
INSERT INTO `item` VALUES ('16', '《龙王传说》', '唐家三少', '16', '10', '999', '408', '275', '', 'https://img13.360buyimg.com/n1/s200x200_jfs/t5203/171/1861884096/266161/3665c35c/59157fe5Na627a36e.jpg', '湖南少年儿童出版社', '2017/1/1', 'https://img30.360buyimg.com/popWareDetail/jfs/t2710/363/4342644705/350764/dd366dd0/57b813feN1a84645a.jpg', '100');
INSERT INTO `item` VALUES ('17', '《去旅行》', '阿梅莉·卡斯唐（法）纳塔莉·佩泰斯塔', '17', '7', '999', '108', '86', '', 'https://img11.360buyimg.com/n1/s200x200_jfs/t6001/119/615927963/120287/463d86e/592aa30cN80007ac2.jpg', '', '2017/5/25', 'https://img30.360buyimg.com/popWaterMark/jfs/t5887/208/1911022361/281798/d5c3edd9/592aa38bN5ce63acd.jpg', '100');
INSERT INTO `item` VALUES ('18', '《外婆的道歉信》', '弗雷德里克巴·克曼', '18', '7', '999', '32', '21', '外婆说，要大笑要做梦要与众不同。人生是一场伟大的冒险。作者巴克曼位列美国亚马逊文学榜首，当选瑞典年度作家。该书上市后连续霸占《纽约时报》畅销榜50周。巴克曼让我们爱上这个活泼过头的外婆，也重新爱上生活', 'https://img13.360buyimg.com/n1/s200x200_jfs/t5518/119/2393591974/306451/f61ba8fe/591a6d4aN8880cf45.jpg', '天津人民出版社', '2017年03月 ', '../static/images/goods/waipo_desc.jpg', '91');
INSERT INTO `item` VALUES ('19', '《周星驰》', '橙花', '19', '8', '999', '40', '26', '周星驰：做人如果没有梦想，跟咸鱼有什么分别', 'https://img14.360buyimg.com/n7/jfs/t3268/288/6363948392/318439/4496f6b6/58a568dcN5f020ef8.jpg', '华文出版社', '2017年03月 ', 'https://img30.360buyimg.com/vc/jfs/t5251/52/1518433116/836295/e1ae262e/59117ad6N906385cb.jpg', '100');
INSERT INTO `item` VALUES ('20', '《钢铁是怎样练成的》', '尼古拉·奥斯特洛夫斯基', '20', '1', '49', '36', '20', '《新课标必读·永远的经典：钢铁是怎样练成的》主要讲述了主人公保尔·柯察金如何从一个普通青年成长为一名优秀的布尔什维克主义战士的过程。保尔的经历是那个革命年代青年的缩影，他那舍己为人、勇于斗争以及忠诚无私的爱国主义精神，从一开始便超越时空，跨过国界，深深地影响了几代人，尤其是鼓舞着一代代的青年人为自己的国家和理想而奋斗。经典永恒，因时间的沉淀而显现出更无穷的魅力。', 'https://img10.360buyimg.com/n1/s200x200_jfs/t1072/360/753920079/115195/ab0de181/55417f83Nac1cef84.jpg', '中国工人出版社', '2014/10/17', '', '98');

-- ----------------------------
-- Table structure for kinds
-- ----------------------------
DROP TABLE IF EXISTS `kinds`;
CREATE TABLE `kinds` (
  `id` int(5) NOT NULL,
  `kind` varchar(10) DEFAULT NULL,
  `kindpic` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of kinds
-- ----------------------------
INSERT INTO `kinds` VALUES ('1', '小说', '../static/images/kinds/novel.jpg');
INSERT INTO `kinds` VALUES ('2', '人文', '../static/images/kinds/human.jpg');
INSERT INTO `kinds` VALUES ('3', '科学', '../static/images/kinds/science.jpg');
INSERT INTO `kinds` VALUES ('4', '历史', '../static/images/kinds/history.jpg');
INSERT INTO `kinds` VALUES ('5', '教育', '../static/images/kinds/education.jpg');
INSERT INTO `kinds` VALUES ('6', '经济', '../static/images/kinds/economic.jpg');
INSERT INTO `kinds` VALUES ('7', '生活', '../static/images/kinds/life.jpg');
INSERT INTO `kinds` VALUES ('8', '传记', '../static/images/kinds/biography.jpg');
INSERT INTO `kinds` VALUES ('9', '漫画书', '../static/images/kinds/comic.jpg');
INSERT INTO `kinds` VALUES ('10', '电子书', '../static/images/kinds/ebook.jpg');

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` varchar(10) DEFAULT NULL,
  `itemid` varchar(255) DEFAULT NULL,
  `itemname` varchar(30) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `receiver` varchar(255) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `num` varchar(5) DEFAULT NULL,
  `regtime` varchar(20) DEFAULT NULL,
  `price` varchar(5) DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  `conditions` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('1', '21', '《三国演义》', '1', '李鹏飞', '17862702222', '山东省威海市环翠区哈尔滨工业大学', '1', '2017-06-03 09:24:54', '30.0', '30.0', '2');
INSERT INTO `orders` VALUES ('2', '40', '《诛仙》', '1', 'None', 'None', 'None', '2', '2017-06-03 09:24:54', '20.0', '40.0', '0');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(5) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `phonenum` varchar(30) DEFAULT NULL,
  `receiver` varchar(255) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `regtime` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'z', 'z', 'z', 'None', null, 'None', '2017-06-01');
INSERT INTO `users` VALUES ('2', '1', '1', '1', '17862702222', '李鹏飞', '山东省威海市环翠区哈尔滨工业大学', '2017-06-01');
INSERT INTO `users` VALUES ('3', '2', '2', '2', '12312', '啊', '放假哦史蒂夫', '2017-06-02');
INSERT INTO `users` VALUES ('4', '赵博宇', '123', 'good@163.com', 'None', 'None', 'None', '2017-06-02');
