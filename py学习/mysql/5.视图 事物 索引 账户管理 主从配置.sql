创建视图
create view 视图名称 as select 语句;

查看视图 多个虚拟的表 只能查
show tables;

删除视图
drop view 视图名称;





事物
原子性 要么成功要么失败
一致性 后面的语句失败 也不会损失 因为没有提交
隔离性 当前操作对其他事物不可见
持久性 一旦提交 修改永久保存数据库

开启事物
begin;
或者
start transaction;





建立索引
在表名的 字段 建立索引 10是长度 创建表字段的类型参数varchar或者char才填写
create index 表名 on 表名(字段(10))

查看索引
show index from 表名;

删除索引
drop index 索引名称 on 表名






账户管理
使用user表
desc user;

查看用户
select user,host,authentication_string from user;

创建账户
grant 权限名称 on 数据库 to '用户名'@'访问主机' identified by '密码';

grant select on 表.* to 'liu'@'localhost' identified by '123456';
-- 查询权限select
-- 全部权限all privileges
-- 本地localhost 远程%

修改密码
update user set authentication_string=password('新密码') where user='用户名';

删除帐号root
drop user '用户名'@'主机';

远程连接
注释 vim /etc/mysql/mysql.conf.d/mysqld.cnf里面的bind-addr = 127.0.0.1
mysql -uXXX -pXXX -h192.168.*.* -p3306

刷新权限
flush privileges





主从配置


备份数据库
mysqldump -uroot -p 数据库名 > xxx.sql;

恢复数据库
创建一个新的数据库
mysql -uroot -p 新数据库名 < python.sql

在ubuntu上执行备份
mysqldump -uroot -pmysql --all-databases --lock-all-tables > ~/master_db.sql

还原
mysql -uroot -pmysql < master_db.sql





配置主服务器
打开 sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
去除#  server-id =1 和从服务器不能一样
       log...
重启服务器
sudo service mysql restart

从服务器84行不用开 ID和主服务器不能一样

登入主服务器
mysql -uroot -pmysql
GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' identified by 'slave'; --创建一个slave用户内网登录，密码slave

刷新权限
FLUSH PRIVILEGES;

获取主服务器的二进制日志信息
SHOW MASTER STATUS;

进入从服务器输入
change master to master_host='主服务器IP', master_user='slave', master_password='slave',master_log_file='mysql-bin.000006', master_log_pos=590;

检查 从服务器输入  slave_IO_Running:YES下面的也是YES 表示成功
show slave status \G;