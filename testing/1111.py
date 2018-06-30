# -*- coding:utf-8 -*-
import requests
import urllib3.contrib.pyopenssl

urllib3.contrib.pyopenssl.inject_into_urllib3()

url = "http://epay.ardy0220.top/auth/verify"
data = {"sign":"25c83ec4b6cd2ed0b16e51d82bc0469daeeb48dc658f4341af269ff804dbb05d66c94072ee988d85092d46e1c00d86e3240b19f61ef7b3b268530b80d89330609f267efa6e8ba36b1f2b76684484fcd50ff2d14ed6bfe1d94f685363ecb041b6657f04c6a55283f15ab783b1e0ec1b87e2402b396ca931640457e7a245638528affbc0bc6db4fc50c7c1f8a73eeffb7472b655334042887ceded14cc33fabc68a0ef7e3c01a31f8ee92c6cd42d45b99254d3b77a851290845f29d1f48934bee3dde573c9bedf4f82001720585ec337c0f5ab3f06b1fd7eda28b5435e9045e4a30f97154d8cc68bfc9bb3ef4555e04826b2b96bd6b2f01f625c893187617fea54",
        "data":"2ccdfffce213399a7ed7f828acfb7c55524e87fdae94285075bd113f3582006cb6527d27be00e4197c48ddc80dbcd20d"}

r = requests.post(url,data=data,verify=False)
print (r.status_code)
print (r.text)
print (r.json()['msg'])
try:
        assert r.json()['msg']=="登录成功"
except AssertionError:
        print ("登录失败")