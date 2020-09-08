# Hadoop权威指南

## MapReduce
- 任务分为map阶段和reduce阶段
- 以键值对作为输入/输出，需重写map和reduce函数
- MapReduce作业是需要执行的一个工作单元
- 一个作业分为若干任务，包括map和reduce任务，通过yarn调度
- Hadoop将MapReduce输入数据划分为等长的小数据块（分片）
- map任务输出写入本地磁盘，单个reduce任务的输出通常来自于所有mapper的输出，并输出到HDFS块实现可靠存储![一个reduce任务数据流](https://github.com/Frank-LSY/data-interview/blob/master/hadoop/hadoop-1.png)![多个reduce任务数据流](https://github.com/Frank-LSY/data-interview/blob/master/hadoop/hadoop-2.png)![无reduce任务数据流](https://github.com/Frank-LSY/data-interview/blob/master/hadoop/hadoop-3.png)
- combiner函数，属于优化函数，可以帮助减少mapper和reducer之间的数据传输量
- hadoop streaming --- 允许使用非Java语言来写map和reduce函数
- python 可用dumbo替代streaming

## Hadoop分布式文件系统（HDFS）
- HDFS，流式数据访问模式，超大文件。
- 使用抽象块来存储，增大磁盘利用空间，简化存储系统设计，便于备份容错。
- namenode/datanode.


# Hadoop Udacity
## 细节
- 启动hadoop前。
	- ① 清除tmp下所有文件
	- ② 清空log文件
	- ③ 格式化Namenode: hadoop namenode -format，注意namenode和datanode的clusterId要匹配
- 配置文件core-site.xml; hdfs-site.xml; mapred-site.xml; yarn-site.xml
- hadoop-streaming.jar位置$HADOOP_HOME/share/tools/hadoop/hadoop-streaming.jar

## HDFS Map Reduce
- 文件存储在HDFS当中
	- 每个文件分成大小一致的文件块，通常是64MB/128MB。
	- 每个块存储在不同的DataNode上面，原始文件的metadata存储在NameNode上面。
	- 如果一个DataNode死掉了，那么就会造成原始文件的部分缺失。如何解决？每一个文件块复制三次，然后放在不同的DataNode之中。
	- 如果NameNode死掉了呢？整个文件都不可访问了。如何解决？① NFS ② 两个NameNode(Active、Standby)。
- Map Reduce 并行化处理
	- MapReduce程序被提交到Job Tracker。
	- Task Tracker运行在各Datanodes上面。
	- 