-- phpMyAdmin SQL Dump
-- version 4.4.15.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2016-05-18 06:49:18
-- 服务器版本： 5.5.44-MariaDB
-- PHP Version: 5.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `amazon`
--

-- --------------------------------------------------------

--
-- 表的结构 `books_type`
--

CREATE TABLE IF NOT EXISTS `books_type` (
  `type_id` int(11) NOT NULL,
  `type_name` text NOT NULL,
  `type_num` text NOT NULL,
  `type_link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `book_comment`
--

CREATE TABLE IF NOT EXISTS `book_comment` (
  `commit_id` int(11) NOT NULL,
  `book_name` text NOT NULL,
  `comment_star` text NOT NULL,
  `comment_title` text NOT NULL,
  `comment_time` text NOT NULL,
  `comment_content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `book_info`
--

CREATE TABLE IF NOT EXISTS `book_info` (
  `book_id` int(11) NOT NULL,
  `book_name` text NOT NULL,
  `book_author` text NOT NULL,
  `book_time` text NOT NULL,
  `book_price` text NOT NULL,
  `book_star` text NOT NULL,
  `book_link` text NOT NULL,
  `book_content` mediumtext NOT NULL,
  `book_comment_url` text NOT NULL,
  `book_comment_num` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books_type`
--
ALTER TABLE `books_type`
  ADD PRIMARY KEY (`type_id`);

--
-- Indexes for table `book_comment`
--
ALTER TABLE `book_comment`
  ADD PRIMARY KEY (`commit_id`);

--
-- Indexes for table `book_info`
--
ALTER TABLE `book_info`
  ADD PRIMARY KEY (`book_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books_type`
--
ALTER TABLE `books_type`
  MODIFY `type_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `book_comment`
--
ALTER TABLE `book_comment`
  MODIFY `commit_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `book_info`
--
ALTER TABLE `book_info`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
