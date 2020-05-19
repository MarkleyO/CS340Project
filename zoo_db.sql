-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Host: classmysql.engr.oregonstate.edu:3306
-- Generation Time: May 18, 2020 at 04:37 PM
-- Server version: 10.4.11-MariaDB-log
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_markleyo`
--

-- --------------------------------------------------------

--
-- Table structure for table `Animals`
--

CREATE TABLE `Animals` (
  `Animal ID` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Species` varchar(30) NOT NULL,
  `Age` int(11) NOT NULL,
  `Habitat` varchar(30) NOT NULL,
  `Injury` varchar(50) DEFAULT NULL,
  `Feeding ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Animals`
--

INSERT INTO `Animals` (`Animal ID`, `Name`, `Species`, `Age`, `Habitat`, `Injury`, `Feeding ID`) VALUES
(1, 'Elsa', 'Polar Bear', 10, 'Tundra', 'Cut', 1),
(2, 'Julian', 'Lemur', 3, 'Jungle', 'Cut', 2),
(3, 'Shira', 'Kangaroo', 6, 'Outback', 'Sprained Ankle', 3);

-- --------------------------------------------------------

--
-- Table structure for table `AnimalsKeepers`
--

CREATE TABLE `AnimalsKeepers` (
  `Animal ID` int(11) NOT NULL,
  `Keeper ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `AnimalsKeepers`
--

INSERT INTO `AnimalsKeepers` (`Animal ID`, `Keeper ID`) VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 2);

-- --------------------------------------------------------

--
-- Table structure for table `Diets`
--

CREATE TABLE `Diets` (
  `Diet` varchar(30) NOT NULL,
  `Foods` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Diets`
--

INSERT INTO `Diets` (`Diet`, `Foods`) VALUES
('Fish', 'Tuna, Salmon, Trout'),
('Fruit', 'Tamarind, Tamarillo, Seeds'),
('Grasses', 'Wheat Grass, Flowers, Fern');

-- --------------------------------------------------------

--
-- Table structure for table `Feeding Times`
--

CREATE TABLE `Feeding Times` (
  `Feeding Time ID` int(11) NOT NULL,
  `Diet` varchar(30) NOT NULL,
  `Time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Feeding Times`
--

INSERT INTO `Feeding Times` (`Feeding Time ID`, `Diet`, `Time`) VALUES
(1, 'Fish', 5),
(2, 'Fruit', 4),
(3, 'Grasses', 13);

-- --------------------------------------------------------

--
-- Table structure for table `Keepers`
--

CREATE TABLE `Keepers` (
  `Keeper ID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Job Title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Keepers`
--

INSERT INTO `Keepers` (`Keeper ID`, `Name`, `Job Title`) VALUES
(1, 'Mina', 'Head Keeper'),
(2, 'Steve', 'Herbivore Specialist'),
(3, 'Naomi', 'Keeper');

-- --------------------------------------------------------

--
-- Table structure for table `Special Care Instructions`
--

CREATE TABLE `Special Care Instructions` (
  `Injury` varchar(50) NOT NULL,
  `Bandaging` varchar(255) DEFAULT NULL,
  `Medicine` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Special Care Instructions`
--

INSERT INTO `Special Care Instructions` (`Injury`, `Bandaging`, `Medicine`) VALUES
('Common Cold', NULL, 'Antibiotics'),
('Cut', 'Gauze', NULL),
('Sprained Ankle', 'Ankle Wrap', 'Painkillers');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Animals`
--
ALTER TABLE `Animals`
  ADD PRIMARY KEY (`Animal ID`),
  ADD UNIQUE KEY `Name` (`Name`),
  ADD KEY `Injury` (`Injury`),
  ADD KEY `Feeding ID` (`Feeding ID`);

--
-- Indexes for table `AnimalsKeepers`
--
ALTER TABLE `AnimalsKeepers`
  ADD KEY `Keeper ID` (`Keeper ID`),
  ADD KEY `Animal ID` (`Animal ID`);

--
-- Indexes for table `Diets`
--
ALTER TABLE `Diets`
  ADD PRIMARY KEY (`Diet`);

--
-- Indexes for table `Feeding Times`
--
ALTER TABLE `Feeding Times`
  ADD PRIMARY KEY (`Feeding Time ID`),
  ADD KEY `Diet` (`Diet`);

--
-- Indexes for table `Keepers`
--
ALTER TABLE `Keepers`
  ADD PRIMARY KEY (`Keeper ID`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- Indexes for table `Special Care Instructions`
--
ALTER TABLE `Special Care Instructions`
  ADD PRIMARY KEY (`Injury`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Keepers`
--
ALTER TABLE `Keepers`
  MODIFY `Keeper ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Animals`
--
ALTER TABLE `Animals`
  ADD CONSTRAINT `Animals_ibfk_1` FOREIGN KEY (`Injury`) REFERENCES `Special Care Instructions` (`Injury`),
  ADD CONSTRAINT `Animals_ibfk_2` FOREIGN KEY (`Feeding ID`) REFERENCES `Feeding Times` (`Feeding Time ID`);

--
-- Constraints for table `AnimalsKeepers`
--
ALTER TABLE `AnimalsKeepers`
  ADD CONSTRAINT `AnimalsKeepers_ibfk_1` FOREIGN KEY (`Keeper ID`) REFERENCES `Keepers` (`Keeper ID`),
  ADD CONSTRAINT `AnimalsKeepers_ibfk_2` FOREIGN KEY (`Animal ID`) REFERENCES `Animals` (`Animal ID`);

--
-- Constraints for table `Feeding Times`
--
ALTER TABLE `Feeding Times`
  ADD CONSTRAINT `Feeding Times_ibfk_1` FOREIGN KEY (`Diet`) REFERENCES `Diets` (`Diet`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
