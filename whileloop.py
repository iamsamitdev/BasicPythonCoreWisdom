for i in range(1, 101):
    if i % 10 == 0:
        print(f"{i:03}") # ขึ้นบรรทัดใหม่
    else:
        print(f"{i:03}", end=" ") # แสดงผลบรรทัดเดียวกัน