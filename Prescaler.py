print("CPU PULSE 입력 : ")
CPU = int(input())

print("PreScaler 입력 : ")
prescale = int(input())

t = prescale * 65536 / CPU

print(f"원하는 시간 : {t}")
