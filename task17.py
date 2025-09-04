ball = int(input("balni kiriting(0-100):"))

if 90 <= ball <= 100:
    print("A(a'lo)")
elif 80 <= ball <= 89:
    print("B (yaxshi)")
elif 70 <= ball <=79:
    print("C(qoniqarli)")
elif 60 <= ball <= 69:
    print("D(qoniqarsiz)")
elif 0 <= ball <= 59:
    print(F"(Rad)")
else:
    print("ball 0-100 oraligida bolishi kerak!")