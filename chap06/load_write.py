#! /usr/bin/python3
# 방법 1
# write.csv 방법
# findspark import후 초기화
# 빨리 찾기위한 module 있으나 없으나 별 차이가 없다.
import findspark
findspark.init()
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("pyspark-hdfs3").getOrCreate()

df1 = sparkSession.read.csv('hdfs://localhost:9000/user/mydata/employee.csv',
        inferSchema=True, header=False) 
df1.show()

df2 = df1.toDF('id','name','salary','job')
df2 = df2.withColumn('salary', df2.salary+5000)
df2.show()
df2.write.csv('/home/jshoon/pyspark_test/employee_increase.csv', mode='overwrite', header=True)

df3 = sparkSession.read.csv('/home/jshoon/pyspark_test/employee_increase.csv', header=True)
df3.show()
