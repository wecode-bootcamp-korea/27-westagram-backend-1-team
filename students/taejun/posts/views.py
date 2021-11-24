import json, requests

import jwt
from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.db.models       import F

from my_settings            import SECRET_KEY, ALGORITHM
from posts.models           import Post, Comment, Like
from core.utils             import authorization, Validation

class PostView(View):
    @authorization
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        try:
            desc  = data['desc']
            image = data['image']

            Validation.image_validation(image)

            post       = Post()
            post.user  = user
            post.desc  = desc
            post.image = image

            post.full_clean()
            post.save()

        except TypeError:
            return JsonResponse({'message': 'IMAGE_URL_REQUIRED'}, status=400)

        except requests.RequestException:
            return JsonResponse({'message': 'INVALID_IMAGE_URL'}, status=400)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except ValidationError:
            return JsonResponse({'message': 'INVALID_DESC'}, status=400)

        return JsonResponse({'message': 'POSTED'}, status=200)

    def get(self, request):
        posts = Post.objects.annotate(
            user_name = F('user__name')
        ).prefetch_related('liked_users', 'comment_set')

        results = []

        for post, post_query in zip(
            posts.values('id', 'user_name', 'desc', 'image', 'created_at'), posts
        ):
            post['liked_users'] = list(post_query.liked_users.values('id', 'name'))
            post['comments']    = list(post_query.comment_set.values('user__name', 'content'))

            results.append(post)

        return JsonResponse({'message': results}, status=200)


class CommentView(View):
    @authorization
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        try:
            post_id = data['post_id']
            content = data['content']

            post = Post.objects.get(id=post_id)

            comment         = Comment()
            comment.user    = user
            comment.post    = post
            comment.content = content

            comment.full_clean()
            comment.save()

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except Post.DoesNotExist:
            return JsonResponse({'message': 'INVALID_POST'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message': 'INVALID_CONTANT'}, status=400)

        return JsonResponse({'message': 'CREATED'}, status=200)

    def get(self, request):
        comments = Comment.objects.filter(post_id=1).values('user__name', 'content', 'is_changed', 'changed_at')

        return JsonResponse({'message': list(comments)}, status=200)


class LikeView(View):
    @authorization
    def post(self, request):
        data = json.loads(request.body)
        user = request.user

        try:
            post_id     = data['post_id']
            post        = Post.objects.prefetch_related('liked_users').get(id=post_id)
            like        = Like.objects.get_or_create(user=user, post=post)

            if not like[1]:
                like[0].delete()
                return JsonResponse({'message': 'CANCELED_LIKE'}, status=200)

            return JsonResponse({'message': 'SUCCESS_LIKE'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'POST_ID_REQUIRED'}, status=400)

        except Post.DoesNotExist:
            return JsonResponse({'message': 'INVALID_POST'}, status=400)

        return JsonResponse({'message': 'SUCCESS'}, status=200)
