CREATE TABLE `total_record` (
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
	`OPS` DOUBLE NULL DEFAULT NULL
)
COMMENT='나성범의 통산 기록'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
