from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs')
    contents = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    viewcount = models.PositiveIntegerField(default=0)

    def __str__(self):

        # to return the title of blog page(for return date,do,self.date)
        return self.title + "(" + self.author + ")" + str(self.date) + str(self.id)


class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events')
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Catagory(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='catagory')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    # catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)  #Catagory helps to create a relations with the above Catagory class(for many to one)
    # Catagory helps to create a relations with the above Catagory class(for many to many relatiosn)
    catagory = models.ManyToManyField(Catagory)
    image = models.ImageField(upload_to='news')
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    # null and blank are succesively
    email = models.EmailField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commenter
