from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import ArticleSerializer , CommentSerializer
from webapp.models import Article , Comment

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

class DetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class UpdateView(APIView):
    def put(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        serializer = ArticleSerializer(data=request.data, instance=article)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class DeleteView(APIView):
    def delete(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({'id': pk})

class CommentDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

class CommentUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        serializer = CommentSerializer(data=request.data, instance=comment)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class CommentDeleteView(APIView):
    def delete(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({'id': pk})