CREATE TABLE
IF NOT EXISTS `dfcf_notices` (
	`code` VARCHAR(10) NOT NULL,
	`name` VARCHAR(40) NOT NULL,
	`title` VARCHAR(80),
	`type` varchar(50),
	`publictime` timestamp,
  `spidertime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`url` varchar(300),
	`content` text,
	PRIMARY KEY(`code`, `name`, `title`, `type`, `publictime`)
)DEFAULT CHARSET=utf8;


-- 添加测试数据
INSERT INTO dfcf_notices (
	`code`,
	`name`,
	`title`,
	`type`,
	`publictime`,
	`url`,
	`content`
)
VALUES
	(
		'600393',
		'粤泰股份',
		'600393:粤泰股份重大资产重组停牌进展公告',
		'停牌公告',
		'2018-05-04',
		'http://data.eastmoney.com/notices/detail/600393/AN201805031136090961,JWU3JWIyJWE0JWU2JWIzJWIwJWU4JTgyJWExJWU0JWJiJWJk.html',
		'证券代码：600393 '
	)