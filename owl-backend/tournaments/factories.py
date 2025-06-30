import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from tournaments.models import Competitor, Debate, Judge, Score, Tournament, UserProfile


class UserProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall('set_password', 'password123')
    rank = factory.Sequence(lambda n: n + 1)


class TournamentFactory(DjangoModelFactory):
    class Meta:
        model = Tournament

    title = factory.Faker("sentence", nb_words=3)
    start_date = factory.LazyFunction(timezone.now)
    end_date = factory.LazyFunction(timezone.now)
    registration_deadline = factory.LazyFunction(timezone.now)
    description = factory.Faker("text")
    location = factory.Faker("city")


class DebateFactory(DjangoModelFactory):
    class Meta:
        model = Debate

    statement = factory.Faker("sentence", nb_words=6)
    start_time = factory.LazyFunction(timezone.now)
    end_time = factory.LazyFunction(timezone.now)
    tournament = factory.SubFactory(TournamentFactory)


class JudgeFactory(DjangoModelFactory):
    class Meta:
        model = Judge

    user = factory.SubFactory(UserProfileFactory)
    debate = factory.SubFactory(DebateFactory)


class CompetitorFactory(DjangoModelFactory):
    class Meta:
        model = Competitor

    user = factory.SubFactory(UserProfileFactory)
    debate = factory.SubFactory(DebateFactory)


class ScoreFactory(DjangoModelFactory):
    class Meta:
        model = Score

    competitor = factory.SubFactory(CompetitorFactory)
    judge = factory.SubFactory(JudgeFactory)
    debate = factory.SelfAttribute("competitor.debate")
    score = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
    feedback = factory.Faker("paragraph")
