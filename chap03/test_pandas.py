# 표만드는법
import pandas as pd

data = {
	'A':[20,14,30], #90도로 돌리면 A,B가 컬럼명이 되고 리스트 안의 값들이 컬럼 값이 된다.
	'B':[30,45,20]
	}

# init 메소드가 돌아가면서 객체 생성.
df = pd.DataFrame(data)
#print(df)

#기술통계를 분석할 때에는(통계를 기술한다)
#describe()함수를 사용한다.)
#print(df.describe())

# 테이블 객체가 파일로 저장된다.
#df.to_csv('mydata.csv')


# 파일의 테이블을 읽어서 테이블로 변환한다. 변수에 저장하여 사용하는것이 좋다.
#df2 = pd.read_csv('mydata.csv')
#print(df2)

#CSV파일로 전환할 때, 첫줄의 인덱스도 저장되기 때문에 첫줄은 인덱스라는 것을 
#알려줄 때 속성을 작성한다.
#df2 = pd.read_csv('mydata.csv', index_col=0)
#속성을 작성하면 출력할 때 저장되었던 인덱스 줄이 사라진다.

