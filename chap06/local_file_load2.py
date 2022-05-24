#! /usr/bin/python3
# findspark import후 초기화
# 빨리 찾기위한 module 있으나 없으나 별 차이가 없다.
import findspark
findspark.init()
from pyspark.sql import SparkSession
#SparkSession 객체 생성 방법. (앱이름을 pyspark-hdfs1라는것으로 임의로 주고 .getOrCreate() 해준>
sparkSession = SparkSession.builder.appName("pyspark-hdfs2").getOrCreate()

# read.load()는 다양한 옵션을 설정할 수 있다
df2 = sparkSession.read.load('/home/jshoon/employee.csv',
# inferSchema='true' :데이터들의 자료형을 자동으로 설정해라 라는뜻. 숫자는 숫자 텍스트는 텍스트
# sep() = 데이터 분리, = split()와 같다 보면된다.
    format='csv', sep=',', inferSchema='true', header='false')
df2 = df2.toDF('id','name','salary','job')
df2.show()
