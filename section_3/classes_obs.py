lottery_player_dict = {
    'name':'Rolf',
    'numbers':(5,9,12,3,1,21)
}

class LotterPlayer:
    def __init__(self, name):
        self.name = name,
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player_one = LotterPlayer('rolf')
player_two = LotterPlayer('John')


class Student:
    def __init__(self, name, school):
        self.name = name,
        self.school = school,
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    @staticmethod
    def go_to_school():
        print('im going to school')
        # print('im a {}'.format(/))

anna = Student('Anna','MIT')

# anna.marks.append(56)
# anna.marks.append(71)
# print(anna.average())
anna.go_to_school()
