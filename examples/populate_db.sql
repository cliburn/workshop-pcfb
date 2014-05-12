create table people (
       	id integer primary key,
	name varchar, 
	position varchar,
	phone varchar,
	office varchar
);

create table experiment (
	id integer primary key,
	name varchar,
	researcher integer,
	description text,
	foreign key(researcher) references people(id)
);

	
insert into people values (0, 'Alice', 'Research Director', '555-123-0001', '4b');
insert into people values (1, 'Bob', 'Research assistant', '555-123-0002', '17');
insert into people values (2, 'Charles', 'Research assistant', '555-123-0001', '24');
insert into people values (3, 'David', 'Research assistant', '555-123-0001', '8');

insert into experiment values ( 0, 'EPV Vaccine trial', 0, 'A vaccine trial');
insert into experiment values ( 1, 'Flu antibody study', 2, 'Study of the morphology of flu antibodies');

