# /// script
# requires-python = ">=3.13"
# dependencies = ["factories", "python-dotenv>=1.1.0","django>=5.2","factory-boy>=3.3.3", "faker>=37.1.0"]
# ///
import os
import django
from dotenv import load_dotenv

from ..factories.my_factories import (
    CompetitorFactory,
    DebateFactory,
    JudgeFactory,
    ScoreFactory,
    TournamentFactory,
    UserProfileFactory,
)

load_dotenv(dotenv_path=".env.dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE")) 
django.setup()

def generate_dummy_data():
    # Generate 10 UserProfiles
    print("Generating UserProfiles...")
    user_profiles = [UserProfileFactory.create() for _ in range(10)]
    print(f"Created {len(user_profiles)} UserProfiles")

    # Generate 5 Tournaments
    print("Generating Tournaments...")
    tournaments = [TournamentFactory.create() for _ in range(5)]
    print(f"Created {len(tournaments)} Tournaments")

    # Generate 5 Debates for each Tournament
    print("Generating Debates...")
    debates = []
    for tournament in tournaments:
        for _ in range(3):  # 3 debates per tournament
            debate = DebateFactory.create(tournament=tournament)
            debates.append(debate)
    print(f"Created {len(debates)} Debates")

    # Generate Competitors and Judges for each Debate
    print("Generating Competitors and Judges...")
    for debate in debates:
        # Create 2 Competitors and 1 Judge for each debate
        competitors = [CompetitorFactory.create(debate=debate) for _ in range(2)]
        judges = [JudgeFactory.create(debate=debate) for _ in range(1)]
    
    print(f"Created {len(competitors)} Competitors and {len(judges)} Judges")

    # Generate Scores for Competitors by Judges
    print("Generating Scores...")
    scores = []
    for competitor in competitors:
        # Each competitor gets a score from each judge
        score = ScoreFactory.create(competitor=competitor, judge=judges[0], debate=debate)
        scores.append(score)

    print(f"Created {len(scores)} Scores")

    print("Dummy data generation complete.")

# Run the dummy data generation
if __name__ == "__main__":
    generate_dummy_data()