class human:
      
        HP = 10
        MP = 10
    
        def meet(self):
           print("안녕하세요")


class player(human):
         AD = 10
         def attack(self,enemy):
              enemy.HP = enemy.HP - self.AD + enemy.DP
              print("공격")


class npc(human):

    pass

class enemy(human):

    DP = 5
    


while enemy.HP> 0:
    a = int(input('     player와 npc를 만나려면 1\n player가 enemy를 공격하려면 2:'))
    if a==1:
        player.meet(human)
        npc.meet(human)

    if a==2:
        player.attack(player,enemy)
        

  
