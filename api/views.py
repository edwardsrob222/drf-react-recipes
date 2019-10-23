from rest_framework import generics
from recipes.models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsOwnerORReadOnly

# Create your views here.


class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        #null=True keeps abovefrom giving an error


class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsOwnerORReadOnly,)
