from rest_framework import viewsets
from rest_framework import permissions
from polls.models import Period, Position, Candidate, Poll
from .serializers import (
    PeriodSerializer,
    PositionSerializer,
    CandidateSerializer,
    PollSerializer,
)


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = [permissions.AllowAny]


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.AllowAny]


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.AllowAny]


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.AllowAny]
