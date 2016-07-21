# SAS入门教程
by sola
>参考书籍：:book:the little sas book :book:sas base（sas certification prep guide:base programming for sas 9)  
推荐书籍：:book:sas advance :book:SAS编程技术教程（朱世武）
:book:SAS编程与数据挖掘商业案例（姚志勇）:book:sas从入门到精通:book:深入解析SAS

**友情提示：SAS自带的文档是最好的帮手，然后是百度谷歌，然后是一个学习群**
## 安装
(略，请自行[百度][])

## 编程规范
*  **<font color='#ff0000'>SAS所有语句都是以`;`分号结尾的</font>**，而且所有的标点符号要求是英文状态下标点符号，中文全角标点符号或漏掉分号都会出现运行出错。*<font color='#ff0000'>引用宏可以省略分号,此种情况后面再说</font>*
* SAS不区分大小写，不需要换行，但是为了代码的可读性，建议每句一行，并采用适当的缩进
* SAS注释：每种编程语言都会有注释，SAS的注释是`/* 注释内容 */` 或` * 注释内容 ;` windows下SAS语言的注释快捷键（ctrl + ？），取消注释快捷键（shift + ctrl + ？）。<font color=#000000 size = 2>*注释是为了后期维护代码，所以注意不要做无意义的注释*</font>

## SAS基础编程

如下是一个SAS示例，可以看出，SAS主要由两部分组成，第一部分为data步，负责数据处理 ，第二部分为proc步，负责数据统计分析。

```sas
data work.test;
  input name $5. age birthday date9. score 3.1;
  format birthday data9.;
  cards;
jack 10 01jan2006 9.2
marry 11 03oct2005 8.4
rose 10 30jun2006 9.0
daisy 9 15sep2007 10
;
run;

proc print;
run;
```
打印结果：

|obs|name|age|birthday|score|
|:--|:---|--:|:-------|----:|
|01 |jack|10 |01jan2006|9.2|
|02 |marry|11|03oct2005|8.4|
|03|rose|10|30jun2006|9.0|
|04|daisy|0|15sep2007|10|

>本例中共有5个变量（variables），即是关系性数据库中的列,  
4个观测（observations），即是关系性数据库中的行


### DATA步

sas可以简单的看成是一种关系型数据库，data步的目的就是建立符合统计分析的数据库。

SAS有三种方法得到数据集:
+ input + cards语句手动输入
+ proc import 或者 infile语句导入外部文件数据
+ 直接从关系性数据库中读取并使用


data步申明语句：  
```
data  逻辑库名.数据集名;
```
>逻辑库（library），可以简单的理解为数据集的物理地址，当然其中不仅仅只有数据集，还有宏、format等；当然,逻辑库在工作中更多的是指定到关系性数据库如mysql,oracal,db,hadoop等.
逻辑库由 libname 指定，后面接逻辑库名称 + 逻辑库路径/网络地址/关系性数据库.
eg： libname test “E:/sasexample”;  
     libname test2 mysql -u root -p 12345;  
     libname test3 excel "E:/excelfile/exceltest1";    

>逻辑库省略的时候，则默认为work逻辑库，当然，可以指定默认逻辑库，此处不讨论；但是不推荐，建议大家养成`逻辑库名.数据集名`的写法习惯.

>>逻辑库、数据集及变量命名规范都差不多，可以使用字母、数字及_(下划线)，数字不能作为开头，不区分大小写，长度限制为32个字节。

然后用Input指明输入变量名,变量输入格式,变量输入方式等信息.

>变量类型  
SAS只有2中数据类型,字符型及数值型,其中日期型是数值型的格式化输出形式,其本质是当前日期与1960年1月1日00:00之差保存的.

#### 直接输入
上述的例子就是一个直接输入的例子,定义数据名,然后通过`Input`关键字定义变量名及输入格式,并且还可以定义数据长度.输入输出格式.标签等内容;然后用`cards`或者`datalines`关键字手动输入数据,然后就可以建立成数据库了.

#### 读取外部文件
一般以txt csv dat等文件常见,

可使用filename {nickname} "{path of the file}";来定义一个文件名;当然也可以在代码内引用.

```
filename testfile 'e:\test\test.txt'
libname testlib 'e:\test'
data testlib.test;
  infile  testfile dsd dlm = ',' misseover truncate;
  input name $10. sex $2. age @@;
run;

```


[百度]: http://baidu.com
