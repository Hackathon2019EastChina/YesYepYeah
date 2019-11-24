from aliyunsdkcore.client import AcsClient
import base64
import aliyunsdkimagesearch.request.v20190325.AddImageRequest as AddImageRequest
import aliyunsdkimagesearch.request.v20190325.DeleteImageRequest as DeleteImageRequest
import aliyunsdkimagesearch.request.v20190325.SearchImageRequest as SearchImageRequest
from PIL import Image
from pprint import pprint

client = AcsClient("LTAI4FpNkqhh6ffeB5SP6MMq", "aeN5aSI0zh8JJOvcbEgkEXaCl5Xcnq", "cn-shanghai")

def preprocess(imgfileurl):
    image = Image.open(imgfileurl)
    print (image.size)
    factor = max(image.size[0], image.size[1]) / 1024 + 1
    image = image.resize((int(image.size[0] / factor), int(image.size[1] / factor)))
    # print(int(image.size[0] / factor))
    print (image.size)
    image.save("./demo_new.jpg")
# preprocess("./demo.jpg")

# Add Image
# request = AddImageRequest.AddImageRequest()
# request.set_endpoint("imagesearch.cn-shanghai.aliyuncs.com")
# request.set_InstanceName("hackathon")
# request.set_ProductId("test")
# request.set_PicName("test")

# with open('./demo_new.jpg', 'rb') as imgfile:
#     encoded_pic_content = base64.b64encode(imgfile.read())
#     request.set_PicContent(encoded_pic_content)
# response = client.do_action_with_exception(request)
# print(response)

# Search Image
request = SearchImageRequest.SearchImageRequest()
request.set_endpoint("imagesearch.cn-shanghai.aliyuncs.com")
request.set_InstanceName("hackathon")
with open('./demo_new.jpg', 'rb') as imgfile:
    encoded_pic_content = base64.b64encode(imgfile.read())
    request.set_PicContent(encoded_pic_content)
response = client.do_action_with_exception(request)

print(response)