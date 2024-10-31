create database dbmsproj;
use dbmsproj;

create table student(
    s_id varchar(10) primary key,
    name varchar(20) NOT NULL,
    mobileno bigint NOT NULL,
    birth_date date NOT NULL,
    address varchar(50) NOT NULL,
    email_id varchar(50) NOT NULL,
    check (mobileno between 1000000000 and 9999999999)
);

create table course(
    course_id varchar(10) primary key,
    cname varchar(20) NOT NULL
);

create table stud_course(
    s_id varchar(10),
    course_id varchar(20),
    primary key (s_id,course_id),
    foreign key (s_id) references student(s_id) ON DELETE CASCADE ON UPDATE CASCADE,
    foreign key (course_id) references course(course_id) on delete cascade on update CASCADE
);

create table dept(
    dept_id varchar(20) primary key,
    dept_name varchar(50)
);

create table dept_course(
    course_id varchar(20),
    dept_id varchar(20),
    primary key (course_id,dept_id),
    foreign key(course_id) references course(course_id) on delete cascade on update cascade,
    foreign key (dept_id) references dept (dept_id) on delete cascade on update cascade
);

create table faculty(
    f_id varchar(20) primary key,
    f_name varchar(50) not NULL,
    qualification varchar(50) NOT NULL,
    mobileno bigint NOT NULL,
    email_id varchar(50) not null,
    check (mobileno between 1000000000 and 9999999999)
);

create table dept_faculty(
    dept_id varchar(20),
    f_id varchar(20),
    from_date date NOT NULL,
    to_date date,
    primary key(dept_id,f_id),
    foreign key (dept_id) references dept(dept_id) on delete cascade on update cascade,
    foreign key (f_id) references faculty(f_id) on delete cascade on update cascade
);

create table subjects(
    sub_code varchar(20) primary key,
    sun_name varchar(50) NOT NULL,
    credit int NOT NULL
);

create table sub_faculty(
    f_id varchar(20),
    sub_code varchar(20),
    no_of_hours int,
    academic_yr varchar(9),
    primary key (f_id,sub_code,academic_yr),
    foreign key (f_id) references faculty(f_id) on delete cascade on update cascade,
    foreign key (sub_code) references subjects (sub_code) on delete cascade on update cascade
);

create table stud_sub_attent(
    s_id varchar(20),
    sub_code varchar(20),
    attented_hr int not null,
    primary key(s_id,sub_code),
    foreign key (s_id) references student (s_id) on delete cascade on update cascade,
    foreign key (sub_code) references subjects (sub_code) on delete cascade on update cascade
);

create table stud_sub_study(
    s_id varchar(20),
    sub_code varchar(20),
    chance int,
    primary key(s_id,sub_code,chance),
    foreign key (s_id) references student(s_id) on delete cascade on update cascade,
    foreign key (sub_code) references subjects(sub_code) on delete cascade on update cascade

);
