#!/usr/bin/python3

# reducer.py
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
	# 데이터가 탭사이로 키와밸류로 넘어오기 때문에 분리하여 저장
    word, count = line.split('\t', 1)  # split('separator', max_split=-1)

    try:
        count = int(count) # 정수로 변환.
    except ValueError:     # 혹시 모를 경우를 대비하여 예외처리.
        # count 가 숫자가 아니면 아래 코드를 실행하지 않고 지나감
        continue

    if current_word == word:            # 동일 단어가 반복될 시
        current_count += count
    else:				# 새로운 단어가 나왔다면, 그전까지의 단어와 카운트 출력
        if current_word:                # 동일 단어가 반복 종료될 시, 지금까지 카운트 출력
            print( '%s\t%s' % (current_word, current_count) )
        current_count = count           # 새로 나온 단어가 시작될 시
        current_word = word		# 다시 단어와 카운트 저장.

# 마지막 단어가 그 전에 나왔던 단어와 같아진다면 출력이 없어지고,
# 새로 나온 경우에도 마찬가지로 출력이 안되기 때문에
if current_word == word:                # 마지막 단어는 위의 루프 안에서 출력하지 못하므로 루프 종료 후 아래에서 출력
    print( '%s\t%s' % (current_word, current_count))
