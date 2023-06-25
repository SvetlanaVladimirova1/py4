num = int(input("Введите целое число: "))
temp = num
new_num = " "
while temp != 0:
        mod = str (temp % 16)
        if (temp % 16) == 10:
            mod = "a"
        elif (temp % 16) == 11:
            mod = "b"
        elif (temp % 16) == 12:
            mod = "c"
        elif (temp % 16) == 13:
            mod = "d"
        elif (temp % 16) == 14:
            mod = "e"
        elif (temp % 16) == 15:
            mod = "f"
        new_num = mod + new_num
        temp = temp // 16
print( new_num)

h = hex(num)
print(h)
