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


class Word(BaseModel):  # The words that can be chosen to be guessed
    name = models.CharField(max_length=16)
    l1 = models.CharField(max_length=1)
    l2 = models.CharField(max_length=1)
    l3 = models.CharField(max_length=1)
    l4 = models.CharField(max_length=1)
    l5 = models.CharField(max_length=1)
    # length = models.PositiveIntegerField(validators=[MinValue(3), MaxValue(5)])
    definition = models.TextField()

    class Meta:
        db_table = "words"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Vocab(BaseModel):  # All the words in the vocabulary to be checked against
    name = models.CharField(max_length=16)
    # length = models.PositiveIntegerField(validators=[MinValue(3), MaxValue(5)])

    class Meta:
        db_table = "vocabs"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    points = models.PositiveIntegerField(default=0)
    words_solved = models.ManyToManyField(Word, through='ProfileWords')
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


class ProfileWords(BaseModel):
    word = models.ForeignKey(Word, on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)

    class Meta:
        db_table = "profile_words"
        ordering = ("profile", "word")

    def __str__(self):
        return self.id


class Game(BaseModel):
    player = models.ForeignKey(Profile, on_delete=models.PROTECT)
    time_left_sec = models.PositiveIntegerField(default=0)
    win = models.BooleanField(default=False)

    class Meta:
        db_table = "games"
        ordering = ("-time_left_sec", 'player')

    def __str__(self):
        return self.id
