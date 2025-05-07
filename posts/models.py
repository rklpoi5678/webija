from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):  # 유저프로필사진 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    author_profile_pic = models.ImageField('profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username  # 이 부분을 수정했습니다.

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()  # 이 부분을 수정했습니다.
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
            
class Tag(models.Model):  # 태그 다대다관계
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):  # 게시물
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    views = models.IntegerField(default=0) # 조회수
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):  # 댓글
    content = models.TextField()  # 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    target_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.content[:20]}'

class Category(models.Model):  # 카테고리
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Like(models.Model):  # 좋아요
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='post_likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='comment_likes')

    def __str__(self):
        target = self.post if self.post else self.comment
        return f'Like by {self.user.username} on {target}'
