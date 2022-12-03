def CountInList(x,item):
  c=0
  for i in x:
    if i==item:
      c=c+1
  return c
  
x=[1,2,3,4]
print('         '+'Eff'+'        '+'Freq')
for i in x:
  print(str(i)+'         '+str(CountInList(x,i))+'         '+str(CountInList(x,i)/len(x)))