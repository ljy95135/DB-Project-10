-- author: Jiangyi Lin

-- a)
/*
param:
Email : User's Email, must be unique
FirstName : User's FirstName
LastName : User's LastName
PW : User's PW's hashcode
ProfilePict : relative address of User's icon
Country, City, Street, PostalCode : User's physical address


UserID will be generated automatically.
*/
INSERT INTO user (Email, FirstName, LastName, PW, ProfilePict, Country, City, Street, PostalCode) 
VALUES ('happy.lin.jiangyi@gmail.com', 
        'Jiangyi', 
		'Lin', 
		'12345', 
		'1_icon', 
		'USA', 
		'Boston', 
		'123 St.'
		,'12345');

-- b)
/*
param:
UserID : The user you want to grant

GrantAdmin will be decided automatically in web app (you will login first)
As an special example, the first User grant himself as the admin
*/
INSERT INTO admin (UserID, GrantAdmin, GrantTime)
VALUES (1, 1, NOW());