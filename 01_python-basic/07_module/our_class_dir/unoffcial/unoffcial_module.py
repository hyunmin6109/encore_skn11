import random
from our_class_dir.offcial_module import study, go_lunch, student_count # type: ignore

def study():
    print(f"{student_count}명의 학생들이 열심히 공부를 한다.")

def go_lunch(menus):
    return random.choice(menus)
