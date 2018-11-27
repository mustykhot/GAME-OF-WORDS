while True:
    print("WELCOME TO THE GAME OF WORDS \n YOU WILL BE TESTED IN TEN DIFFERENT LEVELS \n IF YOU FAIL ONE OF THE LEVELS YOU WILL BE KNOCKED OUT OF THE GAME \n IF YOU'VE GOT THE BALLS ENTER AND PLAY")
    name=input('ENTER YOUR NAME: ')
    word=['saw','was','as',]
    l2=['passive']
    l3=['animate']
    l4=['fledgling']
    l5=['succinct']
    l6=['vituperate']
    l7=['truncate']
    l8=['belligerent']
    l9=['reminisce']
    l10=['grandiose']
    user=(input('form a word from (a,s,w): ' ).strip()).lower()
    score=0
    if user in word:
      print('correct')
      y=score+10
      print('score= ' + str(y))
    
    else:
      score=score
      print('wrong')
      print('score=' + str(score))
      print('GAME OVER')
      print('the correct word is was or saw or as')
      break
    
    print('LEVEL 2')
    d=input('form a word with all the following letters (s,e,p,a,i,v,s): ')
    if d in l2:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is passive')
        break
    
    print('LEVEL 3')
    d=input('form a word with all the following letters (n,i,e,t,a,a,m): ')
    if d in l3:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is animate')
        break
      
    print('LEVEL 4')
    d=input('form a word with all the following letters (d,e,f,l,g,n,g,i,l): ')
    if d in l4:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is fledgling')
        break

    print('LEVEL 5')
    d=input('form a word with all the following letters (u,c,s,c,t,c,i,n,): ')
    if d in l5:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is succinct')
        break 
    

    print('LEVEL 6')
    d=input('form a word with all the following letters (e,t,v,u,t,e,p,i,r,a): ')
    if d in l6:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is vituperate')
        break 

    print('LEVEL 7')
    d=input('form a word with all the following letters (u,t,a,n,r,c,e,t): ')
    if d in l7:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is truncate')
        break 
    print('LEVEL 8')
    d=input('form a word with all the following letters (e,e,e,g,i,n,b,l,l,r,t): ')
    if d in l8:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is belligerent')
        break 
    print('LEVEL 9')
    d=input('form a word with all the following letters (n,m,c,r,e,i,s,i,e): ')
    if d in l9:
      print('correct')
      y=y+10
      print('score= ' + str(y))
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('the correct word is reminisce')
        break
    print('LEVEL 10')
    d=input('form a word with all the following letters (o,e,d,r,a,g,n,i,e): ')
    if d in l10:
      print('correct')
      y=y+10
      print('score= ' + str(y))
      print(name + ' YOU ARE A MASTER OF WORDS')
      break
    
    else:
        y= y
        print('wrong')
        print('score= ' + str(y))
        print('GAME OVER')
        print('YOU REALLY TRIED')
        print('the correct word is grandiose')
        break 
input('press enter to end game')
