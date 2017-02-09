CREATE TABLE `season_record` (
	`No` INT(11) NOT NULL AUTO_INCREMENT,
	`경기` INT(11) NULL DEFAULT NULL,
	`타석` INT(11) NULL DEFAULT NULL,
	`타수` INT(11) NULL DEFAULT NULL,
	`안타` INT(11) NULL DEFAULT NULL,
	`2루타` INT(11) NULL DEFAULT NULL,
	`3루타` INT(11) NULL DEFAULT NULL,
	`홈런` INT(11) NULL DEFAULT NULL,
	`타점` INT(11) NULL DEFAULT NULL,
	`득점` INT(11) NULL DEFAULT NULL,
	`도루` INT(11) NULL DEFAULT NULL,
	`사사구` INT(11) NULL DEFAULT NULL,
	`삼진` INT(11) NULL DEFAULT NULL,
	`타율` DOUBLE NULL DEFAULT NULL,
	`출루율` DOUBLE NULL DEFAULT NULL,
	`장타율` DOUBLE NULL DEFAULT NULL,
	`OPS` DOUBLE NULL DEFAULT NULL,
	PRIMARY KEY (`No`)
)
COMMENT='나성범의 시즌 기록'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=4
;
