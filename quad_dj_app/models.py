from django.contrib.auth.models import User
from django.core.validators import MinValueValidator as MinValue, MaxValueValidator as MaxValue
from django.db import models
from django.dispatch import receiver


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    points = models.PositiveIntegerField(default=0)
    games = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "profiles"
        ordering = ("-points", "games")

    def __str__(self):
        return self.user.username


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(models.signals.post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Game(BaseModel):
    player = models.ForeignKey(Profile, on_delete=models.PROTECT)
    time_left_sec = models.PositiveIntegerField(default=0)
    win = models.BooleanField(default=False)

    class Meta:
        db_table = "games"
        ordering = ("-time_left_sec", 'player')

    def __str__(self):
        return self.id


class Word(BaseModel):
    name = models.CharField(max_length=16)
    first_letter = models.CharField(max_length=1)
    last_letter = models.CharField(max_length=1)
    length = models.PositiveIntegerField(validators=[MinValue(3), MaxValue(5)])
    definition = models.TextField()

    class Meta:
        db_table = "words"
        ordering = ("name",)

    def __str__(self):
        return self.name

