class BilgiYarismasi:

    def __init__(self,s_listesi):
        self.soru_no = 0
        self.skor = 0
        self.soru_listesi = s_listesi


    def baskaSoruVarMi(self):
        return self.soru_no < len(self.soru_listesi)
    
    def siradakiSoru(self):
        guncel_soru = self.soru_listesi[self.soru_no]
        self.soru_no += 1
        oyuncu_cevabi = input(f"{self.soru_no}) {guncel_soru.metin} (True/False): ")
        self.cevapKontrol(oyuncu_cevabi,guncel_soru.cevap)

    def cevapKontrol(self,oyuncu_cevabi,dogru_cevap):
        if oyuncu_cevabi.lower() == dogru_cevap.lower():
            self.skor += 1
            print("Congratulations, correct answer!")
        else:
            print("Sorry, wrong answer!")
            print(f"Correct answer: {dogru_cevap} :( ")
            print(f"Your Current Correct Answer Rate in the Quiz: {self.skor}/{self.soru_no}")
            print("\n") 

        
        

    

        
        