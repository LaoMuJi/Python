

事物
原子性 要么成功要么失败
一致性 后面的语句失败 也不会损失 因为没有提交
隔离性 当前操作对其他事物不可见
持久性 一旦提交 修改永久保存数据库

开启事物
begin;
或者
start transaction;

