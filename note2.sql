create database 12_22;

-- 在创建表的时候 增加 
create table user(
	id int primary key,  -- 主键
	name varchar(20) not null,
	age int default 18
);

-- 插入数据
insert into user  values(1, 'which', 20);
insert into user  values(1, 'tuple', 19);  -- 不行 主键不能重复
insert into user(name, age)  values('tuple', 19); -- 不行 主键不能为空
insert into user values(3, 'tom', null);
insert into user values(4, null, 18);

-- 复合主键  
create table user1(
	id int,
	stu_number int,
	name varchar(20),
	age int,
	primary key(id, stu_number)
);

insert into user1(id, stu_number) values(1, 1);
insert into user1(id, stu_number) values(1, 2);
insert into user1(id, stu_number) values(2, 1);

-- 只要是张表 都有id字段 通常只要存在id字段 那么基本上都是主键

-- 删除 
alter table user drop primary key;

insert into user  values(1, 'which', 20);
-- 在表已经存在的时候增加 
alter table user add primary key(id); --  要保证主键字段 值不重复
delete from user where id =1;
insert into user  values(2, 'tuple', 19); 
alter table user modify id int primary key;

-- 在创建表的时候 增加 
create table user2(
	id int primary key auto_increment,
	name varchar(20) not null,
	age int default 18
);

insert into user2(name, age) values('which', 19);
insert into user2(name, age) values('tuple', 19);
insert into user2 values(default,'林', 19);
-- 查看下一个自增
show create table user2;

-- 不创建表的时候就加自增
alter table user2 modify age int auto_increment;

create table user3(
	name varchar(20) not null unique key,
	age int default 18
);
--主键 唯一且不能为空 当你表里没有主键 那么第一个唯一且不为空的字段 就会被认为主键
alter table user3 add primary key(age);
-- 有时候 看表结构 看到的并不一定是真实的 通过查看表创建过程

create table user4(
	name varchar(20) unique key, -- 唯一键,不能重复， 但是一张表可以有多个唯一键。
	age int
);
-- 空数据 不做比较
insert into user4 values('which', 18);
insert into user4 values('Which', 18);
insert into user4 values('tuple', 18);
insert into user4 values(null, 18);
insert into user4 values(null, 18);

-- insert into user values(4, 'tuple', 18);
-- insert into user values(5, 'Tuple', 18);

-- 外键 是关联；两张表的  表关系
-- 关系型数据库 
--  一张表的一个字段 指向另一张表的主键 那么这个字段就被称之为外键
-- create  table user6(
-- 	id int primary key auto_increment,
-- 	name varchar(20) not null,
-- 	age int
-- );

-- 在创建表的时候 增加 
create table user(
	id int primary key,
	name varchar(20) not null,
	age int default 18
);


create table aticle(
	id int primary key auto_increment,
	title varchar(20) not null,
	user_id int,
	foreign key(user_id) references user(id)
);

insert into article(title, user_id) values('这是测试标签111', 1); -- 不可以  因为父表没有id为1 的数据
insert into article(title, user_id) values('这是测试标签111', 2); -- 可以
insert into article(title, user_id) values('这是测试标签222', 2); -- 可以


create table user2(
	id int primary key auto_increment,
	name varchar(20) not null,
	age int default 18
);

create table article1(
	id int primary key auto_increment,
	title varchar(20) not null,
	user_id int,
	foreign key(user_id)  references user2(id) on delete cascade on update set null
);

insert into article1(title, user_id) values('这是测试标签111', 2); -- 可以
insert into article1(title, user_id) values('这是测试标签222', 3); -- 可以

-- 外键删除 
alter table article1 drop foreign key `article1_ibfk_1`;

-- 主键是怎么删的  一张表只有一个主键
alter table tableName drop primary key;

-- 删除唯一键
alter table user3 drop unique key(name); -- 不能
alter table user3 drop index `name`;