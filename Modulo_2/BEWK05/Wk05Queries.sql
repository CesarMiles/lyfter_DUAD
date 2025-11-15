-- Part 1 Creation of DB and Data Population 

-- 2. Customer table creation
create table lyfter_car_rental.customer_car_rental_data (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        password VARCHAR(50),
        email VARCHAR(50),
        full_name VARCHAR(50),
        date_of_birth DATE,
        account_status VARCHAR(9));
    
-- INSERT_MULTIPLE_CUSTOMERS: Inserta 50 clientes de prueba en una sola operación
INSERT INTO lyfter_car_rental.customer_car_rental_data 
(username, password, email, full_name, date_of_birth, account_status) 
VALUES 
('bcorey0', 'mI8+%P)8#lb$b/r9', 'bcorey0@gov.uk', 'Bonny Corey', '1955-10-20', 'inactive'),
('yblas1', 'zY0>Hg"!UAI?EX\\Y', 'yblas1@prlog.org', 'Yasmeen Blas', '1981-06-23', 'inactive'),
('kcouroy2', 'jX4%/@~,OO1', 'kcouroy2@reverbnation.com', 'Karim Couroy', '1953-06-22', 'active'),
('kryhorovich3', 'eP5#YQ,HMnKJL', 'kryhorovich3@washingtonpost.com', 'Kasey Ryhorovich', '1971-08-01', 'active'),
('lpaddle4', 'zR3.$.NJR#5DOu60', 'lpaddle4@skype.com', 'Lorianna Paddle', '1967-12-16', 'suspended'),
('tmellish5', 'jP4_T=6aFk*V,2E', 'tmellish5@github.io', 'Tabor Mellish', '1978-08-10', 'suspended'),
('fdeehan6', 'fU9.zb5t/we`Tw"', 'fdeehan6@bravesites.com', 'Fionnula Deehan', '1981-08-22', 'suspended'),
('jbyford7', 'dG8)"e2P', 'jbyford7@umich.edu', 'Jessee Byford', '1972-06-27', 'suspended'),
('mbails8', 'jJ4`z$Od5E', 'mbails8@blinklist.com', 'Malchy Bails', '1956-03-15', 'inactive'),
('cfallanche9', 'tJ5!l126#W9v&g', 'cfallanche9@geocities.com', 'Camey Fallanche', '1969-09-17', 'inactive'),
('wbenleya', 'sG8}hDSA*wR#v', 'wbenleya@unblog.fr', 'Weidar Benley', '2002-04-30', 'suspended'),
('bfaraganb', 'pP6{wz&%3HnL}cU', 'bfaraganb@squidoo.com', 'Boyd Faragan', '1997-12-13', 'suspended'),
('cbarrassc', 'jF4)=rR4$I', 'cbarrassc@weebly.com', 'Constancy Barrass', '1981-01-13', 'inactive'),
('kmauserd', 'iO2"4I#G)=bA/', 'kmauserd@dailymotion.com', 'Kath Mauser', '1951-11-12', 'suspended'),
('rdelvese', 'mB4''Z%@|\\c"D', 'rdelvese@tinyurl.com', 'Robbi Delves', '2002-12-01', 'inactive'),
('dhaythornf', 'dV6/kY"jiT/xOek', 'dhaythornf@ow.ly', 'Daryl Haythorn', '1952-09-15', 'active'),
('asainerg', 'kH2=qTy@Hl', 'asainerg@arizona.edu', 'Alex Sainer', '1963-02-07', 'inactive'),
('oleitchh', 'jY1>/E(Rv%xx', 'oleitchh@ycombinator.com', 'Orland Leitch', '1997-10-04', 'active'),
('nquarriei', 'bA8?$Yhm||4PN', 'nquarriei@youku.com', 'Nobie Quarrie', '1971-04-23', 'active'),
('ohowcroftj', 'kG3@6JkF)FAM=%~''', 'ohowcroftj@chronoengine.com', 'Odetta Howcroft', '1973-08-30', 'inactive'),
('acuttelark', 'jW9_*zxn%nL', 'acuttelark@seattletimes.com', 'Ada Cuttelar', '1974-04-16', 'active'),
('npitsalll', 'wV7/9iJpXYm)j', 'npitsalll@privacy.gov.au', 'Nathalie Pitsall', '1965-07-18', 'suspended'),
('aboatem', 'oN6<>$qqH(', 'aboatem@tripod.com', 'Antonetta Boate', '1985-01-06', 'active'),
('hbartolijnn', 'dC6\\bbR9', 'hbartolijnn@51.la', 'Herschel Bartolijn', '1985-03-10', 'active'),
('mtourleo', 'zZ2|M1q4m>W', 'mtourleo@yellowbook.com', 'Martha Tourle', '1954-09-20', 'inactive'),
('swellp', 'uV6>!K@E04hRIx', 'swellp@yale.edu', 'Scotti Well', '1971-11-18', 'suspended'),
('iwahlbergq', 'rP4)Du1AHW', 'iwahlbergq@dropbox.com', 'Iago Wahlberg', '1995-11-30', 'inactive'),
('bzylbermannr', 'yS6.W0g=*"e', 'bzylbermannr@last.fm', 'Berrie Zylbermann', '1962-02-11', 'inactive'),
('tchritchleys', 'sS9)&L_3|&', 'tchritchleys@shinystat.com', 'Tommi Chritchley', '1978-04-29', 'suspended'),
('tturvillet', 'qY8,"+bo?&RB', 'tturvillet@chicagotribune.com', 'Taddeo Turville', '1985-04-19', 'inactive'),
('aschallu', 'cR2=1}Mz"mUYq!', 'aschallu@squidoo.com', 'Albrecht Schall', '1999-03-26', 'active'),
('nkobierskiv', 'mD7<@U>&W3&yS', 'nkobierskiv@tinypic.com', 'Neal Kobierski', '1989-12-23', 'active'),
('jcrawshayw', 'jX2''+s"91kQb=', 'jcrawshayw@nymag.com', 'Jenica Crawshay', '1999-12-26', 'inactive'),
('acunnowx', 'aM3%8htUY@2GWQ/', 'acunnowx@bravesites.com', 'Angeli Cunnow', '1986-02-22', 'suspended'),
('troachey', 'pM2(w`aaslE<', 'troachey@alibaba.com', 'Tammy Roache', '2002-07-05', 'active'),
('bblazewiczz', 'hZ7\\Os"7R7>%zFE', 'bblazewiczz@indiegogo.com', 'Brandie Blazewicz', '1982-08-05', 'suspended'),
('scoolahan10', 'dQ9&(u"AsW', 'scoolahan10@google.ru', 'Shanon Coolahan', '2000-08-30', 'active'),
('nroyse11', 'dY9~y._`F', 'nroyse11@miitbeian.gov.cn', 'Natalie Royse', '1962-07-10', 'inactive'),
('athody12', 'rL3=,s\\4HCC.u', 'athody12@prlog.org', 'Almeria Thody', '1956-04-27', 'inactive'),
('ktuite13', 'nA9,T#Oeq', 'ktuite13@fema.gov', 'Koo Tuite', '1999-11-21', 'active'),
('rgribben14', 'vE0\\oX<d)4LD', 'rgribben14@salon.com', 'Raffarty Gribben', '1965-02-21', 'suspended'),
('mfirpo15', 'aJ7|X!W%', 'mfirpo15@topsy.com', 'Meggi Firpo', '1980-03-18', 'inactive'),
('rcurrer16', 'pD3_>n@A%q', 'rcurrer16@artisteer.com', 'Redford Currer', '1991-01-19', 'inactive'),
('vjacklings17', 'iE1//j9w|)Vvk*', 'vjacklings17@dyndns.org', 'Victor Jacklings', '1993-01-10', 'active'),
('dneeve18', 'tR8|B0{X', 'dneeve18@fotki.com', 'Duff Neeve', '1959-03-12', 'inactive'),
('pmordey19', 'sV4"QvYT', 'pmordey19@nih.gov', 'Perla Mordey', '1975-12-08', 'suspended'),
('gdi1a', 'uR9*tE51BcI', 'gdi1a@rambler.ru', 'Gerri Di Lucia', '1971-12-09', 'inactive'),
('mmuggach1b', 'dD0+h&KbrX', 'mmuggach1b@illinois.edu', 'Maiga Muggach', '1992-04-26', 'inactive'),
('hjotham1c', 'mA2''RC2Mc\\R~', 'hjotham1c@blinklist.com', 'Harriot Jotham', '1959-12-07', 'active'),
('rhow1d', 'pS0\\)7&%k', 'rhow1d@cisco.com', 'Ross How', '1954-10-23', 'inactive');


-- 3. Car Table creation 
create table lyfter_car_rental.car_data (
	car_id SERIAL PRIMARY KEY,
	brand VARCHAR(50),
	model VARCHAR(50),
	factory_year INT,
	car_rental_status VARCHAR(11)
    );

INSERT INTO lyfter_car_rental.car_data 
(car_id, brand, model, factory_year, date_of_birth, car_rental_status) 
VALUES 
(1, 'Mercedes-Benz', 'SL-Class', 2017, 'avaialble'),
(2, 'Acura', 'NSX', 2007, 'avaialble'),
(3, 'Chevrolet', 'G-Series 3500', 2014, 'rented'),
(4, 'Mercedes-Benz', 'S-Class', 2015, 'avaialble'),
(5, 'Chevrolet', 'Camaro', 2015, 'avaialble'),
(6, 'Suzuki', 'Daewoo Magnus', 1994, 'avaialble'),
(7, 'Ferrari', 'F430', 1992, 'rented'),
(8, 'Dodge', 'Ram Van 1500', 1997, 'avaialble'),
(9, 'Buick', 'Century', 2002, 'avaialble'),
(10, 'Mitsubishi', 'Starion', 1998, 'rented'),
(11, 'Honda', 'Element', 2005, 'rented'),
(12, 'Pontiac', 'Grand Prix', 2013, 'avaialble'),
(13, 'Chevrolet', 'Cavalier', 2016, 'avaialble'),
(14, 'Buick', 'Park Avenue', 2010, 'avaialble'),
(15, 'Mitsubishi', 'Pajero', 2021, 'avaialble'),
(16, 'Nissan', 'Frontier', 1993, 'avaialble'),
(17, 'Ford', 'Econoline E350', 2019, 'rented'),
(18, 'Ford', 'Crown Victoria', 2004, 'rented'),
(19, 'Lexus', 'GX', 2003, 'rented'),
(20, 'Acura', 'Integra', 2012, 'avaialble'),
(21, 'Ford', 'Crown Victoria', 2015, 'rented'),
(22, 'GMC', 'Envoy', 2008, 'avaialble'),
(23, 'Volkswagen', 'New Beetle', 2018, 'rented'),
(24, 'Pontiac', 'Aztek', 1993, 'rented'),
(25, 'Buick', 'Park Avenue', 2025, 'avaialble'),
(26, 'Chevrolet', 'Tahoe', 2010, 'avaialble'),
(27, 'Nissan', 'Xterra', 2013, 'rented'),
(28, 'BMW', '760', 2002, 'avaialble'),
(29, 'Lincoln', 'Town Car', 1997, 'avaialble'),
(30, 'Saab', '9000', 1995, 'avaialble'),
(31, 'Toyota', 'Celica', 2010, 'avaialble'),
(32, 'Volkswagen', 'New Beetle', 2005, 'rented'),
(33, 'Volvo', '940', 2024, 'avaialble'),
(34, 'Pontiac', 'Solstice', 2001, 'rented'),
(35, 'Pontiac', 'Bonneville', 1999, 'avaialble'),
(36, 'Nissan', 'Sentra', 2019, 'avaialble'),
(37, 'Kia', 'Optima', 2005, 'avaialble'),
(38, 'Chevrolet', 'Corvette', 2016, 'avaialble'),
(39, 'Dodge', 'Neon', 2021, 'avaialble'),
(40, 'Pontiac', 'Sunfire', 2005, 'avaialble'),
(41, 'Dodge', 'Charger', 1997, 'rented'),
(42, 'Lexus', 'IS', 2008, 'avaialble'),
(43, 'GMC', 'Suburban 2500', 2010, 'avaialble'),
(44, 'Toyota', 'Camry', 2020, 'available'),
(45, 'Honda', 'Civic', 2018, 'rented'),
(46, 'Ford', 'Mustang', 2022, 'available'),
(47, 'BMW', 'X5', 2019, 'rented'),
(48, 'Audi', 'A4', 2021, 'available'),
(49, 'Tesla', 'Model 3', 2023, 'available'),
(50, 'Hyundai', 'Tucson', 2020, 'rented');

-- 4. Cross table to relate Car and Users with Rengals 
create table lyfter_car_rental.rental_information (
        rental_id SERIAL PRIMARY KEY,
        car_id INT NOT NULL references lyfter_car_rental.car_data(car_id),
        user_id INT NOT NULL references lyfter_car_rental.customer_car_rental_data(user_id),
        rent_request_date DATE not NULL default CURRENT_DATE,
        rent_start DATE,
        rent_end DATE,
        payment_status VARCHAR(10),
        rent_status VARCHAR(15)
        );

-- Part 2 test DB
-- a. script to add new user to db 
INSERT INTO lyfter_car_rental.customer_car_rental_data 
        (username, password, email, full_name, date_of_birth, account_status) 
        VALUES ('john20m', 'john123', 'jhohn@doe.com', 'John Doe', '1997-05-14', 'active');

-- b. script to add new car to db 
INSERT INTO lyfter_car_rental.car_data 
        (car_id, brand, model, factory_year, car_rental_status)
        VALUES ('BYD', 'Seagul', '2025', 'available');

-- c. script to modify the status of a user
UPDATE lyfter_car_rental.customer_car_rental_data
        SET account_status = 'inactive'
        WHERE user_id = 52

-- d. script to modify the status of a car 
UPDATE lyfter_car_rental.car_data
        SET car_rental_status = 'rented'
        WHERE car_id = 52

-- e. script to add a new rental with user and car rental information 
INSERT INTO lyfter_car_rental.rental_information 
        (car_id, user_id, rent_start, rent_end, payment_status, rent_status)
        VALUES (52, 51, '2025-11-15', '2025-11-30', 'completed', 'pending');

-- f script to complete a rental status and change the car to available 
UPDATE lyfter_car_rental.car_data 
SET car_rental_status = 'available'
WHERE car_id = 7;

UPDATE lyfter_car_rental.rental_information 
SET rent_status = 'completed',
    rent_end = CURRENT_DATE  
WHERE rental_id = 15;


-- g script to remove a car from available
UPDATE lyfter_car_rental.car_data
        SET car_rental_status = 'unavailable'
        WHERE car_id = 52


-- h. script to retrieve all rented cars and anotherone to retrieve all available cars 
SELECT * FROM lyfter_car_rental.car_data 
        WHERE car_rental_status = 'rented'

SELECT * FROM lyfter_car_rental.car_data 
        WHERE car_rental_status = 'available'