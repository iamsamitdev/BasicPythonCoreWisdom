i = 1

while i <= 100:
    if i % 10 == 0:
        print(f"{i:03}") # ขึ้นบรรทัดใหม่
    else:
        print(f"{i:03}", end=" ") # แสดงผลบรรทัดเดียวกัน
    i = i + 1