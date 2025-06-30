from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import (
    IndexView,
    AddParticipantsToDebateView,
    DebateListCreateView,
    DebateRetrieveUpdateDestroyView,
    TournamentListCreateView,
    TournamentRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Index View
    path('', IndexView.as_view()),

    # Tournament URLs
    path(
        "tournaments/",
        TournamentListCreateView.as_view(),
        name="tournament-list-create",
    ),
    path(
        "tournaments/<uuid:pk>/",
        TournamentRetrieveUpdateDestroyView.as_view(),
        name="tournament-retrieve-update-destroy",
    ),
    # Debate URLs
    path("debates/", DebateListCreateView.as_view(), name="debate-list-create"),
    path(
        "debates/<uuid:pk>/",
        DebateRetrieveUpdateDestroyView.as_view(),
        name="debate-retrieve-update-destroy",
    ),
    path(
        "debates/<uuid:debate_id>/participants/",
        AddParticipantsToDebateView.as_view(),
        name="add_participants",
    ),
    # API Docs URLS
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
