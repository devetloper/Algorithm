phone_number = {"홍길동":"010-1111-1111", "이순신": "010-1111-2222", "강감찬":"010-1111-3333"}

print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for key in phone_number:
	print(key)

search_name = input("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.")

print(phone_number[search_name])

