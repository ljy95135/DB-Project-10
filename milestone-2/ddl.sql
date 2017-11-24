# author: Jiangyi Lin
/*
This DDL is for MySQL
*/

drop table QuizQuestion, Quiz, Post, Link, Downloadable,
Contain, PlayList, LikeAnswer, Related, Answer, 
Question, CompleteMaterial, CourseMaterial, Interested, Buy, 
CompleteCourse, CreateCourse, SecondaryTopic, AdminPosition, Student, 
Faculty, Admin, Phone, User, Course;

CREATE TABLE User (
  Email VARCHAR(100) NOT NULL,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  PW VARCHAR(50) NOT NULL,
  ProfilePict blob NOT NULL,
  Country VARCHAR(50) NOT NULL,
  City VARCHAR(50) NOT NULL,
  Street VARCHAR(200)NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  PRIMARY KEY (Email)
);

CREATE TABLE Phone (
  Email VARCHAR(100) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  PRIMARY KEY (Email, Phone),
  FOREIGN KEY (Email) REFERENCES User(Email)
);

CREATE TABLE Student (
  Email VARCHAR(100) NOT NULL,
  PRIMARY KEY (Email),
  FOREIGN KEY (Email) REFERENCES User(Email)
);

CREATE TABLE Admin (
  Email VARCHAR(100) NOT NULL,
  GrantAdmin VARCHAR(100) NOT NULL,
  GrantTime DATETIME NOT NULL,
  PRIMARY KEY (Email),
  FOREIGN KEY (GrantAdmin) REFERENCES Admin(Email)
);

CREATE TABLE Faculty (
  Email VARCHAR(100) NOT NULL,
  Website VARCHAR(200) NOT NULL,
  Affiliation VARCHAR(50) NOT NULL,
  Title VARCHAR(300) NOT NULL,
  GrantAdmin VARCHAR(100) NOT NULL,
  GrantTime DATETIME NOT NULL,
  PRIMARY KEY (Email),
  FOREIGN KEY (Email) REFERENCES User(Email),
  FOREIGN KEY (GrantAdmin) REFERENCES Admin(Email)
);

CREATE TABLE AdminPosition (
  Email VARCHAR(100) NOT NULL,
  Position VARCHAR(200) NOT NULL,
  PRIMARY KEY (Email, Position),
  FOREIGN KEY (Email) REFERENCES Admin(Email)
);

CREATE TABLE Course (
  CID INT AUTO_INCREMENT,
  Name VARCHAR(100) NOT NULL,
  Description TEXT NOT NULL,
  Icon BLOB NOT NULL,
  Date DATETIME NOT NULL,
  Cost INT NOT NULL,
  PrimaryTopic VARCHAR(100) NOT NULL,
  PRIMARY KEY (CID)
);

CREATE TABLE SecondaryTopic (
  CID INT NOT NULL,
  SecondaryTopic VARCHAR(100) NOT NULL,
  PRIMARY KEY (CID, SecondaryTopic),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE CreateCourse (
  Email VARCHAR(100) NOT NULL,
  CID INT NOT NULL,
  PRIMARY KEY (Email, CID),
  FOREIGN KEY (Email) REFERENCES Faculty(Email),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE CompleteCourse (
  Email VARCHAR(100) NOT NULL,
  CID INT NOT NULL,
  Time DATETIME NOT NULL,
  Rating INT NOT NULL,
  Comment TEXT NOT NULL,
  PRIMARY KEY (Email, CID),
  FOREIGN KEY (Email) REFERENCES Student(Email),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE Buy (
  Email VARCHAR(100) NOT NULL,
  CID INT NOT NULL,
  Time DATETIME NOT NULL,
  Code VARCHAR(100) NOT NULL,
  PRIMARY KEY (Email, CID),
  FOREIGN KEY (Email) REFERENCES Student(Email),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE Interested (
  Email VARCHAR(100) NOT NULL,
  CID INT NOT NULL,
  PRIMARY KEY (Email, CID),
  FOREIGN KEY (Email) REFERENCES Student(Email),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE CourseMaterial (
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (CID, MaterialOrder),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE CompleteMaterial (
  Email VARCHAR(100) NOT NULL,
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  PRIMARY KEY (Email, CID, MaterialOrder),
  FOREIGN KEY (Email) REFERENCES Student(Email),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder)
);

CREATE TABLE Question (
  QID INT AUTO_INCREMENT,
  Title VARCHAR(100) NOT NULL,
  Text TEXT NOT NULL,
  Visible BOOLEAN,
  AskBy VARCHAR(100) NOT NULL,
  Time DATETIME NOT NULL,
  PRIMARY KEY (QID),
  FOREIGN KEY (AskBy) REFERENCES Student(Email)
);

CREATE TABLE Answer (
  Email VARCHAR(100) NOT NULL,
  QID INT NOT NULL,
  Text TEXT NOT NULL,
  PRIMARY KEY (Email, QID),
  FOREIGN KEY (Email) REFERENCES Faculty(Email),
  FOREIGN KEY (QID) REFERENCES Question(QID)
);

CREATE TABLE Related (
  QID INT NOT NULL,
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  PRIMARY KEY (QID, CID, MaterialOrder),
  FOREIGN KEY (QID) REFERENCES Question(QID),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder)
);

CREATE TABLE LikeAnswer (
  QID INT NOT NULL,
  Email VARCHAR(100) NOT NULL,
  PRIMARY KEY (Email, QID),
  FOREIGN KEY (Email) REFERENCES Faculty(Email),
  FOREIGN KEY (QID) REFERENCES Question(QID)
);

CREATE TABLE PlayList(
  Email VARCHAR(100) NOT NULL,
  Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (Email, Name),
  FOREIGN KEY (Email) REFERENCES User(Email)
);

CREATE TABLE Contain(
  Email VARCHAR(100) NOT NULL,
  Name VARCHAR(100) NOT NULL,
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  PRIMARY KEY (Email, Name, CID, MaterialOrder),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder),
  FOREIGN KEY (Email, Name) REFERENCES PlayList(Email, Name)
);

CREATE TABLE Post(
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  Text TEXT NOT NULL,
  PRIMARY KEY (CID, MaterialOrder),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder)
);

CREATE TABLE Link(
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  URL VARCHAR(200) NOT NULL,
  TagVedio BOOLEAN NOT NULL,
  PRIMARY KEY (CID, MaterialOrder),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder)
);

CREATE TABLE Downloadable(
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  Path VARCHAR(500) NOT NULL,
  Size Long NOT NULL,
  Type VARCHAR(50) NOT NULL,
  PRIMARY KEY (CID, MaterialOrder),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder)
);

CREATE TABLE Quiz(
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  PassingScore INT NOT NULL,
  PRIMARY KEY (CID, MaterialOrder),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder)
);

CREATE TABLE QuizQuestion(
  CID INT NOT NULL,
  MaterialOrder INT NOT NULL,
  Number INT NOT NULL,
  Text TEXT NOT NULL,
  Indicator BOOLEAN NOT NULL,
  Feedback TEXT NOT NULL,
  PRIMARY KEY (CID, MaterialOrder, Number),
  FOREIGN KEY (CID, MaterialOrder) REFERENCES CourseMaterial(CID, MaterialOrder)
);