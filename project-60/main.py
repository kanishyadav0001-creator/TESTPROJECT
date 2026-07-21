import random

def ludo_dice_experiment():
    dice = ['1', '2', '3', '4', '5', '6']

    result = random.choice(dice)
    
    pro = dice.count('6') / len(dice)
    print("Probability of getting a 6 is:", pro)

    if result == '6':
        return 'The game can be started.'
    else:
        return 'Roll again. Best of luck!'
    
res = ludo_dice_experiment()
print(res)