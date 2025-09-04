chipta_narxi = 100_000
yosh = int(input("yoshni kiriting: "))

if 0 <= yosh <= 6:
    chegirma_foizi = 50
elif 7 <= yosh <=17:
    chegirma_foizi = 20
elif yosh > 60:
    chegirma_foizi = 30
else:
    chegirma_foizi = 0


yakuniy_narx = chipta_narxi - chipta_narxi * chegirma_foizi / 100

print(f"yakuniy narx:{yakuniy_narx}som({chegirma_foizi}%chegirma qollaniladi)")
