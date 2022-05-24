#! /usr/bin/python3
# findspark import후 초기화
# 빨리 찾기위한 module 있으나 없으나 별 차이가 없다.
import findspark
findspark.init()
from pyspark.sql import SparkSession
#SparkSession 객체 생성 방법. (앱이름을 pyspark-hdfs1라는것으로 임의로 주고 .getOrCreate() 해준>
sparkSession = SparkSession.builder.appName("pyspark-hdfs1").getOrCreate()

#csv를 읽으면, DataFrame(데이터틀:테이블,표)이 된다. 
# df1 = DataFrame(데이터틀:테이블,표)
df1 = sparkSession.read.csv('/home/jshoon/employee.csv')  # csv 내의 헤더가 없는 경우
# .toDF()컬럼명을 추가해준다. 위의 df1과 밑의 df1은 다르다. 컬럼명 있고 없고.
df1 = df1.toDF('id','name','salary','job')        #  컬럼명 추가
df1.show()

# csv 파일에 헤더가 포함된 경우
#df2 = sparkSession.read.csv('emp_with_header.csv', header=True)
#df2.show()

# hdfs 영역으로부터 파일 읽어오기
df = sparkSession.read.csv('hdfs://localhost:9000/user/mydata/employee.csv')
df = df.toDF('id','name','salary','job') 
df.show()

#withColumn(컬럼명을 가지고 작업을 하겠다라는 뜻.)
df = df.withColumn('salary', df.salary+1000)
df.show()
# 저장 후 나오기
