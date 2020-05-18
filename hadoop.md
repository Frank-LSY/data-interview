#Hadoop权威指南

##MapReduce
- 任务分为map阶段和reduce阶段
- 以键值对作为输入/输出，需重写map和reduce函数
- MapReduce作业是需要执行的一个工作单元
- 一个作业分为若干任务，包括map和reduce任务，通过yarn调度
- Hadoop将MapReduce输入数据划分为等长的小数据块（分片）
- map任务输出写入本地磁盘，单个reduce任务的输出通常来自于所有mapper的输出，并输出到HDFS块实现可靠存储![一个reduce任务数据流](file:///Users/frank-lsy/Desktop/data-interview/hadoop/hadoop-1.png)![多个reduce任务数据流](file:///Users/frank-lsy/Desktop/data-interview/hadoop/hadoop-2.png)![无reduce任务数据流](file:///Users/frank-lsy/Desktop/data-interview/hadoop/hadoop-3.png)
- combiner函数，属于优化函数，可以帮助减少mapper和reducer之间的数据传输量
- hadoop streaming --- 允许使用非Java语言来写map和reduce函数
- python 可用dumbo替代streaming

##Hadoop分布式文件系统（HDFS）
- HDFS，流式数据访问模式，超大文件。
- 使用抽象块来存储，增大磁盘利用空间，简化存储系统设计，便于备份容错。
- namenode/datanode.
