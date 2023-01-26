ques="What is the capital of India?"
oA="A.Delhi"
oB="B.Mumbai"
oC="C.Chennai"
oD='D.KOLKATA'
print("Welcome to the quiz")
print(ques)
print('-'*10)
print(f'a) {oA}') # f is format
print(f'b) {oB}')
print(f'c) {oC}')
print(f'd) {oD}')
ans=input("enter your answer:")
if ans=="A" or ans=="a":
    print("Sahi jawab✔️")
else:
    print("Galat jawab!😕")