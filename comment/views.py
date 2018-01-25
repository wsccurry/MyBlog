from django.shortcuts import render
from comment.models import Comment
# Create your views here.

def show_comment(id):
    comments=Comment.objects.filter(titleId=id)
    return comments