-- =====================================================================
-- AskDB AI — Sample Data
-- Run schema.sql first, then this file, to populate uber_db with
-- synthetic demo data for testing the text-to-SQL pipeline.
-- =====================================================================

USE uber_db;

-- ---------------------------------------------------------------------
-- Users
-- ---------------------------------------------------------------------
INSERT INTO users (name, email, phone) VALUES
('Ravi Kumar', 'ravi.kumar@example.com', '9876543210'),
('Priya Singh', 'priya.singh@example.com', '9876543211'),
('Sneha Patel', 'sneha.patel@example.com', '9876543212'),
('Vikram Rao', 'vikram.rao@example.com', '9876543213'),
('Ananya Iyer', 'ananya.iyer@example.com', '9876543214'),
('Rahul Nair', 'rahul.nair@example.com', '9876543215'),
('Divya Menon', 'divya.menon@example.com', '9876543216'),
('Sameer Khan', 'sameer.khan@example.com', '9876543217'),
('Neha Joshi', 'neha.joshi@example.com', '9876543218'),
('Aditya Reddy', 'aditya.reddy@example.com', '9876543219');

-- ---------------------------------------------------------------------
-- Drivers
-- ---------------------------------------------------------------------
INSERT INTO drivers (name, email, phone, license_no, rating, is_active) VALUES
('Arjun Mehta', 'arjun.mehta@example.com', '9123456780', 'DL-001-2024', 4.9, TRUE),
('Karan Verma', 'karan.verma@example.com', '9123456781', 'DL-002-2024', 4.6, TRUE),
('Suresh Pillai', 'suresh.pillai@example.com', '9123456782', 'DL-003-2024', 4.7, TRUE),
('Manoj Tiwari', 'manoj.tiwari@example.com', '9123456783', 'DL-004-2024', 4.9, TRUE),
('Ramesh Yadav', 'ramesh.yadav@example.com', '9123456784', 'DL-005-2024', 4.5, FALSE),
('Deepak Chauhan', 'deepak.chauhan@example.com', '9123456785', 'DL-006-2024', 4.6, TRUE),
('Ajay Malhotra', 'ajay.malhotra@example.com', '9123456786', 'DL-007-2024', 4.8, FALSE);

-- ---------------------------------------------------------------------
-- Vehicles
-- ---------------------------------------------------------------------
INSERT INTO vehicles (driver_id, make, model, plate_number, vehicle_type) VALUES
(1, 'Toyota', 'Innova', 'MH12AB1234', 'SUV'),
(2, 'Honda', 'City', 'MH12CD5678', 'Sedan'),
(3, 'Maruti', 'Swift', 'MH14EF9012', 'Mini'),
(4, 'Hyundai', 'Verna', 'MH14GH3456', 'Sedan'),
(5, 'Mahindra', 'XUV700', 'MH14IJ7890', 'SUV'),
(6, 'Bajaj', 'Pulsar', 'MH14KL1122', 'Bike'),
(7, 'Tata', 'Nexon', 'MH14MN3344', 'SUV');

-- ---------------------------------------------------------------------
-- Rides
-- ---------------------------------------------------------------------
INSERT INTO rides (user_id, driver_id, vehicle_id, pickup_location, dropoff_location, ride_status, fare, distance_km, requested_at, completed_at) VALUES
(1, 1, 1, 'Andheri', 'Bandra', 'Completed', 250.00, 8.5, '2026-07-18 09:10:00', '2026-07-18 09:40:00'),
(2, 2, 2, 'Powai', 'Worli', 'Completed', 300.00, 12.0, '2026-07-19 18:05:00', '2026-07-19 18:45:00'),
(3, 3, 3, 'Kurla', 'Dadar', 'Completed', 150.00, 6.2, '2026-07-20 08:15:00', '2026-07-20 08:45:00'),
(4, 4, 4, 'Chembur', 'Vashi', 'Completed', 320.00, 15.4, '2026-07-20 09:30:00', '2026-07-20 10:10:00'),
(5, 3, 3, 'Thane', 'Ghatkopar', 'Ongoing', NULL, 9.8, '2026-07-21 07:45:00', NULL),
(6, 6, 6, 'Malad', 'Goregaon', 'Requested', NULL, 4.1, '2026-07-21 08:00:00', NULL),
(7, 2, 2, 'Borivali', 'Andheri', 'Completed', 220.00, 11.3, '2026-07-21 10:00:00', '2026-07-21 10:35:00'),
(8, 1, 1, 'Bandra', 'Juhu', 'Cancelled', NULL, 3.5, '2026-07-21 11:00:00', NULL),
(9, 2, 2, 'Colaba', 'Marine Lines', 'Completed', 90.00, 2.8, '2026-07-21 12:30:00', '2026-07-21 12:50:00'),
(10, 3, 3, 'Worli', 'Lower Parel', 'Ongoing', NULL, 3.2, '2026-07-22 07:00:00', NULL);

-- ---------------------------------------------------------------------
-- Payments
-- ---------------------------------------------------------------------
INSERT INTO payments (ride_id, amount, payment_method, payment_status, paid_at) VALUES
(1, 250.00, 'UPI', 'Completed', '2026-07-18 09:41:00'),
(2, 300.00, 'Card', 'Completed', '2026-07-19 18:46:00'),
(3, 150.00, 'Cash', 'Completed', '2026-07-20 08:45:30'),
(4, 320.00, 'Wallet', 'Completed', '2026-07-20 10:11:00'),
(7, 220.00, 'UPI', 'Completed', '2026-07-21 10:36:00'),
(9, 90.00, 'Card', 'Completed', '2026-07-21 12:51:00');
