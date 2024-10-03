-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 23, 2024 at 08:23 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ck_edge_local`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `role` varchar(60) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `role`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$aDdgqfUSChTKbDaXPsfAwp$tqMDow/P8D7CVAyV5SZ1T5zia2M0qWGIHOx1QBbH6a4=', '2023-12-15 09:52:08.569581', 1, 'admin', 'Admin', '', '', '', 1, 1, '2023-02-25 05:24:25.759741'),
(2, 'pbkdf2_sha256$390000$aDdgqfUSChTKbDaXPsfAwp$tqMDow/P8D7CVAyV5SZ1T5zia2M0qWGIHOx1QBbH6a4=', '2023-12-15 05:55:34.531166', 0, 'Auditor', 'Internal Audit', 'Internal Auditor', '', '', 1, 1, '2023-12-14 05:24:25.759741');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('abfyp65fnb484aphzp9zbdgfofwbii27', 'e30:1rDfdI:8PeOdrJikNr8AjQb8xUmgSfK-yBPFh8oIydD9t_I8wc', '2023-12-28 06:55:44.229230'),
('iwdys0ycoinorn3d3xvpz9psuaq4wufd', '.eJxVjMsOgjAUBf-la9MItfTiTvd-A7mvCgptwmNl_HchYSHbmTnnY8bcq7mamwxdMiezTDomHP5Rg8vcNptoOll5cWSE_Na0CXlhembLOc1jR3ZL7G4n-8ii_X1vDwctTu26ZlZF1BpLlqJ0JUcXvcQavIeaKEDwQJUCxFAxIlyoEIwEVcSzcxLM9wcTUEP6:1rE4rY:IuXjQRiAGsyg0WanaJCuOQWSU07JMFDgdm1gcf4DxHw', '2023-12-29 09:52:08.583466'),
('jj0dt21fi37b97wea1thu9i1ed35p16t', '.eJxVjMEOwiAQRH_FcDZEQcrWm948-A3Nwi62WiGh9GT8d4vppcd5b2Y-IqeRxVncYuEccdxdZhqK2It5qvld3R-lvMAO59J3VXUDLUZtmUP_4lgFPTE-kvQpljw4WStytZO8J-LxunY3Bz1O_bL2nhmRW1SejkorH3QwFFowBlrnLFgDrmGAYBuPCCd3JAwOmoAHrcmK7w-bokhV:1rDin2:c_E_6mvn9De74UY5rJgEbTsAxtk_l3C1EJUYFVPYDcc', '2023-12-28 10:18:00.242762'),
('ztiq4bu9rv8tl9pdj9ejv8lu36jav7c9', '.eJxVjMsOgjAUBf-la9NIa-nFpXu_oblPQQ0kFFbGf1cSFro9M3NeruC69GWtOpdB3NkFd_jdCPmh4wbkjuNt8jyNyzyQ3xS_0-qvk-jzsrt_Bz3W_lszqyJqh4GlCTGwRUtiHaQEHVGGnIBaBbDcMiKcqBE0gtbwGKNk9_4AIi05Ow:1rE1Ac:9m6iAkFcMRMYx01v2dS9EiDbHXZUbhFsrytjEAZo2a4', '2023-12-29 05:55:34.555089');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_adcourse`
--

CREATE TABLE `myapp_adcourse` (
  `id` bigint(20) NOT NULL,
  `cname` varchar(60) NOT NULL,
  `cdetails` varchar(60) DEFAULT NULL,
  `cduration` varchar(60) NOT NULL,
  `cprice` varchar(100) NOT NULL,
  `cgst` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_adcourse`
--

INSERT INTO `myapp_adcourse` (`id`, `cname`, `cdetails`, `cduration`, `cprice`, `cgst`) VALUES
(1, 'PHP FULL STACK', 'PHP FULL STACK', '3', '15000', 18),
(3, 'Website Creator', 'Website creator', '3', '15000', 18),
(4, 'TNPSC', 'Competitive exam coaching', '1', '3500', 18),
(5, 'Python', 'In-depth exploration of Python programming with practical tr', '2', '9320', 18),
(6, 'React JS', 'Helpful in  building a Modern Web Application', '2', '9320', 18),
(7, 'UI/UX', 'Web designing', '1', '4660', 18);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_ck_table`
--

CREATE TABLE `myapp_ck_table` (
  `id` bigint(20) NOT NULL,
  `Location` varchar(100) NOT NULL,
  `education` varchar(60) NOT NULL,
  `comp_year` int(11) DEFAULT NULL,
  `parent_name` varchar(60) NOT NULL,
  `ph_num` varchar(20) NOT NULL,
  `al_ph_num` varchar(20) NOT NULL,
  `parent_ph_num` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `source` varchar(20) DEFAULT NULL,
  `payment_type` varchar(50) NOT NULL,
  `payment_mode` varchar(50) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `remark` varchar(50) NOT NULL,
  `receipt_id` varchar(20) NOT NULL,
  `candid_name` varchar(60) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `blc_amnt` varchar(100) DEFAULT NULL,
  `dat` date DEFAULT NULL,
  `nxt_month` date DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `acourse_id` bigint(20) NOT NULL,
  `inactive_dat` date DEFAULT NULL,
  `dis_price` varchar(100) DEFAULT NULL,
  `discount` varchar(100) DEFAULT NULL,
  `final_amount` varchar(100) DEFAULT NULL,
  `gst_amount` varchar(100) DEFAULT NULL,
  `gst_p` varchar(100) DEFAULT NULL,
  `cgst` varchar(100) DEFAULT NULL,
  `candid_no` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_ck_table`
--

INSERT INTO `myapp_ck_table` (`id`, `Location`, `education`, `comp_year`, `parent_name`, `ph_num`, `al_ph_num`, `parent_ph_num`, `email`, `address`, `source`, `payment_type`, `payment_mode`, `amount`, `remark`, `receipt_id`, `candid_name`, `price`, `blc_amnt`, `dat`, `nxt_month`, `status`, `acourse_id`, `inactive_dat`, `dis_price`, `discount`, `final_amount`, `gst_amount`, `gst_p`, `cgst`, `candid_no`) VALUES
(1, 'Cuddalore', 'MCA', 2018, 'Pandiyan ', '6383850074', '', '', 'rrammu2016@gmail.com', '3 natesan nagar semmandalam cuddaloe', 'Advertisement', 'Monthly Payment', 'UPI', '5000.00', '', '1605230001', 'Hemalatha pandiyan', '15000', '5900.00', '2023-04-10', '2023-06-16', 'Active', 3, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CK002'),
(2, 'Cuddalore', 'MCA', 2005, '-', '9840433537', '', '', 'pradeesh.n@hepl.com', 'h', 'Inner\r\nReferences', 'Monthly Payment', 'Cash', '5000.00', 'Test ', '1004230002', 'Pradeesh N', '15000', '11800.00', '2023-04-10', '2023-05-10', 'Active', 3, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', '171184'),
(3, 'Cuddalore', 'Bsc.Cs', 2021, 'BASKARAN ', '8124864878', '', '7448844778', 'athithyabaskaran2001@gmail.com', 'No.6 Subrayalunnagar  Varakalpattu , cuddalore ', 'Advertisement', 'Full Payment', 'UPI', '10500.00', '', '1804230001', 'ATHITHYA', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC01'),
(4, 'Cuddalore', 'B.Tech CS', 2022, 'SEEVANANDHAM', '8973427499', '', '9524864307', 'ajaykiran2352001@gmail.com', '26, MAINROAD KANNITAMILNADU KURINJIPADI TK, CUDDALORE ', 'Nakuri', 'Full Payment', 'UPI', '10500.00', '', '1804230002', 'AJAYKIRAN', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC02'),
(5, 'Cuddalore', 'B.E Mech. ', 2019, 'SUBRAMANIYAN', '7339055623', '', '', 'bharathimechbharathi@gmail.com', '17/56 PARVATHIPURAM INDIRA NAGAR VADALUR ', 'Inner References', 'Full Payment', 'UPI', '10500.00', '', '1804230003', 'BHARATHI ', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC03'),
(6, 'Cuddalore', 'BCA', 2022, 'ELUMALAI ', '6381562092', '', '9688027749', 'hema18eg@gmail.com', '4/A SUNDARMUDALI ST. GIDANGAL 1 THINDIVANAM. ', 'Advertisement', 'Full Payment', 'UPI', '10500.00', '', '1804230004', 'HEMALATHA. E', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC04'),
(7, 'Cuddalore', 'B.Tech. IT ', 2022, 'RAMESH', '8220710152', '', '8122770152', 'jananiramesh01@gmail.com', '66, SIVARAMAN NAGAR BHARATHIYAR ST. KONDUR 607006', 'Advertisement', 'Full Payment', 'UPI', '10500.00', '', '1804230005', 'JANANEE. R', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC05'),
(8, 'Cuddalore', 'Bsc.Cs', 2022, 'VENKATESAN ', '9786757723', '', '9245108750', 'marievenkat008@gmail.com', '57 GNANASUNDARA LAKSHMI NAGAR K.N.PETTAI CUDDALORE ', 'Advertisement', 'Full Payment', 'UPI', '10500.00', '', '1804230006', 'MARIESWARI. V', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC07'),
(9, 'Cuddalore', 'BCA', 2022, 'MURUGAIYAN .G ', '9043572326', '', '9345899310', 'moovika2002@gmail.com', '1504,Sanjeevirayan koil st,Cuddalore-OT,607005', 'Advertisement', 'Full Payment', 'UPI', '10500.00', '', '1804230007', 'MOOVIKA.M ', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC08'),
(10, 'Cuddalore', 'MSc.cs', 2021, 'RAMACHANDRAN', '9843016482', '', '8428410522', 'nisharamachandran98@gmail.com', '36A , MARKET ST. THIRUPAPULIYUR CUDDALORE', 'Advertisement', 'Full Payment', 'UPI', '10500.00', '', '1804230008', 'NISHA ', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC09'),
(11, 'Cuddalore', 'B.Tech. IT ', 2022, 'SELVAMUTHUKUMARAESON ', '8825569339', '', '9345991267', 'kumarsathish9024@gmail.com', '21, VENUGOPALNAIDU NAGAR NATHAVELI ROAD THIRUPAPULIYUR CUDDALORE 607002', 'Advertisement', 'Full Payment', 'UPI', '10500.00', '', '1804230009', 'SATHISH. S', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC10'),
(12, 'Cuddalore', 'MBA FIN. & OP. ', 2015, 'ASHOK.S', '9944331777', '', '9367616350', 'er.srinathashok@gmail.com', '87 3rd st. RAJAM NAGAR THIRUPAPULIYUR CUDDALORE 607002', 'Inner References', 'Full Payment', 'UPI', '10500.00', '', '1804230010', 'SRINATH .A ', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC11'),
(13, 'Cuddalore', 'BCA', 2022, 'SANKAR', '8838826374', '', '', 'vigneshwari2002@gmail.com', '33, PERUMAL NAGAR THIRUPAPULIYUR CUDDALORE 607002', 'FRIEND ', 'Full Payment', 'UPI', '10500.00', '', '1804230011', 'VIGNESWARI. S', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC14'),
(14, 'Cuddalore', 'BCA', 2021, 'JOTHI MURUGAN ', '8270222953', '', '', 'vijayaganapathy2356@outlook.com', '528 PUTHUKUPPAM KURINJIPADI CUDDALORE 607 302', 'Inner References', 'Full Payment', 'UPI', '10500.00', '', '1804230012', 'VIJAYAGANAPATHY. J', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC15'),
(15, 'Cuddalore', 'MSC-IT', 2022, 'MURUGAN', '8248834289', '', '9677634402', 'vk824882022@gmail.com', '56, PERIYASAMY NAGAR GUNDUUPPALAVADI CUDDALORE 607 006', 'FRIEND ', 'Full Payment', 'UPI', '10500.00', '', '1804230013', 'VIJAYA KUMAR. M ', '15000', '0.00', '2023-04-18', '2023-05-18', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC16'),
(16, 'Cuddalore', 'B.Tech ECE ', 2018, 'SUBRAMANIAN ', '9629590739', '', '8760588447', 'suganthini95@gmail.com', '559, RICE MILL STREET PN PALAYAM MELPATTAMPAKKAM POST CUDDALORE 607 104', 'TELE CALLER ', 'Full Payment', 'UPI', '10500.00', '', '2004230001', 'SUGANTHINI. S', '15000', '0.00', '2023-04-20', '2023-05-20', 'Active', 1, NULL, '10500.00', '30', '12390.00', '1890.00', '1890.00', '18', 'CKEDGEC12'),
(17, 'Cuddalore', 'BCA', 2022, 'MUTHAYAN ', '9489663384', '', '9865032269', 'nazinive318@gmail.com', '32 C New uppalavadi street, manjakuppam cuddalore 607001', 'TELE CALLER ', 'Monthly Payment', 'UPI', '5000.00', '', '1407230001', 'NIVETHAA. M ', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 3, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGEC16'),
(18, 'Cuddalore', 'Bsc.Cs', 2022, 'PERUMAL ', '7708250694', '', '9944130694', 'perumalkamalaveni@gmail.com', '218, Ayal street suthukulam cuddalore O.T  607002', 'Trainee reference ', 'Monthly Payment', 'UPI', '5000.00', '', '1407230002', 'KAMALAVENI', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 1, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGEC21'),
(19, 'Cuddalore', 'B.E CSE', 2022, 'JAYABAL', '8098185278', '', '9942521930', 'jayabalarulsjiva@gmail.com', '3 , East street Subbauppalavadi post uchimedu, cuddalore 607402', 'FRIEND ', 'Monthly Payment', 'UPI', '5000.00', '', '1407230003', 'ARUL SIVA . J ', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 1, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGEC20'),
(20, 'Cuddalore', 'B.Tech. IT ', 2022, 'PARTHIBAN', '9600491195', '', '9345181039', 'gokulanathjp@gmail.com', '28, A/3 MAin road vannarapalayam, cuddalore, 607001', 'FRIEND ', 'Monthly Payment', 'UPI', '5000.00', '', '1407230004', 'GOKULANATH. J.P ', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 3, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGEC18'),
(21, 'Cuddalore', 'B.Tech. IT ', 2023, 'SUBRAMANIAN', '9790370486', '', '8124675710', 'thirunaarayanks@gmail.com', '4 , Ram nagar Kondur cuddalore 607001', 'FRIEND ', 'Monthly Payment', 'UPI', '3500.00', '', '1407230005', 'THIRUNAARAYAN K. S', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 1, NULL, '10500.00', '30', '4130.00', '1890.00', '630.00', '18', 'CKEDGEC15'),
(22, 'Cuddalore', 'B.Tech Mech', 2022, 'BUWANESHWARI', '6379587701', '', '8667608530', 'jagadeesaran@gmail.com', '66, Sivaraman Nagar Kondur Cuddalore 607006', 'Trainee reference ', 'Monthly Payment', 'UPI', '5000.00', '', '1407230006', 'JAGADEESWARAN .R ', '15000', '5900.00', '2023-05-08', '2023-08-14', 'Inactive', 3, '2023-08-02', NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGEC19'),
(23, 'Cuddalore', 'B.E ECE', 2018, 'SUBRAMANIAN', '7550354990', '', '9489232379', 'subasubramanian214@gmail.com', '16, JAYARAM NAGAR MANJAKUPPAM CUDDALORE 607001', 'Trainee reference ', 'Monthly Payment', 'UPI', '3500.00', '', '1407230007', 'SUBASHINI . S', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 1, NULL, '10500.00', '30', '4130.00', '1890.00', '630.00', '18', 'CKEDGEC13'),
(24, 'Cuddalore', 'B.E CSE', 2022, 'SIVAKUMAR P', '9698762819', '', '9698762816', '0401lawanya@gmail.com', '22 B/1 PONNAN STREET PUDUPALAYAM CUDDALORE 607 001', 'Nakuri', 'Monthly Payment', 'UPI', '3500.00', '', '1407230008', 'LAWANYA. S', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 1, NULL, '10500.00', '30', '4130.00', '1890.00', '630.00', '18', 'CKEDGEC14'),
(25, 'Cuddalore', 'B.E CSE', 2022, 'MOHAMMED ALI', '9345845294', '', '9443986713', 'ameer59512@gmail.com', '1 East street pachaiyankuppam cuddalore O.T, cuddalore 607003', 'Nakuri', 'Monthly Payment', 'UPI', '5000.00', '', '1407230009', 'AMMEERUNNISHA.  A', '15000', '0', '2023-05-08', '2023-08-14', 'Active', 3, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGEC22'),
(26, 'Cuddalore', 'BCA', 2023, 'G RAMESH', '6385610093', '9080327962', '9080327962', 'srinivasan274322@gmail.com', '60 A, NELLIKUPAM MAIN ROAD, SN SAVADI, CUDDALORE', 'Advertisement', 'Monthly Payment', 'UPI', '5000.00', 'GOOD', '0811230001', 'SRINIVASAN R', '15000', '0', '2023-08-03', '2023-12-08', 'Active', 1, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGE23'),
(27, 'Cuddalore', 'B.Sc  IT', 2023, 'P ANAND', '6382104090', '6383435203', '9842617501', 'sujithaanandh08@gmail.com', '46/7 NELLIKUPPAM MAIN ROAD, SEMANDALAM, CUDDALORE', 'Inner References', 'Monthly Payment', 'UPI', '5000.00', '', '1811230001', 'A SUJITHA', '15000', '0', '2023-08-03', '2023-12-18', 'Active', 1, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGE24'),
(28, 'Cuddalore', 'B.E CSE', 2014, 'B DHANDAPANI', '7598491905', '', '9442444741', 'dhsuba@gmail.com', '2/29 Bazzar street, Virudhachalam', 'TELE CALLER ', 'Monthly Payment', 'UPI', '5000.00', '', '0910230001', 'D BALAMURUGAN', '15000', '5900.00', '2023-08-14', '2023-11-09', 'Active', 1, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGE25'),
(29, 'Cuddalore', 'Bsc.Cs', 2023, 'R ARUMUGAM', '8825970457', '', '9952582453', 'swathiarumugam01@gmail.com', '34 NEW STREET, kEEZH BHUVANAGIRI', 'TELE CALLER ', 'Monthly Payment', 'UPI', '5000.00', '', '1811230002', 'A SWATHI', '15000', '0', '2023-08-14', '2023-12-18', 'Active', 1, NULL, NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGE26'),
(30, 'Cuddalore', 'MSc.cs', 2021, 'MANI V', '9600697405', '9865470742', '9865470742', 'parsriparthiban@gmail.com', 'C3, Dhatchanamoorthy Street, Manjakuppam, Cuddalore', 'Trainee reference ', 'Monthly Payment', 'UPI', '5000.00', '', '0109230001', 'PARTHIBAN M', '15000', '11800.00', '2023-09-01', '2023-10-01', 'Inactive', 1, '2023-11-22', NULL, NULL, '5900.00', '2700.00', '900.00', '18', 'CKEDGE27'),
(31, 'Cuddalore', 'MBA', 2023, 'B CHARLES', '8778625875', '', '9943427634', 'c.alexjeba@gmail.com', 'No. 4, 4th Street, Jeeva Nagar, Nellikuppam 607105', 'Advertisement', 'Monthly Payment', 'UPI', '4660.00', '', '2911230001', 'C ALEX JEBASTIN', '9320', '5498.80', '2023-11-29', '2023-12-29', 'Active', 6, NULL, NULL, NULL, '5498.80', '1677.60', '838.80', '18', 'CKEDGE28'),
(32, 'Cuddalore', 'Diploma in Mechanical Engineering', 2017, 'Balamurugan', '8667489458', '', '8610949391', 'ashwinsri1997@gmail.com', '194/B Diversion Road Panruti', 'Advertisement', 'Monthly Payment', 'UPI', '4660.00', '', '1312230001', 'Ashwin Kumar B', '9320', '5498.80', '2023-12-13', '2024-01-13', 'Active', 6, NULL, NULL, NULL, '5498.80', '1677.60', '838.80', '18', 'CKEDGE29');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_locations_add`
--

CREATE TABLE `myapp_locations_add` (
  `id` bigint(20) NOT NULL,
  `loc_name` varchar(60) NOT NULL,
  `status` varchar(60) DEFAULT NULL,
  `created_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_locations_add`
--

INSERT INTO `myapp_locations_add` (`id`, `loc_name`, `status`, `created_at`) VALUES
(1, 'Cuddalore', 'Active', '2023-03-22'),
(2, 'Villipuram', 'Active', '2023-03-22');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_paydetails`
--

CREATE TABLE `myapp_paydetails` (
  `id` bigint(20) NOT NULL,
  `candid_name` varchar(60) NOT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `dat` date DEFAULT NULL,
  `ckid` int(11) DEFAULT NULL,
  `discount` varchar(100) DEFAULT NULL,
  `final_amount` varchar(100) DEFAULT NULL,
  `gst_p` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_paydetails`
--

INSERT INTO `myapp_paydetails` (`id`, `candid_name`, `amount`, `dat`, `ckid`, `discount`, `final_amount`, `gst_p`) VALUES
(1, 'Hemalatha pandiyan', '5000.00', '2023-04-10', 1, NULL, '5900.00', '900.00'),
(2, 'Pradeesh N', '5000.00', '2023-04-10', 2, NULL, '5900.00', '900.00'),
(3, 'ATHITHYA', '10500.00', '2023-04-18', 3, '30', '12390.00', '1890.00'),
(4, 'AJAYKIRAN', '10500.00', '2023-04-18', 4, '30', '12390.00', '1890.00'),
(5, 'BHARATHI ', '10500.00', '2023-04-18', 5, '30', '12390.00', '1890.00'),
(6, 'HEMALATHA. E', '10500.00', '2023-04-18', 6, '30', '12390.00', '1890.00'),
(7, 'JANANEE. R', '10500.00', '2023-04-18', 7, '30', '12390.00', '1890.00'),
(8, 'MARIESWARI. V', '10500.00', '2023-04-18', 8, '30', '12390.00', '1890.00'),
(9, 'MOOVIKA.M ', '10500.00', '2023-04-18', 9, '30', '12390.00', '1890.00'),
(10, 'NISHA ', '10500.00', '2023-04-18', 10, '30', '12390.00', '1890.00'),
(11, 'SATHISH. S', '10500.00', '2023-04-18', 11, '30', '12390.00', '1890.00'),
(12, 'SRINATH .A ', '10500.00', '2023-04-18', 12, '30', '12390.00', '1890.00'),
(13, 'VIGNESWARI. S', '10500.00', '2023-04-18', 13, '30', '12390.00', '1890.00'),
(14, 'VIJAYAGANAPATHY. J', '10500.00', '2023-04-18', 14, '30', '12390.00', '1890.00'),
(15, 'VIJAYA KUMAR. M ', '10500.00', '2023-04-18', 15, '30', '12390.00', '1890.00'),
(16, 'SUGANTHINI. S', '10500.00', '2023-04-20', 16, '30', '12390.00', '1890.00'),
(17, 'NIVETHAA. M ', '5000.00', '2023-05-08', 17, NULL, '5900.00', '900.00'),
(18, 'KAMALAVENI', '5000.00', '2023-05-08', 18, NULL, '5900.00', '900.00'),
(19, 'ARUL SIVA . J ', '5000.00', '2023-05-08', 19, NULL, '5900.00', '900.00'),
(20, 'GOKULANATH. J.P ', '5000.00', '2023-05-08', 20, NULL, '5900.00', '900.00'),
(21, 'THIRUNAARAYAN K. S', '3500.00', '2023-05-08', 21, '30', '4130.00', '630.00'),
(22, 'JAGADEESWARAN .R ', '5000.00', '2023-05-08', 22, NULL, '5900.00', '900.00'),
(23, 'SUBASHINI . S', '3500.00', '2023-05-08', 23, '30', '4130.00', '630.00'),
(24, 'LAWANYA. S', '3500.00', '2023-05-08', 24, '30', '4130.00', '630.00'),
(25, 'AMMEERUNNISHA.  A', '5000.00', '2023-05-08', 25, NULL, '5900.00', '900.00'),
(26, 'Hemalatha pandiyan', '5000.00', '2023-05-16', 1, NULL, '5900.00', '900.00'),
(27, 'NIVETHAA. M ', '5000.00', '2023-06-16', 17, NULL, '5900.00', '900.00'),
(28, 'KAMALAVENI', '5000.00', '2023-06-16', 18, NULL, '5900.00', '900.00'),
(29, 'ARUL SIVA . J ', '5000.00', '2023-06-16', 19, NULL, '5900.00', '900.00'),
(30, 'GOKULANATH. J.P ', '5000.00', '2023-06-16', 20, NULL, '5900.00', '900.00'),
(31, 'THIRUNAARAYAN K. S', '3500.00', '2023-06-16', 21, NULL, '4130.00', '630.00'),
(32, 'SUBASHINI . S', '3500.00', '2023-06-16', 23, NULL, '4130.00', '630.00'),
(33, 'LAWANYA. S', '3500.00', '2023-06-16', 24, NULL, '4130.00', '630.00'),
(34, 'AMMEERUNNISHA.  A', '5000.00', '2023-06-16', 25, NULL, '5900.00', '900.00'),
(35, 'NIVETHAA. M ', '5000.00', '2023-07-14', 17, NULL, '5900.00', '900.00'),
(36, 'KAMALAVENI', '5000.00', '2023-07-14', 18, NULL, '5900.00', '900.00'),
(37, 'ARUL SIVA . J ', '5000.00', '2023-07-14', 19, NULL, '5900.00', '900.00'),
(38, 'GOKULANATH. J.P ', '5000.00', '2023-07-14', 20, NULL, '5900.00', '900.00'),
(39, 'THIRUNAARAYAN K. S', '3500.00', '2023-07-14', 21, NULL, '4130.00', '630.00'),
(40, 'JAGADEESWARAN .R ', '5000.00', '2023-07-14', 22, NULL, '5900.00', '900.00'),
(41, 'SUBASHINI . S', '3500.00', '2023-07-14', 23, NULL, '4130.00', '630.00'),
(42, 'LAWANYA. S', '3500.00', '2023-07-14', 24, NULL, '4130.00', '630.00'),
(43, 'AMMEERUNNISHA.  A', '5000.00', '2023-07-14', 25, NULL, '5900.00', '900.00'),
(44, 'SRINIVASAN R', '5000.00', '2023-08-03', 26, NULL, '5900.00', '900.00'),
(46, 'A SUJITHA', '5000.00', '2023-08-03', 27, NULL, '5900.00', '900.00'),
(48, 'D BALAMURUGAN', '5000.00', '2023-08-14', 28, NULL, '5900.00', '900.00'),
(49, 'A SWATHI', '5000.00', '2023-08-14', 29, NULL, '5900.00', '900.00'),
(50, 'PARTHIBAN M', '5000.00', '2023-09-01', 30, NULL, '5900.00', '900.00'),
(51, 'SRINIVASAN R', '5000.00', '2023-10-06', 26, NULL, '5900.00', '900.00'),
(52, 'D BALAMURUGAN', '5000.00', '2023-10-09', 28, NULL, '5900.00', '900.00'),
(53, 'A SWATHI', '5000.00', '2023-10-13', 29, NULL, '5900.00', '900.00'),
(54, 'A SUJITHA', '5000.00', '2023-10-16', 27, NULL, '5900.00', '900.00'),
(55, 'SRINIVASAN R', '5000.00', '2023-11-08', 26, NULL, '5900.00', '900.00'),
(56, 'A SUJITHA', '5000.00', '2023-11-18', 27, NULL, '5900.00', '900.00'),
(57, 'A SWATHI', '5000.00', '2023-11-18', 29, NULL, '5900.00', '900.00'),
(58, 'C ALEX JEBASTIN', '4660.00', '2023-11-29', 31, NULL, '5498.80', '838.80'),
(59, 'Ashwin Kumar B', '4660.00', '2023-12-13', 32, NULL, '5498.80', '838.80');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_qualifications`
--

CREATE TABLE `myapp_qualifications` (
  `id` bigint(20) NOT NULL,
  `qualification` varchar(60) NOT NULL,
  `remark` varchar(60) DEFAULT NULL,
  `created_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_qualifications`
--

INSERT INTO `myapp_qualifications` (`id`, `qualification`, `remark`, `created_at`) VALUES
(1, 'Bsc.Cs', '', '2023-02-25'),
(2, 'BCA', '', '2023-02-25'),
(3, 'MCA', '', '2023-02-25'),
(4, 'MSC-IT', '', '2023-02-25'),
(5, 'Bsc.Mathematics ', '', '2023-03-07'),
(6, 'MSc.cs', '', '2023-03-07'),
(7, 'B.Tech CS', '', '2023-04-18'),
(8, 'B.E Mech. ', '', '2023-04-18'),
(9, 'B.Tech. IT ', '', '2023-04-18'),
(10, 'MBA FIN. & OP. ', '', '2023-04-18'),
(11, 'B.Tech ECE ', '', '2023-04-20'),
(12, 'B.E CSE', '', '2023-05-08'),
(13, 'B.Tech Mech', '', '2023-05-08'),
(14, 'B.E ECE', '', '2023-05-08'),
(15, 'B.Sc  IT', '', '2023-08-03'),
(16, 'MBA', '', '2023-11-24'),
(17, 'Diploma in Mechanical Engineering', '', '2023-12-13');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_rep_id`
--

CREATE TABLE `myapp_rep_id` (
  `id` bigint(20) NOT NULL,
  `receipt_id` int(11) NOT NULL,
  `dat` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_rep_id`
--

INSERT INTO `myapp_rep_id` (`id`, `receipt_id`, `dat`) VALUES
(1, 1, '2023-12-13');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_source`
--

CREATE TABLE `myapp_source` (
  `id` bigint(20) NOT NULL,
  `source_name` varchar(60) NOT NULL,
  `status` varchar(60) DEFAULT NULL,
  `created_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_source`
--

INSERT INTO `myapp_source` (`id`, `source_name`, `status`, `created_at`) VALUES
(2, 'Inner References', 'Active', '2023-03-22'),
(3, 'Nakuri', 'Active', '2023-03-22'),
(4, 'LinkedIn', 'Active', '2023-03-22'),
(5, 'Advertisement', 'Active', '2023-03-22'),
(6, 'TELE CALLER ', 'Active', '2023-04-18'),
(7, 'FRIEND ', 'Active', '2023-04-18'),
(8, 'Trainee reference ', 'Active', '2023-04-19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_adcourse`
--
ALTER TABLE `myapp_adcourse`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_ck_table`
--
ALTER TABLE `myapp_ck_table`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `myapp_ck_table_email_2d3b614e_uniq` (`email`),
  ADD UNIQUE KEY `myapp_ck_table_ph_num_933855ed_uniq` (`ph_num`),
  ADD KEY `myapp_ck_table_acourse_id_93d5817c_fk_myapp_adcourse_id` (`acourse_id`);

--
-- Indexes for table `myapp_locations_add`
--
ALTER TABLE `myapp_locations_add`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_paydetails`
--
ALTER TABLE `myapp_paydetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_qualifications`
--
ALTER TABLE `myapp_qualifications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_rep_id`
--
ALTER TABLE `myapp_rep_id`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_source`
--
ALTER TABLE `myapp_source`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `myapp_adcourse`
--
ALTER TABLE `myapp_adcourse`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `myapp_ck_table`
--
ALTER TABLE `myapp_ck_table`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `myapp_locations_add`
--
ALTER TABLE `myapp_locations_add`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `myapp_paydetails`
--
ALTER TABLE `myapp_paydetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `myapp_qualifications`
--
ALTER TABLE `myapp_qualifications`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `myapp_rep_id`
--
ALTER TABLE `myapp_rep_id`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_source`
--
ALTER TABLE `myapp_source`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `myapp_ck_table`
--
ALTER TABLE `myapp_ck_table`
  ADD CONSTRAINT `myapp_ck_table_acourse_id_93d5817c_fk_myapp_adcourse_id` FOREIGN KEY (`acourse_id`) REFERENCES `myapp_adcourse` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
