meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SUS": "Şüpheli bir durumda kullanılır.",
            "SHEESH": "Onaylamamak.",
            "AGGRO": "Agrasifleşmek/sinirlenmek.",
            "ROFL": "Bir şakaya karşılık cevap."
}
word = input("Anlamını öğrenmek istediğin modern kelimeyi gir:")

if word in meme_dict.keys():
    print("Aradığınız kelimenin anlamı",meme_dict[word])
else:
    print("Maalesef aradığın kelime burada yok...")
