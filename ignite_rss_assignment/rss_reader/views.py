from django.shortcuts import render, get_object_or_404
import feedparser





def feed_view(request):
    post_list = []
    post_obj = {}
    feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed_data = feedparser.parse(feed_url)
    entries = feed_data['entries']
    for entry in entries:
        post_obj = {
        "title" : entry['title'],
        "published" : entry['published'],
        "summary" : entry['summary'],
        "link" : entry['id'],
        "media" : entry['media_thumbnail']
        }
        post_list.append(post_obj)

    context = {"feed_data" : post_list}
    return render(request, "feed.html", context)


