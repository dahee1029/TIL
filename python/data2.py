#items실습
#미션1.점수가 80점 이상, 이름이 대문자인 새 딕셔너리 생성
student_scores={
    "alice":85,
    "bob":92,
    "charlie":78,
    "david":95,
    "eva":88,
}
high_scores={name.upper() : score for name,score in student_scores.items() if score>=80}
print(high_scores) #{'ALICE': 85, 'BOB': 92, 'DAVID': 95, 'EVA': 88}

#미션2
#new_dict의 결과가 {'A':3,'B':3,'0':3,'AB':3}
# blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# new_dict={}
# count=0 
# for blood_type in blood_types :
#     if blood_type in new_dict:
#         new_dict[blood_type]+=1
#     else:
#         new_dict[blood_type]=1
# print(new_dict)
#두번째 풀이
# blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# new_dict={}
# for blood_type in blood_types :
#     new_dict[blood_type]=new_dict.get(blood_type,0)+1
# print(new_dict)
from collections import Counter
blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
new_dict=Counter(blood_types)
print(new_dict)