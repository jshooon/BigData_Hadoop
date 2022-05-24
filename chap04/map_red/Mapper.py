#!/usr/bin/python3

# mapper.py

import sys                         #

for line in sys.stdin:             # 입력스트림 키보드에서 전달한 입력값이 한행한행 line으로 전달 
    line = line.strip()		   # 한행이 넘어오면 좌우 공백 삭제.
    words = line.split()           # 한개의 공백이나 연속된 공백을 한개의 구분자로 간주함(디폴트 값은 공백) 리스트값으로 반환.


# 리스트에서 나온 단어들을 word에 담는다
    for word in words: 
	# 단어에 1이라는 숫자를 매핑한다. (분석,계산하기 위하여)
        print( '%s\t%s' % (word, 1) )     # 단어와 숫자 1을 매핑하여 출력한다
