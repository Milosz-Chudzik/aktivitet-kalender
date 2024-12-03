-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Stats
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Stats
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Stats` DEFAULT CHARACTER SET utf8 ;
USE `Stats` ;

-- -----------------------------------------------------
-- Table `Stats`.`bruker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Stats`.`bruker` (
  `bruker_id` INT NOT NULL AUTO_INCREMENT,
  `fornavn` VARCHAR(45) NOT NULL,
  `etternavn` VARCHAR(45) NOT NULL,
  `tlf` VARCHAR(45) NOT NULL,
  `epost` VARCHAR(45) NULL,
  `passord` VARCHAR(45) NOT NULL,
  `brukernavn` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`bruker_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Stats`.`muskel_gruppe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Stats`.`muskel_gruppe` (
  `muskel_gruppe_id` INT NOT NULL AUTO_INCREMENT,
  `muskel_gruppe` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`muskel_gruppe_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Stats`.`ovelser`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Stats`.`ovelser` (
  `ovelse_id` INT NOT NULL AUTO_INCREMENT,
  `ovelse` VARCHAR(45) NOT NULL,
  `muskelgruppe` INT NOT NULL,
  PRIMARY KEY (`ovelse_id`),
  INDEX `fk_ovelser_muskel_gruppe_idx` (`muskelgruppe` ASC),
  CONSTRAINT `fk_ovelser_muskel_gruppe`
    FOREIGN KEY (`muskelgruppe`)
    REFERENCES `Stats`.`muskel_gruppe` (`muskel_gruppe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Stats`.`bruker_ovelser`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Stats`.`bruker_ovelser` (
  `bruker_id` INT NOT NULL,
  `ovelse_id` INT NOT NULL,
  `reps` INT NULL,
  `sets` INT NULL,
  `vekt` INT NULL,
  PRIMARY KEY (`bruker_id`, `ovelse_id`),
  INDEX `fk_bruker_has_ovelser_ovelser1_idx` (`ovelse_id` ASC),
  INDEX `fk_bruker_has_ovelser_bruker1_idx` (`bruker_id` ASC),
  CONSTRAINT `fk_bruker_has_ovelser_bruker1`
    FOREIGN KEY (`bruker_id`)
    REFERENCES `Stats`.`bruker` (`bruker_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_bruker_has_ovelser_ovelser1`
    FOREIGN KEY (`ovelse_id`)
    REFERENCES `Stats`.`ovelser` (`ovelse_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
