# author: Jiangyi Lin
/*
This DDL is for MySQL
*/

drop table QuizQuestion, Quiz, Post, Link, Downloadable,
Contain, PlayList, LikeQuestion, Related, Answer, 
Question, CompleteMaterial, CourseMaterial, Interested,
BuyCourse, CreateCourse, SecondaryTopic, Course, Topic,
AdminPosition, Faculty, Admin, Phone, User;

CREATE TABLE User (
  UserID INT AUTO_INCREMENT,
  Email VARCHAR(100) NOT NULL,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  PW VARCHAR(300) NOT NULL, # it is the hash of PW after adding salt.
  ProfilePict VARCHAR(50) NOT NULL, # address of the icon
  Country VARCHAR(50) NOT NULL,
  City VARCHAR(50) NOT NULL,
  Street VARCHAR(200)NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  PRIMARY KEY (UserID),
  UNIQUE (Email)
);

CREATE TABLE Phone (
  UserID INT NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  PRIMARY KEY (UserID, Phone),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE Admin (
  UserID INT NOT NULL,
  GrantAdmin INT NOT NULL,
  GrantTime DATETIME NOT NULL,
  PRIMARY KEY (UserID),
  FOREIGN KEY (GrantAdmin) REFERENCES Admin(UserID)
);

CREATE TABLE Faculty (
  UserID INT NOT NULL,
  Website VARCHAR(200) NOT NULL,
  Affiliation VARCHAR(50) NOT NULL,
  Title VARCHAR(300) NOT NULL,
  GrantAdmin INT NOT NULL,
  GrantTime DATETIME NOT NULL,
  PRIMARY KEY (UserID),
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (GrantAdmin) REFERENCES Admin(UserID)
);

CREATE TABLE AdminPosition (
  UserID INT NOT NULL,
  Position VARCHAR(200) NOT NULL,
  PRIMARY KEY (UserID, Position),
  FOREIGN KEY (UserID) REFERENCES Admin(UserID)
);

CREATE TABLE Topic (
  TID INT AUTO_INCREMENT,
  Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (TID)
);

CREATE TABLE Course (
  CID INT AUTO_INCREMENT,
  Name VARCHAR(100) NOT NULL,
  Description TEXT NOT NULL,
  Icon BLOB NOT NULL,
  Date DATETIME NOT NULL,
  Cost INT NOT NULL,
  PrimaryTopic INT NOT NULL,
  PRIMARY KEY (CID),
  FOREIGN KEY (PrimaryTopic) REFERENCES Topic(TID)
);

CREATE TABLE SecondaryTopic (
  CID INT NOT NULL,
  TID INT NOT NULL,
  PRIMARY KEY (CID, TID),
  FOREIGN KEY (CID) REFERENCES Course(CID),
  FOREIGN KEY (TID) REFERENCES Topic(TID)
);

CREATE TABLE CreateCourse (
  UserID INT NOT NULL,
  CID INT NOT NULL,
  PRIMARY KEY (UserID, CID),
  FOREIGN KEY (UserID) REFERENCES Faculty(UserID),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE BuyCourse (
  UserID INT NOT NULL,
  CID INT NOT NULL,
  BuyTime DATETIME NOT NULL,
  Code VARCHAR(100) NOT NULL,
  IsCompelete BOOLEAN NOT NULL,
  CompeleteTime DATETIME NOT NULL,
  Rating INT NOT NULL,
  Comment TEXT NOT NULL,
  PRIMARY KEY (UserID, CID),
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE Interested (
  UserID INT NOT NULL,
  CID INT NOT NULL,
  PRIMARY KEY (UserID, CID),
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE CourseMaterial (
  CMID INT AUTO_INCREMENT,
  CID INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (CMID, CID),
  FOREIGN KEY (CID) REFERENCES Course(CID)
);

CREATE TABLE CompleteMaterial (
  CMID INT NOT NULL,
  UserID INT NOT NULL,
  CompleteTime DATETIME NOT NULL,
  PRIMARY KEY (CMID, UserID),
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID)
);

CREATE TABLE Question (
  QID INT AUTO_INCREMENT,
  Title VARCHAR(100) NOT NULL,
  Text TEXT NOT NULL,
  Visible BOOLEAN,
  AskBy INT NOT NULL,
  Time DATETIME NOT NULL,
  PRIMARY KEY (QID),
  FOREIGN KEY (AskBy) REFERENCES User(UserID)
);

CREATE TABLE Answer (
  UserID INT NOT NULL,
  QID INT NOT NULL,
  Text TEXT NOT NULL,
  PRIMARY KEY (UserID, QID),
  FOREIGN KEY (UserID) REFERENCES Faculty(UserID),
  FOREIGN KEY (QID) REFERENCES Question(QID)
);

CREATE TABLE Related (
  QID INT NOT NULL,
  CMID INT NOT NULL,
  PRIMARY KEY (QID, CMID),
  FOREIGN KEY (QID) REFERENCES Question(QID),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID)
);

CREATE TABLE LikeQuestion (
  QID INT NOT NULL,
  UserID INT NOT NULL,
  PRIMARY KEY (UserID, QID),
  FOREIGN KEY (UserID) REFERENCES Faculty(UserID),
  FOREIGN KEY (QID) REFERENCES Question(QID)
);

CREATE TABLE PlayList(
  UserID INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (UserID, Name),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE Contain(
  UserID INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  CMID INT NOT NULL,
  PRIMARY KEY (UserID, Name, CMID),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID),
  FOREIGN KEY (UserID, Name) REFERENCES PlayList(UserID, Name)
);

CREATE TABLE Post(
  CMID INT NOT NULL,
  Text TEXT NOT NULL,
  PRIMARY KEY (CMID),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID)
);

CREATE TABLE Link(
  CMID INT NOT NULL,
  URL VARCHAR(200) NOT NULL,
  TagVedio BOOLEAN NOT NULL,
  PRIMARY KEY (CMID),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID)
);

CREATE TABLE Downloadable(
  CMID INT NOT NULL,
  Path VARCHAR(500) NOT NULL,
  Size Long NOT NULL,
  Type VARCHAR(50) NOT NULL,
  PRIMARY KEY (CMID),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID)
);

CREATE TABLE Quiz(
  CMID INT NOT NULL,
  PassingScore INT NOT NULL,
  PRIMARY KEY (CMID),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID)
);

CREATE TABLE QuizQuestion(
  CMID INT NOT NULL,
  Number INT NOT NULL,
  Text TEXT NOT NULL,
  Indicator BOOLEAN NOT NULL,
  Feedback TEXT NOT NULL,
  PRIMARY KEY (CMID, Number),
  FOREIGN KEY (CMID) REFERENCES CourseMaterial(CMID)
);