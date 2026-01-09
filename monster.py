import random
import skill
import sys

class Monster:
    def __init__(self, name, m_type, hp, skill1, skill2,skill3,skill4, lv, exp = 0, exp_to_next=100):
        self.name = name
        self.m_type = m_type
        self.hp = hp
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        self.skill4 = skill4
        self.max_hp = hp
        self.lv = lv
        self.exp = exp
        self.exp_to_next = exp_to_next

    def heal(self, heal):
        if self.hp + heal >=100:
            self.hp = 100
            print(self.name, "hp: {}".format(self.hp))
        else:
            self.hp += heal
            print(self.name, "hp: {}".format(self.hp))

    def gain_exp(self,amount):
        if amount <= 0:
            return

        self.exp += amount
        print(f"[경험치] {self.name} 경험치 +{amount} (현재 {self.exp}/{self.exp_to_next})")

        while self.exp >= self.exp_to_next:
            self.exp -= self.exp_to_next
            self.level_up()

    def level_up(self):
        self.lv += 1
        print(f"[레벨업] {self.name} 레벨이 {self.lv}이(가) 되었습니다! (남은 EXP {self.exp}/{self.exp_to_next})")
#랜덤 몬스터 생성 함수
def random_monster():
    return random.choice(Monsters[0:3])

#몬스터 종류
Monsters = [
    Monster("불꽃숭이", "불", 100, skill.fire(), skill.head(),skill.fire(), skill.head(),5),
    Monster("팽도리", "물", 100, skill.water(), skill.head(),skill.water(), skill.head(),5),
    Monster("모부기", "풀", 100, skill.tree(), skill.head(),skill.tree(), skill.head(),5),
    Monster("펄기아","노멀",150,skill.tree(), skill.fire(),skill.water(), skill.punch(),10),
    Monster("초염몽", "불", 150, skill.fire2(), skill.head(), skill.water(), skill.head(),5),
    Monster("엠페르트", "물", 150, skill.water2(), skill.head(), skill.tree(), skill.head(),5),
    Monster("토대부기", "풀", 150, skill.tree2(), skill.head(), skill.water(), skill.punch(),5),
]