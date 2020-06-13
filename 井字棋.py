broad={'11':' ','12':' ','13':' ',
       '21':' ','22':' ','23':' ',
       '31':' ','32':' ','33':' '}
human={'A':'*','B':'O'}
win=[['11','12','13'],['21','22','23'],['31','32','33'],['11','22','33'],['11','21','31'],
     ['12','22','32'],['13','23','33'],['13','22','31']]
a=1
def printbroad(broad):
       print(broad['11']+'|'+broad['12']+'|'+broad['13'])
       print('-+-+-')
       print(broad['21'] + '|' + broad['22'] + '|' + broad['23'])
       print('-+-+-')
       print(broad['31'] + '|' + broad['32'] + '|' + broad['33'])
def enternumber(broad,man):
       print('turn for '+str(man))
       print('输入棋子放置行数:',end='')
       i=input()
       print('输入棋子放置列数:',end='')
       j=input()
       if judgerepeat(broad,i,j)==0:
              broad[str(i)+str(j)]=human[man]
              printbroad(broad)
              if(judgewinner(broad)!=0):
                     print('游戏结束!  '+str(man)+'获胜!')
                     global a
                     a=0

       else:
              print('该位置已经有棋子!')
              enternumber(broad,man)
def judgerepeat(broad,i,j):
       if(broad[str(i)+str(j)]!=' '):
              return 1
       else:
              return 0
def judgewinner(broad):
       for i in win:
              if(broad[i[0]]==broad[i[1]] and broad[i[1]]==broad[i[2]] and broad[i[0]]!=' '):
                     return 1
       return 0

while(a):
       enternumber(broad,'A')
       if(a==1):
              enternumber(broad,'B')
       else:
              break




