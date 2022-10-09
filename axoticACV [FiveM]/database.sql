CREATE TABLE IF NOT EXISTS `user` (
  `steamid` varchar(255) NOT NULL,
  `ip` varchar(255) NOT NULL,
  `verify` boolean,
  `lastupdated` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (steamid, ip)
);
