
--d)
/*
param:
UserID: The user who wants to enroll this course
*/
INSERT INTO BuyCourse (UserID, CID, BuyTime, Code, IsComplete, CompleteTime, Rating, Comment) 
VALUES ( 16, 1, '2017-04-15 08:00:00', 'djgen3j5', 0, NULL, 90, 'Good');

--e)
/*
param:
UserID: The student who has enrolled this course
CID: The CID of this course
*/
--The course materials which have been completed
SELECT cm.CMID AS completed_CM, cm.Name
FROM CourseMaterial cm
WHERE cm.CID = 7 AND cm.CMID
IN (SELECT cpm.CMID FROM CompleteMaterial cpm
WHERE cpm.UserID = 24)
ORDER BY cm.CMID;

--The course materials which have not been completed
SELECT cm.CMID AS Incompleted_CM, cm.Name
FROM CourseMaterial cm
WHERE cm.CID = 7 AND cm.CMID
NOT IN (SELECT cpm.CMID FROM CompleteMaterial cpm
WHERE cpm.UserID = 24)
ORDER BY cm.CMID;

--f)
/*
param: 
UserID: The student who has enrolled this course material
CID: The CID which this course material belongs to
*/
--Mark course material as having been completed by a student
INSERT INTO CompleteMaterial (CMID, UserID, CompleteTime)
VALUES ( 30, 24, '2017-11-25 21:00:00');

--count the number of completed course materials
SELECT COUNT(cpm.CMID) AS numsOfcpm
FROM (Course c INNER JOIN CourseMaterial cm ON c.CID = cm.CID)
INNER JOIN CompleteMaterial cpm ON cm.CMID = cpm.CMID
WHERE cpm.UserID = 24 AND c.CID = 7;

-- count the number of total course materials
SELECT COUNT(cm.CMID) AS numsOfcm
FROM Course c INNER JOIN CourseMaterial cm ON c.CID = cm.CID
WHERE c.CID = 7;

--if the two above results are equal, then update this course to be completed
UPDATE BuyCourse
SET IsComplete = 1, CompleteTime = '2017-11-25 21:00:00', Rating = 4, Comment = 'quite well'
WHERE UserID = 24 AND CID = 7;
