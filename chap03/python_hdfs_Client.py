# 서버에 접속하겠다라는 뜻.
from hdfs import InsecureClient

# 읽기위한 스트림 연결.
Client = InsecureClient('http://localhost:9870')

# 읽어오기 위한 객체 스트림 생성.
with Client.read('/user/mydata/names.dat', encoding='utf-8') as reader:
	contents = reader.read()

#print(contents)

# 쓰기위한 객체 스트림 생성.
with Client.write('/user/mydata/testw.txt', overwrite=True, encoding='utf-8') as writer:
	writer.write(contents)

print('End of write')
