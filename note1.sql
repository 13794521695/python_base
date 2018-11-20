-- 创建数据库
create database 12_20;

-- 使用数据库
use 12_20;

create table user(
	name varchar(20),
	age int
)

-- 查看表结构
desc user;
describe user;
show columns from user;

-- 查看表的创建过程 
show create table user; == show create table user\g
-- 更加直观点
show create table user\G

-- 插入数据
insert into user  values('which', 18);
insert into user(age)  values(18);
insert into user values('tuple', 20),('林泷', 20),('qq', 18);
insert into user(age, name) values(10, 'qwe');

-- 查询
select * from user; -- 查询所有
select name, age from user; -- 指定字段查询

-- 改/更新
update user set name = 'Which';  -- 改的是整张表的name
update user set name = 'Tuple' where age = 20; -- 指定修改年龄为20

-- 删除 是最简单  where 后面是条件
delete from user; -- 删除整表
delete from user where age = 18;

-- 修改表
-- 修改表名
rename table user to user666;
-- 修改表结构
-- 新增(add) 、 修改(modify) 、重命名(change)、 删除(drop)  alter
-- 新增
alter table user add gender varchar(10);
-- 修改 （自己的字段名字不能改）
alter table user modify name varchar(30);
-- 修改字段名字
alter table user change name usernmae varchar(20);
-- 删除是最简单的 
alter table user drop gender;
-- 指定位置 first表示第一个
alter table user add gender char(10) first;
-- after 在..后  
alter table user add test char(10) after usernmae;
-- 修改
alter table user change usernmae username varchar(20) first;

/*
	介绍数据类型
		字符类型
			varchar(10) 变长字符串
			char(20)	定长字符串
			text   		文本类型 
		数值类
			int 		 整形    
			tinyint		微整形   符号
		时间日期
			datetime

*/			
create table `my_type`(
	s1 varchar(20),
	s2 char(20),
	s3 text,
	i1 int, -- 
	i2 tinyint,
	d1 datetime
)

insert into my_type values('这是s1', '这是s2', '这是s3', '1','2', '2017-12-20 21:41:40');

insert into my_type values('这是s1', '这是s2', '这是s3', '1w','2', '2017-12-20 21:41:40');


-- 重点  约束 
-- null / not null
-- 在建表的时候 直接设置非空
create table user1(
	name varchar(20) not null,
	age  int
);
-- 插入数据
insert into user1 values('which', 18); -- 都不为空
insert into user1(name) values('which');-- age 为空
insert into user1(age) values(18);	-- name 为空

-- 在建表的时候 直接设置默认值
create table user2(
	name varchar(20) not null,
	age  int default 18,
);

-- 验证
insert into user2 values('which', null); 
insert into user2(name) values('which');
insert into user2 values('which', default);

-- 在建表的时候 直接设置默认值
create table user3(
	name varchar(20) not null comment '名字',
	age  int default 18 comment '年龄',
	gender varchar(3) comment '性别',
	mz   varchar(20) comment '名字'
);

-- 当表已经存在 修改字段