import pandas as pd
from hdfs import InsecureClient

df = pd.read_csv('mydata.csv', index_col=0)

print('sum')
print(df.sum(axis=0))

# 스트림 연결.
Client = InsecureClient('http://localhost:9870')

# 로컬에서 생성된 DataFrame 객체를 dfs에 csv로 저장하기
with Client.write('/user/mydata/mydata.csv', overwrite=True, encoding='utf-8') as writer:
        df.to_csv(writer)

print('CSV saved')

# dfs에 저장된 csv 파일을 읽어서 DataFrame 객체를 생성하고 통계함수(sum)를 실행한다.
#with Client.read('/user/jshoon/user/mydata.csv') as reader:
#	df2 = pd.read_csv(reader, index_col=0)
#	print(type(df2))
#	df2.sum(axis=0).to_csv('axis0_sum.csv', encoding='utf-8')
#	print('results of sum saved!')
