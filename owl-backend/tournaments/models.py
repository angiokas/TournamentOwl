import uuid
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def three_months_from_now():
    return timezone.now() + timedelta(days=90)


class Tournament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="RandomTournament")
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    registration_deadline = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Debate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    statement = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tournament = models.ForeignKey("Tournament", on_delete=models.CASCADE)

    def __str__(self):
        return f"Debate: {self.statement}"


class UserProfile(User):
    rank = models.IntegerField(unique=True)

    def __str__(self):
        return self.username


class Competitor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "debate")

    def __str__(self):
        return f"Competitor: {self.user} in {self.debate}"


class Judge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "debate")

    def __str__(self):
        return f"Judge: {self.user} in {self.debate}"


class Score(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ("competitor", "judge", "debate")

    def __str__(self):
        return f"Score: {self.score} for {self.competitor} by {self.judge}"
