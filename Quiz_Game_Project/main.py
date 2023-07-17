from question_model import Soru
from data import sorular
from quiz_brain import BilgiYarismasi

soru_havuzu = []
for soru_ogesi in sorular:
    for soru in soru_ogesi["results"]:
        soru_metni = soru["soru"]
        soru_cevabi = soru["dogru_cevap"]
        yeni_soru = Soru(soru_metni, soru_cevabi)
        soru_havuzu.append(yeni_soru)

yarisma = BilgiYarismasi(soru_havuzu)

while yarisma.baskaSoruVarMi(): 
    yarisma.siradakiSoru()

print("Completed the Quiz!")
print(f"Your success rate: {yarisma.skor}/{yarisma.soru_no}")
