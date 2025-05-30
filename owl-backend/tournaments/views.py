from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Competitor, Debate, Judge, Score, Tournament, UserProfile
from .serializers import DebateSerializer, TournamentSerializer
from django.http import JsonResponse

class IndexView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to TournamentOwl API!",
            "version": "v1",
            "docs_url": "/docs/",
        })

# --- Tournament Views ---
class TournamentListCreateView(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"success": True, "count": queryset.count(), "data": serializer.data}
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "success": True,
                "message": "Tournament created successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class TournamentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"success": True, "data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {
                "success": True,
                "message": "Tournament updated successfully",
                "data": serializer.data,
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"success": True, "message": "Tournament deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


# --- Debate Views ---
class DebateListCreateView(generics.ListCreateAPIView):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"success": True, "count": queryset.count(), "data": serializer.data}
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "success": True,
                "message": "Debate created successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class DebateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"success": True, "data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {
                "success": True,
                "message": "Debate updated successfully",
                "data": serializer.data,
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"success": True, "message": "Debate deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class AddParticipantsToDebateView(APIView):
    def patch(self, request, debate_id):
        try:
            debate = Debate.objects.get(id=debate_id)
        except Debate.DoesNotExist:
            return Response(
                {"success": False, "message": "Debate not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            with transaction.atomic():
                for item in request.data:
                    user_id = item.get("user_id")
                    role = item.get("role")

                    user = UserProfile.objects.get(id=user_id)

                    if role == "judge":
                        Judge.objects.get_or_create(user=user, debate=debate)
                    elif role == "competitor":
                        Competitor.objects.get_or_create(user=user, debate=debate)
                    else:
                        return Response(
                            {"success": False, "message": f"Invalid role: {role}"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

            return Response(
                {"success": True, "message": "Participants added successfully"}
            )

        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
