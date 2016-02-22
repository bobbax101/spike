import time
print('Hello I am Cooper')
time.sleep(2)
print('i will teach you how to science')
time.sleep(2)
print('do you want to science?')
input()
print('thank You For Choosing Cooper Industries')
time.sleep(2)
print('your first lesson will be on...')
time.sleep(2)#time delay
print('*machine crackles and fizzes*')
time.sleep(2)
print('what do you do')
time.sleep(2)
print('run or stay')
choice=str((input('If you run -type r. or if you stay - type s: ')))
if choice is 'r':
    print('you come across a split, you can go down an old passageway and a more modern looking passage')
    choice=str((input('old passage - type o. modern - type m: ')))
    if choice is 'o':
        print('you follow the passage and you come across a set of computers')
        time.sleep(2)
        print('one crackels to life and starts to say hello over and over like it is stuck in a loop')
        time.sleep(0.5)
        print('you hear foot steps behind you')
        time.sleep(2)
        choice=str((input('run - type r stay - type s: ')))
        if choice is 'r':
            print('you run into a wall and die')
        elif choice is 's':
            print('you are grasped by the throat and are being strangled')
            time.sleep(0.5)
            print('you have the choice to fight or call for help')
            choice=str((input('fight - type f call for help - type c: ')))
            if choice is 'f':
                print('you break off and are faceing your aggessor')
                time.sleep(1)
                print('you can see thier face but they seem familiar to you')
                time.sleep(2)
                print('you have no time to think as he comes back at you at lightning speed')
                time.sleep(0.5)
                print('you can run or fight')
                choice=str((input('fight - type f run - type r: ')))
            elif choice is 'c':
                print('you try to call out but you cannot speak and you die a sad death')
                choice=str((input('fight - type f; run - type r: ')))
                if choice is 'r':
                    print('you run into a wall and die')
                elif choice is 'f':
                    print('you trip the man up and he falls into a wall')
                    time.sleep(0.5)
                    print('you see the blood spill and realise he is dead')
                    print('you can look at the body or not')
                    choice=str((input('look - type look not look - type notlook: ')))
                    if choice is 'look':
                        print('you turn over the body to reveal')
                        time.sleep(3)
                        print('yourself')
                        time.sleep(3.5)
                        print('you continue on - slightlty disturbed - and find a small vent and enter it')
                    elif choice is 'notlook':
                        print('you continue on and find a small vent and enter it')
    elif choice is 'm':
        print('you follow the passage and end up in a room filled with typewriters')
        time.sleep(2)
        print('you hear a faint clicking and you inspect the sound')
        time.sleep(2)
        print('you realise that the typewriters are typing on their own')
        time.sleep(2)
        print('you die to the typewriters')
elif choice is 's':
    print('you die of old age')
else:
    print('TYPE CORRECTLY INFERIOR BEING')
    



