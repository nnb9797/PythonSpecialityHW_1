from HW_task_2 import AnimalFactory
from HW_task_2 import Bird
from HW_task_3 import Triangle

__all__ = ("AnimalFactory", 'Bird', 'Triangle')

if __name__ == '__main__':
     bird = Bird('Альбатрос', 20, 'черно-белый', 'кра')
     print(f'{bird.name = }, \n{bird.age = }, \n{bird.voice = }, \n{bird.color = }, \n{bird.get_info()}')
     triangle = Triangle(5, 5, 7)
     print(f'{triangle}')
     print(triangle.triangle_check(5, 5, 7))