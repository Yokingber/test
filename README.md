# 一个用于切割Nginx日志的不成熟的脚本(仅用了一次，所以没有修改)

## useage:
./cut_exsit_log_by_day.py nginx_access_log_file

## 作用：对没有进行按日期切割的Nginx access日志进行切割

切割后在当前目录产生按日期命名文件的access日志，
产生的access日志名称类似于：nginx_access_YYYY_MM_DD.log

## 注意：
切割前的日志文件不要太大(不要超过系统可用内存)，因为要将日志内容赋值给变量
