-- I will use Django in my application, and some information like UserID will not be necessary to provide

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
VALUES (17, 1, NOW());

-- faculty
INSERT INTO faculty (UserID, Website, Affiliation, Title, GrantAdmin, GrantTime)
VALUES (17, 'www.example1.com', 'Affilation1', 'Title1', 1, NOW());

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
    WHERE bc.UserID = 16)
ORDER BY c.AvgRate DESC;

-- completed
SELECT c.Name, t1.Name, t2.Name
FROM ((Course c INNER JOIN SecondaryTopic st ON c.CID = st.CID)
INNER JOIN Topic t1 ON t1.TID = st.TID)
INNER JOIN Topic t2 ON t2.TID = c.PrimaryTopic
WHERE c.CID IN (
    SELECT CID
    FROM BuyCourse bc
    WHERE bc.UserID = 16 AND bc.IsComplete)
ORDER BY c.AvgRate DESC;

-- Interested
SELECT c.Name, t1.Name, t2.Name
FROM ((Course c INNER JOIN SecondaryTopic st ON c.CID = st.CID)
INNER JOIN Topic t1 ON t1.TID = st.TID)
INNER JOIN Topic t2 ON t2.TID = c.PrimaryTopic
WHERE c.CID IN (
    SELECT CID
    FROM Interested i
    WHERE i.UserID = 16)
ORDER BY c.AvgRate DESC;

-- d)
/*
param:
UserID: The user who wants to enroll this course
*/
INSERT INTO BuyCourse (UserID, CID, BuyTime, Code, IsComplete, CompleteTime, Rating, Comment) 
VALUES ( 16, 1, '2017-04-15 08:00:00', 'djgen3j5', 0, NULL, 90, 'Good');

-- e)
/*
param:
UserID: The student who has enrolled this course
CID: The CID of this course
*/
-- The course materials which have been completed
SELECT cm.CMID AS completed_CM, cm.Name
FROM CourseMaterial cm
WHERE cm.CID = 7 AND cm.CMID
IN (SELECT cpm.CMID FROM CompleteMaterial cpm
WHERE cpm.UserID = 24)
ORDER BY cm.CMID;

-- The course materials which have not been completed
SELECT cm.CMID AS Incompleted_CM, cm.Name
FROM CourseMaterial cm
WHERE cm.CID = 7 AND cm.CMID
NOT IN (SELECT cpm.CMID FROM CompleteMaterial cpm
WHERE cpm.UserID = 24)
ORDER BY cm.CMID;

-- f)
/*
param: 
UserID: The student who has enrolled this course material
CID: The CID which this course material belongs to
*/
-- Mark course material as having been completed by a student
INSERT INTO CompleteMaterial (CMID, UserID, CompleteTime)
VALUES ( 30, 24, '2017-11-25 21:00:00');

-- count the number of completed course materials
SELECT COUNT(cpm.CMID) AS numsOfcpm
FROM (Course c INNER JOIN CourseMaterial cm ON c.CID = cm.CID)
INNER JOIN CompleteMaterial cpm ON cm.CMID = cpm.CMID
WHERE cpm.UserID = 24 AND c.CID = 7;

-- count the number of total course materials
SELECT COUNT(cm.CMID) AS numsOfcm
FROM Course c INNER JOIN CourseMaterial cm ON c.CID = cm.CID
WHERE c.CID = 7;

-- if the two above results are equal, then update this course to be completed
UPDATE BuyCourse
SET IsComplete = 1, CompleteTime = '2017-11-25 21:00:00', Rating = 4, Comment = 'quite well'
WHERE UserID = 24 AND CID = 7;

-- g)
/*
param:
UserID : The user you want to check
*/
SELECT c.Name, bc.CompleteTime
FROM BuyCourse bc INNER JOIN Course c ON bc.CID = c.CID
WHERE bc.IsComplete AND bc.UserID = 16
ORDER BY bc.CompleteTime;

-- h)
/*
param:
UserID : The user you want to check
*/
-- enroll time/complete time/cost/code
SELECT c.Name, c.Cost, bc.Code, bc.buyTime, bc.CompleteTime
FROM BuyCourse bc INNER JOIN Course c ON bc.CID = c.CID
WHERE bc.IsComplete AND bc.UserID = 16
ORDER BY bc.CompleteTime;

-- total spent
SELECT SUM(c.Cost)
FROM BuyCourse bc INNER JOIN Course c ON bc.CID = c.CID
WHERE bc.IsComplete AND bc.UserID = 16;
