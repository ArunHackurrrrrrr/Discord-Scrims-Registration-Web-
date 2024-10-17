from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default="0")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self) :
        return self.product_name


#YAHA PAR JO BHI MODEL BANAOGE USKO ADMIN.PY PAR REGISTER BHI KARNA HOTA HIA SO ITS IMPORTANT 

#YE DEKHO DEFAULT = BLANK IS LIYE KIY HAI BCS YE DATA BASE ALREADY EXIST KAR RAHA THA AND MAINE ISME AUR CHEEZE ADD KI HAI LIKE PRICE CATEGORY SUB CATEGORY SO YE PUCHTA HAI KI JO TUM YE NEW FIELD INTODUCE KAR RAHE HO USKO ADD TO KARDENGE BUT JO FIELDS / PRODUCT PAHLE SE BANE HAI UNME INKI KYA VALUE KAREN LIKE JO GHADI TUMNE BAYA THA US SAMAY TO YE FIELD NAHI THI TO US SAMAY KUCH DALNA HI NAHI THA BUT AAB JO YE NAI FIEWL ADD HUI HAI YE TO SABKE LIYE HUI HAI SO ALREADY EXITSTING PRODUCT ME BHI HONGI SO UNME INKI KYA VALUE RAKHEN {AND AS WE KNOW WHEN WE USE DEAFULT TO JAB KISI OBJECT KI KOI VALUE NAHI HOTI HAI SO YE AUTMATICALLY DEFAULT USE KARTA HAI AS A VALUE}