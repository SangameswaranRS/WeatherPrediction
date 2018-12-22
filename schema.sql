CREATE TABLE `area` (
  `areaId` int(11) NOT NULL AUTO_INCREMENT,
  `lattitude` double NOT NULL,
  `longitude` double NOT NULL,
  PRIMARY KEY (`areaId`),
  UNIQUE KEY `area_UNIQUE` (`lattitude`,`longitude`),
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `areaToFeaturesMap` (
  `areaId` int(11) NOT NULL,
  `weatherCategory` varchar(100) NOT NULL,
  `weatherDetailedInformation` varchar(1000) NOT NULL,
  `averageTemperature` double NOT NULL,
  `averagePressure` double NOT NULL,
  `minTempSoFar` double NOT NULL,
  `maxTempSoFar` double NOT NULL,
  `updatedAtEpoch` bigint(20) NOT NULL,
  PRIMARY KEY (`areaId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `weather`.`DatasetData` (
  `entryId` INT NOT NULL AUTO_INCREMENT,
  `year` INT NOT NULL,
  `month` INT NOT NULL,
  `date` INT NOT NULL,
  `hours` INT NOT NULL,
  `minutes` INT NOT NULL,
  `seconds` INT NOT NULL,
  `Typ` VARCHAR(50) NOT NULL,
  `C` VARCHAR(50) NOT NULL,
  `stat` VARCHAR(50) NOT NULL,
  `ATim` INT NOT NULL,
  `vol` DOUBLE NOT NULL,
  `Bl` DOUBLE NOT NULL,
  `MaxV` DOUBLE NOT NULL,
  `Area` MEDIUMTEXT NULL,
  `mercuryContent` DOUBLE NULL,
  PRIMARY KEY (`entryId`));

