Hadoop
======

Hadoop Configuration
====================

XML Config files
----------------

core-site.xml

<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
`  `<property>
`    `<name>`fs.default.name`</name>
`    `<value>`hdfs://fuji.cs:24310`</value>
`  `</property>
`  `<property>
`    `<name>`hadoop.tmp.dir`</name>
`    `<value>`/private/var/folders/zz/zzzivhrRnAmviuee+++UUE++662/hadoop`</value>
`    `<description>`IMPORTANT: The top-level directory for all the hadoop logging and mapreduce output. Do not put this on NFS! You must also make sure to create this directory on all computers. See the shell scripts section below. The "/private/var" place I chose was a writable local-disk directory on the SD Hall Mac Lab that, unlike /tmp, does not go away on a reboot.`</description>
`  `</property>
</configuration>

mapred-site.xml

<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
`  `<property>
`    `<name>`mapred.job.tracker`</name>
`    `<value>`fuji.cs:24311`</value>
`    `<description>`The host and port that the MapReduce job tracker runs`
`  at.  If "local", then jobs are run in-process as a single map`
`  and reduce task.`
`  `</description>
`  `</property>
`  `<property>
`    `<name>`mapred.job.tracker.info.port`</name>
`    `<value>`24380`</value>
`  `</property>
`  `<property>
`    `<name>`tasktracker.http.port`</name>
`    `<value>`24300`</value>
`  `</property>
`  `<property>
`    `<name>`mapred.job.tracker.http.address`</name>
`    `<value>`0.0.0.0:24030`</value>
`  `</property>
`  `<property>
`    `<name>`mapred.task.tracker.http.address`</name>
`    `<value>`0.0.0.0:24060`</value>
`  `</property>
`  `<property>
`    `<name>`mapred.child.java.opts`</name>
`    `<value>`-Xmx2000m`</value>
`    `<description>`IMPORTANT: The actual amount of memory to be allowed for the child processes`</description>
`  `</property>
</configuration>

hdfs-site.xml

<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
`  `<property>
`    `<name>`dfs.datanode.address`</name>
`    `<value>`0.0.0.0:24308`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.secondary.http.address`</name>
`    `<value>`0.0.0.0:24490`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.http.address`</name>
`    `<value>`0.0.0.0:24470`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.datanode.http.address`</name>
`    `<value>`0.0.0.0:24504`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.backup.http.address`</name>
`    `<value>`0.0.0.0:24505`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.datanode.ipc.address`</name>
`    `<value>`0.0.0.0:24304`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.backup.address`</name>
`    `<value>`0.0.0.0:24303`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.secondary.info.port`</name>
`    `<value>`24302`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.info.port`</name>
`    `<value>`24301`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.replication`</name>
`    `<value>`1`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.umask`</name>
`    `<value>`007`</value>
`  `</property>
`  `<property>
`    `<name>`dfs.datanode.max.xcievers`</name>
`    `<value>`1000`</value>
`    `<description>`IMPORTANT: Defaults to 256, causes the following exception:`
`2009-11-15 23:03:48,585 ERROR org.apache.hadoop.hdfs.server.datanode.DataNode: DatanodeRegistration(128.32.156.236:50010, storageID=DS-1360695743-128.32.156.236-50010-12583`
`51154995, infoPort=50075, ipcPort=50020):DataXceiver`
`java.io.IOException: xceiverCount 257 exceeds the limit of concurrent xcievers 256`
`        at org.apache.hadoop.hdfs.server.datanode.DataXceiver.run(DataXceiver.java:88)`
`        at java.lang.Thread.run(Thread.java:637)`
`On the DFS node with the error, followed by:`
`Caused by: java.io.IOException: Could not obtain block: blk_1531838615902005301_32624 file=/tmp/hadoop65/tier27/part-00000`
`        at org.apache.hadoop.hdfs.DFSClient$DFSInputStream.chooseDataNode(DFSClient.java:1787)`
`        at org.apache.hadoop.hdfs.DFSClient$DFSInputStream.blockSeekTo(DFSClient.java:1615)`
`        at org.apache.hadoop.hdfs.DFSClient$DFSInputStream.read(DFSClient.java:1742)`
`on the mappers.`
`  `</description>
`  `</property>
</configuration>

hadoop-env.sh

`# Set Hadoop-specific environment variables here.`
`# The only required environment variable is JAVA_HOME.  All others are`
`# optional.  When running a distributed configuration it is best to`
`# set JAVA_HOME in this file, so that it is correctly defined on`
`# remote nodes.`
`ulimit -Hn unlimited`
`ulimit -Sn 10240`
`ulimit -Hn unlimited`
`# The java implementation to use.  Required.`
`export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/1.6.0/Home`
`# Extra Java CLASSPATH elements.  Optional.`
`export HADOOP_CLASSPATH=/home/aa/orgs/gamers/gamers/GamesmanJava/bin:/home/aa/orgs/gamers/gamers/GamesmanJava/lib/xercesImpl.jar`
`# The value for this doesn't really matter--it's not used in the actual Child processes.`
`# The maximum amount of heap to use, in MB. Default is 1000.`
`export HADOOP_HEAPSIZE=1000`

masters

`fuji.cs`

slaves

`fuji.cs`
`akane.cs`
`...`

GamesmanJava/jobs/Connect4\_66\_hadoop.job

`gamesman.game = Connect4`
`gamesman.game.width = 6`
`gamesman.game.height = 6`
`gamesman.game.pieces = 4`
`gamesman.hasher = TieredItergameHasher`
`gamesman.solver = C4IntegratedSolver`
`gamesman.master = HadoopMaster`
`gamesman.database = HadoopSplitDatabase`
`gamesman.db.uri = /tmp/hadoop66`
`record.fields = VALUE:3`
`record.compression = 90`
`gamesman.debug.SOLVER = true`
`gamesman.debug.HADOOP = true`
`gamesman.hadoop.numMappers = 60`
`gamesman.split = 20`
`gamesman.threads = 10`
`gamesman.hadoop.minSplit = 10000`
`gamesman.minSplit = 1000`
`gamesman.maxSplit = 1000000000`
`gamesman.db.compression = gzip`
