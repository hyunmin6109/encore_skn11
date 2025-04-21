# our_class.py 모듈을 가져와서
# 선생님 이름과 학생 수를 출력하고
# study()함수와 lecture()함수를 호출하고
# 먹고 싶은 메뉴명이 5개 담긴 menus리스트를 만들어서
# go_lunch()함수를 호출해 오늘의 점심메뉴를 출력해보자

import our_class

print(our_class.teacher_name, our_class.student_count)

our_class.study()
our_class.lecture()

menus = ["햄버거","초밥", "자장면", "제육", "샌드위치"]
print(our_class.go_lunch(menus))

# from-import 구문 사용
# our_class.py 모듈을 가져와서
from our_class import teacher_name, student_count, study, lecture, go_lunch

# 선생님 이름과 학생 수를 출력하고
print(teacher_name, student_count)

# study() 함수와 lecture() 함수를 호출하고
study()
lecture()

# 먹고싶은 메뉴명이 5개 담긴 meuns 리스트를 만들어서 출력하기
menus = ["햄버거","초밥", "자장면", "제육", "샌드위치"]

# go_lunch()함수를 호풀해 오늘의 점심 메뉴를 출력해 보자!
print(our_class.go_lunch(menus))

#########################################################
# 3. 패키지 내의 모듈 import
import our_class_dir.offcial.offcial_module
from our_class_dir.unoffcial.unoffcial_module import study,go_lunch


# 선생님 이름과 학생 수를 출력하고
print(our_class_dir.offcial.offcial_module.teacher_name)
print(our_class_dir.offcial.offcial_module.student_count)

# study() 함수와 lecture() 함수를 호출하고
study()
lecture()

# 먹고싶은 메뉴명이 5개 담긴 meuns 리스트를 만들어서 출력하기
menus = ["햄버거","초밥", "자장면", "제육", "샌드위치"]

# go_lunch()함수를 호풀해 오늘의 점심 메뉴를 출력해 보자!
print(our_class.go_lunch(menus))

