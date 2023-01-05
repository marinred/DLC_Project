from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from review.models import Review
from musics.models import Music
from review.serializers import (
    ReviewSerializer,
    ReviewCreateSerializer,
    ReviewMusicSerializer,
)


class ReviewView(APIView):
    def get(self, request, music_id):
        music = Music.objects.get(id=music_id)
        comment = music.review_set.all()
        serializer = ReviewMusicSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, music_id):
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, music_id=music_id, rank=5)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, music_id, review_id):
        review = Review.objects.get(id=review_id)
        if request.user == review.user:
            serializer = ReviewCreateSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, music_id, review_id):
        review = get_object_or_404(Review, id=review_id)
        if request.user == review.user:
            review.delete()
            return Response("삭제가 완료되었습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)
