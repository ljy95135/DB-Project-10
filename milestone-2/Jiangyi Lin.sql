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
-- admin
INSERT INTO admin (UserID, GrantAdmin, GrantTime)
VALUES (1, 1, NOW());

-- faculty

-- c)
/*
param:
UserID : The student to see
*/
-- enrolled
SELECT c.Name, t1.Name, t2.Name
FROM ((Course c INNER JOIN SecondaryTopic st ON c.CID = st.CID)
INNER JOIN Topic t1 ON t1.TID = st.TID)
INNER JOIN Topic t2 ON t2.TID = c.PrimaryTopic
WHERE c.CID IN (
    SELECT CID
    FROM BuyCourse bc
    WHERE bc.UserID = 1)
ORDER BY c.AvgRate DESC;

-- compeleted
SELECT c.Name, t1.Name, t2.Name
FROM ((Course c INNER JOIN SecondaryTopic st ON c.CID = st.CID)
INNER JOIN Topic t1 ON t1.TID = st.TID)
INNER JOIN Topic t2 ON t2.TID = c.PrimaryTopic
WHERE c.CID IN (
    SELECT CID
    FROM BuyCourse bc
    WHERE bc.UserID = 1 AND bc.IsCompelete)
ORDER BY c.AvgRate DESC;

-- Interested
