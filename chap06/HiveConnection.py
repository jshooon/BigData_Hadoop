#!/usr/bin/env python
# coding: utf-8

# In[18]:


from impala.dbapi import connect
# host는 리눅스 ip주소 입력.
conn = connect(host='192.168.217.128', port=10000, database="userdb", auth_mechanism='PLAIN')
cursor = conn.cursor()
cursor.execute('select * from employee')
#print(cursor.fetchall())
for row in cursor.fetchall():
    num,name,salary,destination = row
    #{:12} = 최대 열두자로 잡아서 표시해라. 이름은 자리를 12자리로 잡으라는 뜻.
    #자리 수 지정.
    print("{}\t{:12}\t{}\t{}".format(num,name,salary,destination))

