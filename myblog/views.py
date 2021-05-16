from django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import (
    get_seven_days_read_data,
    get_today_hot_data,
    get_yesterday_hot_data,
    get_7_days_hot_data
)
from blog.models import Blog


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    context = {}
    context["dates"] = dates
    context["read_nums"] = read_nums
    context["today_hot_data"] = get_today_hot_data(blog_content_type)
    context["yesterday_hot_data"] = get_yesterday_hot_data(blog_content_type)
    context["hot_data_for_7_days"] = get_7_days_hot_data(blog_content_type)
    return render_to_response("home.html", context)
