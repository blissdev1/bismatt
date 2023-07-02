from django.db import models
# Create your models here.


class Maker(models.Model): 
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name 


class Car(models.Model): 
  
  model = models.CharField(max_length=200)
  maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
  cat = models.CharField(max_length=120, blank=True, null=True)
  vin = models.CharField(max_length=200, blank=True, null=True)
  mileage = models.CharField(max_length=200, blank=True, null=True)
  condition = models.TextField(default='good', blank=True, null=True)
  interior_color = models.CharField(max_length=120, blank=True, null=True)
  exterior_color = models.CharField(max_length=120, blank=True, null=True)
  price = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
  img = models.ImageField(upload_to ='./uploaded_img', blank=True, null=True)
  imga = models.ImageField(upload_to ='./uploaded_img', blank=True, null=True)
  imgb = models.ImageField(upload_to ='./uploaded_img', blank=True, null=True)
  imgc = models.ImageField(upload_to ='./uploaded_img',blank=True, null=True)
  imgd = models.ImageField(upload_to ='./uploaded_img',blank=True, null=True)
  transittion = models.CharField(max_length=200, blank=True, null=True)
  horsepower = models.CharField(max_length=200, blank=True, null=True)
  torque = models.CharField(max_length=200, blank=True, null=True)
  date = models.DateField(auto_created=True, blank=True, null=True)

  def serialize(self):
        return {
            "user": self.model,
            "maker": self.maker,
            "cat": self.cat,
            "maker": self.maker,
            "mileage": self.mileage,
            "condition": self.condition,
            "interiot_color": self.interior_color,
            "exterior_color": self.exterior_color,
            "price": self.price,
            "img": self.img,
            "transittion": self.transittion,
            "horsepower": self.horsepower,
            "torque": self.torque,
            "date": self.date.strftime("%a-%d-%b-%Y , %H:%M:%S %p"),
            "img": self.img.url
        }

  
 
 
  
 
 

#class Car(models.Model): 
# model = models.CharField(max_length=200)
#  maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
#  year = models.CharField(max_length=200)
#  mileage = models.CharField(max_length=200, blank=True, null=True)
#  capacity = models.IntegerField(blank=True, null=True)
#  drivetrain = models.CharField(max_length=200, blank=True, null=True)
#  transittion = models.CharField(max_length=200, blank=True, null=True)
#  horsepower = models.CharField(max_length=200, blank=True, null=True)
#  torque = models.CharField(max_length=200, blank=True, null=True)
#  engine = models.CharField(max_length=200, blank=True, null=True)
#  interior_color = models.CharField(max_length=200, blank=True, null=True)
#  exterior_color = models.CharField(max_length=200, blank=True, null=True)
#  img = models.ImageField(upload_to ='./uploads')
    
# upload = models.ImageField(upload_to ='uploads/% Y/% m/% d/')



#class Car(models.Model): 
#  make = models.CharField(max_length=200)
#  model = models.CharField(max_length=200)
#  condition = models.CharField(max_length=400)
#  year = models.CharField(max_length=120)
#  mileage = models.CharField(max_length=120)
#  drivetrain = models.CharField(max_length=120)
#  engine = models.CharField(max_length=120)
#  transittion = models.CharField(max_length=120)
