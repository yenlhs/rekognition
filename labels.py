import boto3
import image_helpers
from pprint import pprint

client = boto3.client('rekognition')

imgurl = 'https://visitpahrump.com/wp-content/uploads/2015/08/outdoors-v2.jpg'
imgbytes = image_helpers.get_image_from_url(imgurl)
client.detect_labels(Image={'Bytes': imgbytes})

rekresp = client.detect_labels(Image={'Bytes': imgbytes})

pprint(rekresp)


