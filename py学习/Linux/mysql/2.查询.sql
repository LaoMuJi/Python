-- 创建数据库
create database python charset=utf8;

-- 使用数据库
use python;

-- 创建students表
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

-- 创建classes表
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);


-- 向students表中插入数据
insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,NULL,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0);

-- 向classes表中插入数据
insert into classes values (0, "python_01期"), (0, "python_02期");





-- 查询
  -- 查询students数据库里面所有表
  select * from students;

  -- 查询students里面的id，name，查询指定的字段
  select id, name from students;

  -- 使用 as 给字段起别名
  select id as 序号, name as 名字, gender as 性别 from students;

  -- 表名.字段名
  select students.id,students.name,students.gender from students;

  -- 可以通过 as 给表起别名
  select s.id,s.name,s.gender from students as s;



  -- 消除重复行
    -- 在select后面列前使用distinct可以消除重复的行
    -- select distinct 列1,... from 表名;
    select distinct gender from students; -- 查询性别



  -- 条件查询

    -- 比较运算符
      -- 等于: =
      -- 大于: >
      -- 大于等于: >=
      -- 小于: <
      -- 小于等于: <=
      -- 不等于: !=

    -- select * from 表名 where 条件;
    select * from students where age>18;


  -- 逻辑运算符
    -- and
    -- or
    -- not

    select * from students where id > 8 and id < 10;

    select * from students where id < 10 or age<25;

    select * from students where not id < 10 or gender<2;
    select * from students where not (id <= 10 or gender<2);



  -- 模糊查询 like
    -- %表示任意多个任意字符
    -- 表示一个任意字符
    -- 查询姓黄的学生
    select * from students where name like '黄%';

    -- 查询姓黄并且“名”是一个字的学生
    select * from students where name like '黄_';
    -- 查询姓黄或叫靖的学生
    select * from students where name like '黄%' or name like '%靖';

    -- rlike 正则
    -- 查询以 周开始的姓名
    select name form students where name rlike "^周.*"


  -- 范围查询
    -- in表示在一个非连续的范围内
      -- 查询编号是1或3或8的名字
      select name,age from students where id in(1,3,8);
                                             not in(1,3,8);

      -- between ... and ...表示在一个连续的范围内
      -- 查询编号为3至8的学生
      select * from students where id between 3 and 8;
                                      not between 3 and 8;

      -- 查询编号是3至8的男生
      select * from students where (id between 3 and 8) and gender=1;

      --

  -- 空判断
    -- 注意：null与''是不同的，判空is null
      -- 查询没有填写身高的学生
      select * from students where height is null;

    -- 判非空is not null
      -- 查询填写了身高的学生
      select * from students where height is not null;

      -- 查询填写了身高的男生
      select * from students where height is not null and gender=1;


  -- 排序
    -- 默认按照列值从小到大排列（asc）
    -- asc从小到大排列，即升序
    -- desc从大到小排序，即降序
      -- 查询年龄在18到34岁之间的男性，按照年龄从小到大排序
      select * from students where where (age between 18 and 34) and gender=1 order by age;

      -- 查询年龄在18到34之间的女性，身高从高到矮排序
      select * from students where age between 18 and 34 and gender=2 order by height desc;
      -- order by 多个字段，如果身高相同，id从大到小排序
      select * from students where age between 18 and 34 and gender=2 order by height desc,id desc;
      -- 如果还一样，按照age从小到大
      select * from students where age between 18 and 34 and gender=2 order by height desc,age asc,id desc;

      -- 按照年龄从小到大，身高从高到矮的排序
      select * from students order by age asc,height desc;


-- 聚合函数
  --统计数据
  -- 总数
    -- 查询学生总数
    select count(*) from students;
    select count(*) as 男性人数 from students where gender=1;

  -- 最大值
    -- 查询女生年龄最大值
    select max(age) from students where gender=2;

  -- 最小值
    -- 查询未删除的学生最小编号
    select min(id) from students where is_delete=0;

  -- 求和
    -- 查询男生的总年龄
    select sum(age) from students where gender=1;

  -- 平均年龄
  select sum(age)/count(*) from students where gender=1;

  -- 四舍五入round(123.23,1)保留1位小数
    --计算所有人平均年龄，保留2位小数
    select round(sun(age)/count(*), 2) from students;

  -- 平均值
    -- 查询未删除女生的年龄平均值
    select avg(age) from students where is_delete=0 and gender=2;

  -- 计算男性的平均身高，保留2位小数
  select round(avg(height), 2) from students where gender=1


-- 分组
  -- group by
    -- 按照性别分组，查询所有的性别
    select gender from students group by gender;

    -- 计算每种性别中的人数
    select gender,count(*) from students group by gender;
                  avg(age) -- 等等等

    -- 计算男性的人数
    select gender,count (*) from students where gender=1 group by gender;


  -- group_concat 查询同种性别中的姓名
    -- 查询同种性别中的姓名
    select gender,group_concat(name,"_",age,"_",id) from students where gender=1 group by gender;

