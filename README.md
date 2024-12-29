# AccessVault: A Comprehensive Database Solution for Role-Based Security Management

**This project involves designing and implementing a relational database system to manage discretionary access control for a database management system (DBMS). The primary focus is on creating a structured database schema, implementing it using SQL, and performing various queries and transactions to showcase functionality.**

## Overview
The project is divided into three main parts:

## Part 1: EER Schema Design
Design an Enhanced Entity-Relationship (EER) schema based on the specified requirements.
Document design decisions, assumptions, and any missing or incomplete requirements that were addressed.
Create a clear and comprehensive schema diagram.

##Part 2: Relational Database Schema Implementation
Map the EER schema to a relational schema.
Implement the relational schema using SQL with key and referential integrity constraints.
Document mapping decisions and any changes made to the initial EER design.

## Part 3: Data Loading, Transactions, and Queries
Populate the database with sample data, including user accounts, roles, tables, and privileges.

**Implement and test the following database update transactions:**

Add a new user account.
Add a new role.
Add a new table with its owner.
Add a new privilege and its type.
Relate a user account to a role.
Relate an account privilege to a role.
Relate a relation privilege, role, and table.

# Write queries to:
Retrieve all privileges for a specific role or user account.
Check if a specific privilege is granted to a user account.

# Features
Comprehensive schema design for managing discretionary access control.
Support for binary and ternary relationships among entities.
User-friendly interface for database transactions.
Queries to validate privileges and relationships.
# Technologies Used
## Database Systems: Oracle, MySQL
## Programming Languages: Python 
## Tools: SQLPlus, Draw.io, or MS Visio for diagrams

# Directions to Execute:-
**
1) Create the following tables by executing the following commands:-
 **
create table User_account (IDNO INTEGER PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PHONE CHAR(12) NOT NULL, CHECK (Name LIKE '_%.%' AND LENGTH(Name) <= 50));
 
create table user_role(RNAME VARCHAR(60) NOT NULL PRIMARY KEY,RACC_ID INT,DESCRIPTION VARCHAR(160),CONSTRAINT FK1 FOREIGN KEY (RACC_ID) REFERENCES USER_ACCOUNT(IDNO));
 
CREATE TABLE ACCOUNT_PRIVILEGE (

PRIVILEGENAME VARCHAR(50) NOT NULL,

PRIVILEGE_DESC VARCHAR(150),

ACC_ID INT NOT NULL,

RNAME VARCHAR(50),

PRIMARY KEY(PRIVILEGENAME,ACC_ID),

CONSTRAINT FK2 FOREIGN KEY (RNAME) REFERENCES USER_ROLE(RNAME));
 
CREATE TABLE RELATION_PRIVILEGE ( R_ID INT NOT NULL, PRIVILEGE_NAME VARCHAR(50) NOT NULL, PRIVILEGE_DESC VARCHAR(150), PRIMARY KEY(R_ID,PRIVILEGE_NAME));
 
CREATE TABLE TABLES ( T_NAME VARCHAR(30) NOT NULL,

O_ID INT NOT NULL,

PRIMARY KEY(T_NAME,O_ID),

CONSTRAINT FK3 FOREIGN KEY (O_ID) REFERENCES USER_ACCOUNT(IDNO));
 
CREATE INDEX idx_privilege_name ON RELATION_PRIVILEGE (PRIVILEGE_NAME);
 
 
CREATE TABLE HAS_PREDEFINED ( T_NAME VARCHAR(30) NOT NULL,

RNAME VARCHAR(45) NOT NULL,

PRIVILEGE_NAME VARCHAR(45) NOT NULL,

R_ID INT NOT NULL,
 
PRIMARY KEY(T_NAME,RNAME,PRIVILEGE_NAME,R_ID),

CONSTRAINT FK5 FOREIGN KEY (T_NAME) REFERENCES TABLES(T_NAME),

CONSTRAINT FK6 FOREIGN KEY (RNAME) REFERENCES USER_ROLE(RNAME),

CONSTRAINT FK4 FOREIGN KEY (PRIVILEGE_NAME) REFERENCES RELATION_PRIVILEGE(PRIVILEGE_NAME),

CONSTRAINT FK7 FOREIGN KEY (R_ID) REFERENCES RELATION_PRIVILEGE(R_ID));
 
**2) Put your ID , password and database in 'sqlApp.py' file 
**
