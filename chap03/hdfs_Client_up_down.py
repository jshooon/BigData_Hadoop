from hdfs import InsecureClient

Client = InsecureClient('http://localhost:9870')

# 로컬에있는 파일내용 fds파일에 저장하기.
Client.upload('/user/up.txt', 'BigData/chap03/mem.txt')

# dfs에있는 파일내용 로컬에 저장하기.
#Client.download('/user/jshoon/user/up.txt', 'BigData/chap03/down.txt')

#print(Client.content('/user/jshoon/user/up.txt'))
