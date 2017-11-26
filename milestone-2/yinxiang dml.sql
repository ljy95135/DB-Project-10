/*
Show all the questions that has likes from students and show the student ID and email of whom asked the question,as well as the total likes that a question has.

1.3 joins
2.natural join
3.aggregation function 
4.order
5.group
6.strong purpose
*/
Select User.UserID as UID,User.Email as email,count(*) as num_likes,Question.QID as QID,Question.Title as title from ((Question natural join Likequestion) join User on User.UserID=Question.AskBy) group by Question.QID order by num_likes desc,email desc


/*
For all the playlists that users created,count the material order that is included most among the playlists

1. 3 joins
2.Order
3.Group
4.Subqueries
5.Aggregation function
6.Natural join 
7.	where

*/
Select num as max_num,CMID from(select count(*) as num,CourseMaterial.CMID as CMID from ((Contain join PlayList on Contain.Name=PlayList.Name and Contain.UserID=PlayList.UserID) join CourseMaterial on Contain.CMID=CourseMaterial.CMID) group by CMID) q where num=(select max(num) from (select count(*) as num,CourseMaterial.CMID as CMID from ((Contain join PlayList on Contain.Name=PlayList.Name and Contain.UserID=PlayList.UserID) join CourseMaterial on Contain.CMID=CourseMaterial.CMID) group by CMID) q2) order by CMID,max_num

/*
Calculate the total cost of every students.

1.3 join
2.natural join
3.Aggregation function
4.orderGroup
5.Order
6.Having
*/
select sum(cost) as total_cost,User.UserID as UserID from ((course Natural join BuyCourse) join User on User.UserID=BuyCourse.UserID) group by UserID having total_cost>1000 order by total_cost desc,UserID


/*
calculate all the main topics that is included for all the questions that are asked by students.

1.  3 join
2.natural join
3.Aggregate
4.Group
5.Order
6.Having 
7.motivation
*/
Select Topic.Name as name,count(*) as num from ((((Question natural join Related) join CourseMaterial on Related.CMID=CourseMaterial.CMID) join Course on Course.CID=CourseMaterial.CID) join Topic on Topic.TID=Course.PrimaryTopic)  group by Course.PrimaryTopic having num>3 order by num desc,name asc

