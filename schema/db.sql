-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.1.19-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win32
-- HeidiSQL 버전:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 테이블 test.daily_record 구조 내보내기
DROP TABLE IF EXISTS `daily_record`;
CREATE TABLE IF NOT EXISTS `daily_record` (
  `date` double DEFAULT NULL,
  `game` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 test.daily_record:~8 rows (대략적) 내보내기
/*!40000 ALTER TABLE `daily_record` DISABLE KEYS */;
INSERT INTO `daily_record` (`date`, `game`) VALUES
	(1.1, 144),
	(2.1, 144),
	(3.1, 144),
	(1.1, 144),
	(2.1, 144),
	(3.1, 144),
	(1.1, 144),
	(2.1, 144),
	(3.1, 144);
/*!40000 ALTER TABLE `daily_record` ENABLE KEYS */;

-- 테이블 test.season_record 구조 내보내기
DROP TABLE IF EXISTS `season_record`;
CREATE TABLE IF NOT EXISTS `season_record` (
  `game` int(11) DEFAULT NULL,
  `avg` double DEFAULT NULL,
  `rbi` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 test.season_record:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `season_record` DISABLE KEYS */;
INSERT INTO `season_record` (`game`, `avg`, `rbi`) VALUES
	(144, 0.999, 1222);
/*!40000 ALTER TABLE `season_record` ENABLE KEYS */;

-- 테이블 test.total_record 구조 내보내기
DROP TABLE IF EXISTS `total_record`;
CREATE TABLE IF NOT EXISTS `total_record` (
  `game` int(11) DEFAULT NULL,
  `avg` double DEFAULT NULL,
  `rbi` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- 테이블 데이터 test.total_record:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `total_record` DISABLE KEYS */;
INSERT INTO `total_record` (`game`, `avg`, `rbi`) VALUES
	(144, 0.999, 1222);
/*!40000 ALTER TABLE `total_record` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/sports*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;