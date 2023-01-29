from django.db import models
import datetime
from django.contrib.auth.models import User 

# Create your models here.

CATEGORIES = (
    ('ক্যাম্পাস', 'ক্যাম্পাস'),
    ('হল','হল'),
    ('ক্লাব','ক্লাব'),
    ('স্পোর্টস','স্পোর্টস'),
    ('এলামনাই','এলামনাই'),
    ('ব্লগ','ব্লগ'),
    ('গ্যালারি','গ্যালারি'),
    ('স্পোর্টস','স্পোর্টস'),
    ('অন্যান্য','অন্যান্য'),
)

# Create your models here.
class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='ক্যাম্পাস', null=True)
    title = models.CharField(max_length=400)
    para1 = models.TextField(blank=True)
    para2 = models.TextField(blank=True)
    para3 = models.TextField(blank=True)
    para4 = models.TextField(blank=True)
    para5 = models.TextField(blank=True) 
    para6 = models.TextField(blank=True)
    para7 = models.TextField(blank=True)
    para8 = models.TextField(blank=True)
    para9 = models.TextField(blank=True)
    para10 = models.TextField(blank=True)
    para11 = models.TextField(blank=True)
    para12 = models.TextField(blank=True)
    para13 = models.TextField(blank=True)
    para14 = models.TextField(blank=True)
    para15 = models.TextField(blank=True)
    para16 = models.TextField(blank=True)
    para17 = models.TextField(blank=True)
    para18 = models.TextField(blank=True)
    para19 = models.TextField(blank=True)
    para20 = models.TextField(blank=True)
    para21 = models.TextField(blank=True)
    para22 = models.TextField(blank=True)
    para23 = models.TextField(blank=True)
    para24 = models.TextField(blank=True)
    para25 = models.TextField(blank=True)

    para26 = models.TextField(blank=True)
    para27 = models.TextField(blank=True)
    para28 = models.TextField(blank=True)
    para29 = models.TextField(blank=True)
    para30 = models.TextField(blank=True)
    para31 = models.TextField(blank=True)
    para32 = models.TextField(blank=True)
    para33 = models.TextField(blank=True)
    para34 = models.TextField(blank=True)
    para35 = models.TextField(blank=True)
    para36 = models.TextField(blank=True)
    para37 = models.TextField(blank=True)
    para38 = models.TextField(blank=True)
    para39 = models.TextField(blank=True)
    para40 = models.TextField(blank=True)
    para41 = models.TextField(blank=True)
    para42 = models.TextField(blank=True)
    para43 = models.TextField(blank=True)
    para44 = models.TextField(blank=True)
    para45 = models.TextField(blank=True)
    para46 = models.TextField(blank=True)
    para47 = models.TextField(blank=True)
    para48 = models.TextField(blank=True)
    para49 = models.TextField(blank=True)
    para50 = models.TextField(blank=True)

    para51 = models.TextField(blank=True)
    para52 = models.TextField(blank=True)
    para53 = models.TextField(blank=True)
    para54 = models.TextField(blank=True)
    para55 = models.TextField(blank=True)
    para56 = models.TextField(blank=True)
    para57 = models.TextField(blank=True)
    para58 = models.TextField(blank=True)
    para59 = models.TextField(blank=True)
    para60 = models.TextField(blank=True)
    para61 = models.TextField(blank=True)
    para62 = models.TextField(blank=True)
    para63 = models.TextField(blank=True)
    para64 = models.TextField(blank=True)
    para65 = models.TextField(blank=True)
    para66 = models.TextField(blank=True)
    para67 = models.TextField(blank=True)
    para68 = models.TextField(blank=True)
    para69 = models.TextField(blank=True)
    para70 = models.TextField(blank=True)
    para71 = models.TextField(blank=True)
    para72 = models.TextField(blank=True)
    para73 = models.TextField(blank=True)
    para74 = models.TextField(blank=True)
    para75 = models.TextField(blank=True)

    para76 = models.TextField(blank=True)
    para77 = models.TextField(blank=True)
    para78 = models.TextField(blank=True)
    para79 = models.TextField(blank=True)
    para80 = models.TextField(blank=True)
    para81 = models.TextField(blank=True)
    para82 = models.TextField(blank=True)
    para83 = models.TextField(blank=True)
    para84 = models.TextField(blank=True)
    para85 = models.TextField(blank=True)
    para86 = models.TextField(blank=True)
    para87 = models.TextField(blank=True)
    para88 = models.TextField(blank=True)
    para89 = models.TextField(blank=True)
    para90 = models.TextField(blank=True)
    para91 = models.TextField(blank=True)
    para92 = models.TextField(blank=True)
    para93 = models.TextField(blank=True)
    para94 = models.TextField(blank=True)
    para95 = models.TextField(blank=True)
    para96 = models.TextField(blank=True)
    para97 = models.TextField(blank=True)
    para98 = models.TextField(blank=True)
    para99 = models.TextField(blank=True)
    para100 = models.TextField(blank=True)

    img1 = models.ImageField(upload_to ='static/uploads', blank=True)
    img1caption = models.CharField(max_length=500, blank=True)
    img2 = models.ImageField(upload_to ='static/uploads', blank=True)
    img2caption = models.CharField(max_length=500, blank=True)
    img3 = models.ImageField(upload_to ='static/uploads', blank=True)
    img3caption = models.CharField(max_length=500, blank=True)
    img4 = models.ImageField(upload_to ='static/uploads', blank=True)
    img4caption = models.CharField(max_length=500, blank=True)
    img5 = models.ImageField(upload_to ='static/uploads', blank=True)
    img5caption = models.CharField(max_length=500, blank=True)
    img6 = models.ImageField(upload_to ='static/uploads', blank=True)
    img6caption = models.CharField(max_length=500, blank=True)
    img7 = models.ImageField(upload_to ='static/uploads', blank=True)
    img7caption = models.CharField(max_length=500, blank=True)
    img8 = models.ImageField(upload_to ='static/uploads', blank=True)
    img8caption = models.CharField(max_length=500, blank=True)
    img9 = models.ImageField(upload_to ='static/uploads', blank=True)
    img9caption = models.CharField(max_length=500, blank=True)
    img10 = models.ImageField(upload_to ='static/uploads', blank=True)
    img10caption = models.CharField(max_length=500, blank=True)
    author = models.CharField(max_length=264, default='BUETJS')

    def __str__(self):
        return self.title  

class Gellery(models.Model):
    date = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    image = models.ImageField(upload_to ='static/uploads/gellery', blank=True, null=True)
    caption = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '{} . {} - {}'.format(self.id,self.caption,self.date)


class Contact(models.Model):
    full_name = models.CharField(max_length=128) 
    email = models.EmailField(max_length=256 )
    phone = models.CharField(max_length=20, blank=True, default='')
    comment = models.TextField(max_length=2000)

    def __str__(self):
        return self.email  


class AllComment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE, null=True)
    # commentor_name = models.CharField(max_length=255, blank=True, null=True)
    # commentor_email = models.EmailField(max_length=128, blank=True, null=True)
    comment = models.TextField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Commented by {} on {}'.format(self.user.viewer.name, self.post.title)  


class Viewer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50,null = True)
    profile_pic = models.ImageField(default='static/default.jpeg',null=True, blank = True, upload_to='static/profiles') 
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)  