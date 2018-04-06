def standingInTheQueue(heights,directions):
  sums=[]
  
  for i in heights:
    count=0
    for j in heights:
      if(i>j):
        count+=1
      else:
        sums.append(count)
        break
  print("standingInTheQueue(heights,directions)=",sum(sums))
h=[178, 180, 170, 190]
d = "LLLL"
standingInTheQueue(h,d)
