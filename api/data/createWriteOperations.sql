-- create table statement
CREATE TABLE HEADLINES
(
	HEADLINE_DATE DATE, 
	TITLE TEXT,
	COUNTRIES TEXT,
	PUBLISHED_DATE DATE,
	DESCRIPTION TEXT, 
	SOURCE TEXT
);

-- example insert table statement 
INSERT INTO HEADLINES VALUES(
	'2016-03-30',
	'Patrolling Disputed Waters, U.S. and China Jockey for Dominance',
	'China UnitedStates',
	'2016-03-31',
	'BLANK DESCRIPTION',
	'BLANK SOURCE'
);

-- sample insert table statement from data
INSERT INTO HEADLINES VALUES 
('2016-03-30', 'Patrolling Disputed Waters, U.S. and China Jockey for Dominance', 'united states|china|dominica', '2016-03-31', '', 'New York Times'),
('2016-03-30', 'American Killed in Brussels Identified as Air Force Officers Wife', 'united states|chile', '2016-03-30', '', 'ABC News');