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
