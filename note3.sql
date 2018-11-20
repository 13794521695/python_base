create database 12_25;

-- 学院
create table department(
	id int primary key auto_increment,
	name  varchar(20) not null
);

-- 学生
create table student(
	id int primary key auto_increment,
	name varchar(10) not null,
	dep_id int,
	constraint `idx_dep_id` foreign key(dep_id) references department(id)
)

-- 插入数据 
insert into department(name) values('python学院'), ('web学院'), ('java学院');
insert into student(name, dep_id) values('tom', 3), ('hank', 2);

-- 创建学生详细表
create table student_detail(
	id int primary key auto_increment,
	address varchar(100),
	foreign key(id) references student(id)
);
-- 插入数据
insert into student_detail(address)  values('bj'),('sj');
insert into student_detail(address)  values('s'); -- 不行

-- 创建老师表
create table teacher(
	id int primary key auto_increment,
	name varchar(10) not null
);

-- 中间表
create table teacher_stu(
	stu_id int,
	teacher_id int,
	primary key(stu_id, teacher_id),
	foreign key(stu_id) references student(id),
	foreign key(teacher_id) references teacher(id)
);

-- 插入数据
insert into student(name, dep_id) values('tank', 1), ('嘻嘻', 2);
insert into teacher(name)  values('Tuple'), ('Which');
insert into teacher_stu(teacher_id, stu_id)  values(1, 1),(1, 3),(2, 1);


create table adv_query(
	id int primary key auto_increment,
	name varchar(20),
	age int,
	gender varchar(10)
);

insert into adv_query(name, age, gender) values('Which', 18, 'male');
insert into adv_query(name, age, gender) values('Tuple', 20, 'male');
insert into adv_query(name, age, gender) values('嘻嘻', 25, 'male');
insert into adv_query(name, age, gender) values('哈哈', 18, 'male');
insert into adv_query(name, age, gender) values('Rose', 16, 'female');
insert into adv_query(name, age, gender) values('缇子', 28, 'female');
insert into adv_query(name, age, gender) values('林泷', 25, 'female');
insert into adv_query(name, age, gender) values('佳能', 15, 'male');
insert into adv_query(name, age, gender) values('呵呵', 20, 'male');
insert into adv_query(name, age, gender) values('hank', 20, 'female');


-- 查询一张表的数据
select * from adv_query;
-- 查询某一列
select name,age from adv_query;
-- 查询条件
select * from adv_query where age > 18;
select * from adv_query where age <> 18;
select * from adv_query where age = 18;
select * from adv_query where age = 18 and name='Which';
select * from adv_query where age = 18 or name='Which';
-- && (and)  || (or)
select * from adv_query where age = 18 || name='Which';
select * from adv_query where age = 18 && name='Which';
select * from adv_query where age <= 18 and age > 18;
-- as ==> alias
select name as '名字', age as '年龄' from adv_query;
select name '名字', age '年龄' from adv_query;

-- limit
select name from adv_query limit 5;
delete from adv_query limit 5;     -- 删除前面五条。

-- 清空表 初始化   id会从1开始， 如果用delete，下次插入的时候会从上一次的位置开始
truncate adv_query;

create table test(
	id int primary key auto_increment,
	age int
);

insert into test(age)  values(12),(12),(13),(14);

-- 分组
select gender from adv_query  group by gender;   -- 相同的分为一个组。
select gender,count(*), max(age), min(age), avg(age), sum(age) from adv_query group by gender;
-- 统计男 有多少多个， 最大年龄是多少，最小年龄是多少，平均年龄是多少，合计是多少。

select gender,count(*) from adv_query group by gender having count(*)>5;
select name, age from adv_query having gender = 'male'; -- 不行   having后面的字段必须是select后面出现的字段，where却可以，这是两者不同的地方
select name, age from adv_query where gender = 'male';
select gender,count(*), max(age) from adv_query group by gender having max(age)>25;

select * from adv_query order by id;   -- 升序排序
select * from adv_query order by age;
select * from adv_query order by age asc;
select * from adv_query order by age desc;  -- 降序排序时
select * from adv_query order by name; -- 用的不多

select * from student, student_detail;  --笛卡尔积，没意义，很多重读数据

select * from  student




union
select * from  student_detail;  -- 不行 字段数不一致   多表查询，union  字段数不一样，不能用union


select id, name from  student
union
select id, address from  student_detail;   --其实就两张表查询结果的拼接，第二种结果打印在接第一种结果下面。

select id,name from  student
union -- 重复数据过滤
select id,name from  adv_query;  -- 虽然字段一样，但是第一种情况的结果还是接在第二种情况的下面。

select name, dep_id from  student
union -- 重复数据过滤
select id, name from  adv_query; 

insert into adv_query(name, age, gender) values('呵呵', 20, 'male');
insert into adv_query(name, age, gender) values('hank', 20, 'female');

-- 没有条件内连接
select * from student join student_detail;
select * from student, student_detail;

-- 能查出学生和学生地址
select * from student join student_detail on student.id = student_detail.id;

-- 外连接
-- 左表   left  join  右表
select * from student left join student_detail on student.id = student_detail.id; --左外连接，字段可以出现空值，内连接是不允许的。
select * from student right join student_detail on student.id = student_detail.id;
--左连接已左表为主，无论左边的数据能不能被匹配，都会保留， 右外连接，无论右表数据能不能被匹配，都会保留

-- 左表   left  join  右表
select * from student_detail left join student on student.id = student_detail.id;




-- 事务
create table account(
	name varchar(10),
	money int
);

-- 开启事务：  start transaction     开启事务后， 在没有提交之前，在其他平台查询的不会变， 只有提交后。
-- 提交事务： commit
--  回滚事务：  rollback。

insert into account  values('which', 100);   -- 有一百块
insert into account  values('Tuple', 500);   -- 有500块

-- 500 读
-- 500 - 100 
-- 400 存   -- 断电了
-- 100 读
-- 100+ 100
-- 200 存
update account set money = money-100 where name='Tuple'; -- 断电了
update account set money = money+100 where name ='Which';

-- 作业 自己练习 
-- tzpyxw@qq.com