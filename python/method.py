#join 메서드
my_list=['my','name','is','dahee']
print(' '.join(my_list)) #my name is dahee
#언패킹 연산자
print(*my_list) #my name is dahee

#append와 extend의 차이
#append를 더 자주 쓰긴 함 / 항목 1개를 추가
#extend는 iterable을 추가



queue=[1,2,3,4,5]
first_element=queue.pop(0)
#위처럼 pop(0)는 알고리즘 문제 풀 때 사용하면 안됨=>popleft사용하기
#->pop(0)는 첫번째 요소를 제거하고, 나머지 요소들을 한칸씩 앞으로 이동
#->시간복잡도가 O(n) ===> 시간 초과 발생
print(queue) #[2, 3, 4, 5]

from collections import deque
queue=deque([1,2,3,4,5])
first_element=queue.popleft()
#====>시간 복잡도가 O(1)



#sort와 sorted의 차이를 알고 구분해서 사용할 줄 알아야 함
#둘 다 오름차순 정렬
#1.sort와 sorted의 차이
#2.내림차순 정렬을 어떻게 할까?
numbers=[3,1,4,1,5,9,2]
numbers.sort(reverse=True) #내림차순 정렬
print(numbers) #[9, 5, 4, 3, 2, 1, 1] =>원본 변경o, 반환값x


numbers2=[3,1,4,1,5,9,2]
sorted_numbers=sorted(numbers2,reverse=True)
print(numbers2) #[3, 1, 4, 1, 5, 9, 2]
print(sorted_numbers) #[9, 5, 4, 3, 2, 1, 1] =>원본 변경x, 반환값o
