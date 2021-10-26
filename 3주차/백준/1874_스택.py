n = int(input())
li = [int(input()) for _ in range(n)]

num = 1
idx = 0
stack_order=[]
stack =[]
answer = True

# 1부터 계속 담기 그러는 도중에 stack이랑 비교해서 print하기
while idx < len(li):
  if stack == []:
    stack_order.append('+')
    stack.append(num)
    num +=1
  else:
    if stack[-1] == li[idx]:
      stack_order.append('-')
      stack.pop()
      idx +=1
    else:
      # 꺼내야 하는 게 스택안에 있는데 그게 가장 바깥쪽이 아닌 경우
      if li[idx] in stack:
        answer =False
        break
      else:
        stack_order.append('+')
        stack.append(num)
        num +=1

if answer:
  for item in stack_order:
    print(item)
else:
  print("NO")





n = int(input())
answer = True
s = []
op = []
count = 1

for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        answer = False
        print("NO")
        break

if answer:
    for i in op:
        print(i)

        # 프린터 안에 for문은 안되구나
        # if answer로 간단하게 출력하는 방법