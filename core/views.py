from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.status import status

# Create your views here.
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializar = PostSerializer(post ,many=True)
        return JsonResponse(serializar.data, safe = False)
    if request.method == 'POST':
        serializar = PostSerializer(data = request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data ) #status=status.HTTP_201_CREATED