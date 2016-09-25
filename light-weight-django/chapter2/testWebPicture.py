import io
import urllib.request
from PIL import Image

url = "http://www.nikkansports.com/entertainment/news/img/P2015082303556_miu_takahata-ogp_0.jpg"
imageSource = urllib.request.urlopen(url).read()
print(imageSource)
