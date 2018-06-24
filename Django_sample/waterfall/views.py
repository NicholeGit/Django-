from django.shortcuts import render
from django.http import JsonResponse
from waterfall import models


def imgs(req):
    return render(req, "img.html")


def get_imgs(req):
    nid = req.GET.get('nid')
    img_list = models.Img.objects.filter(id__gt=nid).values('id', 'src', 'title')
    # img_list 为querySet对象
    img_list = list(img_list)  #格式化为列表
    ret = {
        'status': True,
        'data': img_list
    }
    return JsonResponse(ret)
    # return JsonResponse([14 22,33],safe=False) 默认只能返回字典，但是加上safe=False 就可以返回列表



