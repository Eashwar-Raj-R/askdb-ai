-- =====================================================================
-- AskDB AI — Sample Database Schema
-- Database: uber_db
-- Description: A simplified ride-hailing schema (riders, drivers,
--              vehicles, rides, payments) used to demo the AskDB AI
--              text-to-SQL pipeline.
-- =====================================================================

CREATE DATABASE IF NOT EXISTS uber_db;
USE uber_db;

-- ---------------------------------------------------------------------
-- Table: users
-- Riders / passengers who book rides
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    user_id     INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE NOT NULL,
    phone       VARCHAR(15) UNIQUE NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------
-- Table: drivers
-- Registered drivers on the platform
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS drivers (
    driver_id     INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    email         VARCHAR(100) UNIQUE NOT NULL,
    phone         VARCHAR(15) UNIQUE NOT NULL,
    license_no    VARCHAR(50) UNIQUE NOT NULL,
    rating        DECIMAL(2,1) DEFAULT 5.0,
    is_active     BOOLEAN DEFAULT TRUE,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------
-- Table: vehicles
-- Vehicles registered to a driver (1 driver -> 1 active vehicle)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id   INT AUTO_INCREMENT PRIMARY KEY,
    driver_id    INT NOT NULL,
    make         VARCHAR(50),
    model        VARCHAR(50),
    plate_number VARCHAR(20) UNIQUE NOT NULL,
    vehicle_type ENUM('Mini','Sedan','SUV','Bike') DEFAULT 'Sedan',
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);

-- ---------------------------------------------------------------------
-- Table: rides
-- Core transactional table tracking ride lifecycle
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS rides (
    ride_id           INT AUTO_INCREMENT PRIMARY KEY,
    user_id           INT NOT NULL,
    driver_id         INT,
    vehicle_id        INT,
    pickup_location   VARCHAR(255) NOT NULL,
    dropoff_location  VARCHAR(255) NOT NULL,
    ride_status       ENUM('Requested','Accepted','Ongoing','Completed','Cancelled') DEFAULT 'Requested',
    fare              DECIMAL(10,2),
    distance_km       DECIMAL(6,2),
    requested_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at      TIMESTAMP NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- ---------------------------------------------------------------------
-- Table: payments
-- Payment record tied to a completed ride
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS payments (
    payment_id     INT AUTO_INCREMENT PRIMARY KEY,
    ride_id        INT NOT NULL,
    amount         DECIMAL(10,2) NOT NULL,
    payment_method ENUM('Card','Cash','Wallet','UPI') DEFAULT 'Card',
    payment_status ENUM('Pending','Completed','Failed','Refunded') DEFAULT 'Pending',
    paid_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ride_id) REFERENCES rides(ride_id)
);
