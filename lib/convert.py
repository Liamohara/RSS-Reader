from re import sub, findall
import untangle
from dateutil.parser import parse


def run(text):
    text = text.replace("<updated>", "<pubDate>").replace(
        "</updated>", "</pubDate>")
    text = text.replace("<description>", "<summary>").replace(
        "</description>", "</summary>")
    text = text.replace("<link>", '<link href="').replace("</link>", '"/>')
    text = text.replace('<link', '<link/><link')

    parsed = untangle.parse(text)

    try:
        posts = parsed.feed.entry
    except:
        posts = parsed.rss.channel.item

    converted = []

    for post in posts:
        converted.append({
            'img': findall(r'<img.*?src="(.*?)"', post.summary.cdata)[0],
            'title': post.title.cdata,
            'date': parse(post.pubDate.cdata).strftime('%d, %b %Y'),
            'body': sub(r"(<a.*?<\/a>)|(<.*?>)", "", post.summary.cdata),
            'link': post.link[1]['href']
        })

    return converted
