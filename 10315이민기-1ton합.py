print("1부터 n까지의 합을 구하는 프로그램")
endp = int(input("n의 값을 입력하시오 : "))
sum = 1;
for i in range(endp-1):
    print (sum,'+',i+2,'=', sum+i+2)
    sum = sum+i+2
    pass
