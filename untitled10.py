# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/196c2f0Ac4G_rPykZ2ggGfd2KbdXTbaR_
"""

import pandas as pd
baza={
  "FISH" :[  "Eshboyev Ilhom", "Turg'unov Abdulbosit", "Mamadvaliyev Dilshodbek", "Yo'ldashev Husniddin", "Mamataliyev Zikrullo",
           "Tursunov Muhammadqodir","Isaqjanov Muhammadrizo","Muhammadaliyev Abdullo","Muxtorov Nurullo","Nurmuhammadov Muhammadjon"  ],
  "Yoshi" :[ '19', '18', '19',  '19',  '19',  '19',  '20',  '21',  '17',  '19' ] ,
  "Maktabi" :[' 21-maktab',' 18-maktab',' 4-maktab',' 10-maktab',' 6-maktab',' 15-maktab',' 1-maktab',' 9-maktab',' 12-maktab',' 2-maktab'  ],
  "Jinsi" :[ "o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola","o'g'il bola" ],
  "Manzili" :["Paxtachi", "Shahrixon","Turaqo'rg'on","Beshariq","Qo'qon","Shahrixon","Namangan","Chust","Dang'ara","Qo'qon" ],
}
db=pd.DataFrame(baza)
print(db)
filtr=db[db['Yoshi']=="19"]
print(filtr)
filtr=db[(db['Yoshi']=="19") & (db['Manzili']=="Qo'qon")]
print(filtr)