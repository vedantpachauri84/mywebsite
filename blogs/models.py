from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Post(models.Model):
    title = models.CharField(max_length=100)
    intro = models.TextField()
    summary = models.TextField()
    date = models.DateTimeField(auto_now_add=False)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    image=models.ImageField()
    def __str__(self):
        return f'{self.title}'
    def __str__(self):
        return f'{self.title}'
class Comment(models.Model):
    username=models.CharField(max_length=30)
    useremail=models.EmailField()
    text=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    def __str__(self):
        return f'BY {self.username} on post {self.post.title}'