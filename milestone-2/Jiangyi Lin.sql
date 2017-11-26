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
INSERT INTO faculty (UserID, Website, Affiliation, Title, GrantAdmin, GrantTime)
VALUES (1, 'www.example1.com', 'Affilation1', 'Title1', 1, NOW());

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

-- completed
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
SELECT c.Name, t1.Name, t2.Name
FROM ((Course c INNER JOIN SecondaryTopic st ON c.CID = st.CID)
INNER JOIN Topic t1 ON t1.TID = st.TID)
INNER JOIN Topic t2 ON t2.TID = c.PrimaryTopic
WHERE c.CID IN (
    SELECT CID
    FROM Interested i
    WHERE i.UserID = 1)
ORDER BY c.AvgRate DESC;

-- g)
/*
param:
UserID : The user you want to check
*/
SELECT c.Name, bc.CompleteTime
FROM BuyCourse bc INNER JOIN Course c ON bc.CID = c.CID
WHERE bc.IsComplete AND bc.UserID = 1
ORDER BY bc.CompleteTime;

-- h)
/*
param:
UserID : The user you want to check
*/
-- enroll time/complete time/cost/code
SELECT c.Name, c.Cost, bc.Code, bc.buyTime, bc.CompleteTime
FROM BuyCourse bc INNER JOIN Course c ON bc.CID = c.CID
WHERE bc.IsComplete AND bc.UserID = 1
ORDER BY bc.CompleteTime;

-- total spent
SELECT SUM(c.Cost)
FROM BuyCourse bc INNER JOIN Course c ON bc.CID = c.CID
WHERE bc.IsComplete AND bc.UserID = 1;

-- 1 complex report
/*
Find all faculties who teach at least more than 100 students course
that are not free and have rate higher than 90 points.
*/
SELECT u.FirstName AS FirstName, u.LastName AS LastName
FROM User u
WHERE u.UserID IN(
    SELECT DISTINCT(f.UserID)
    FROM Faculty f INNER JOIN CreateCourse cc ON f.UserID = cc.UserID
    WHERE cc.CID IN (
        SELECT c.CID
        FROM BuyCourse bc INNER JOIN Course c ON bc.CID = c.CID
        WHERE c.Cost > 0 AND c.AvgRate > 90
        GROUP BY c.CID
        HAVING COUNT(*)>100
))
ORDER BY FirstName, LastName;