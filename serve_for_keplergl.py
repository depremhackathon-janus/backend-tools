import json
from flask import Flask, make_response, render_template
import requests
import sys, traceback
import os
from flask_cors import CORS

stats = [
  "Guvende",
  "ZorDurumda",
  "GidaIhtiyaci",
  "BezIhtiyaci",
  "CadirIhtiyaci",
  "EnkazAltindayim",
  "KomsumdanSesGeliyor"
]

colors = [
  [0, 255, 0], 
  [255, 0, 0], 
  [255, 255, 0], 
  [0, 0, 255], 
  [255, 255, 255], 
  [255, 0, 255], 
  [0, 255, 255], 
]

app = Flask(__name__)
CORS(app)

def get_point(lat, lon, phone, text, category, colorRGB):
  pnt = {}
  pnt["type"] = "Feature"
  pnt["geometry"] = {}
  pnt["geometry"]["type"] = "Point"
  pnt["geometry"]["coordinates"] = [ lon, lat ]
  pnt["properties"] = {}
  pnt["properties"]["category"] = str(category)
  pnt["properties"]["text"] = str(text)
  pnt["properties"]["phone"] = str(phone)
  pnt["properties"]["fillColor"] = colorRGB
  pnt["properties"]["lat"] = lat
  pnt["properties"]["lon"] = lon
  return pnt

@app.route('/keplergl.json')
def get_keplergl_data():
  global stats, colors
  #print len(stats), len(colors)
  rr = requests.get("http://ebd76af36d58.ngrok.io/users")
  resp = rr.text
  datas = json.loads(resp)
  js = {}
  js["type"] = "FeatureCollection"
  js["features"] = []
  for p in datas:
    #print p
    lat = p["lat"]
    lon = p["long"]
    stat = p["stat"]
    phone = p["num"]
    text = p["txt"]
    stat_id = 0
    while stat != 0:
      #print stat, stat_id
      if (stat & 1) != 0:
        js["features"].append(get_point(lat, lon, phone, text, stats[stat_id], colors[stat_id]))
      stat_id += 1
      stat >>= 1
  r = make_response(json.dumps(js))
  r.mimetype = 'application/json'
  return r

'''
from OpenSSL import SSL
context = SSL.Context(SSL.TLSv1_2_METHOD)
context.use_privatekey_file('/etc/letsencrypt/live/cildir.tk/privkey.pem')
context.use_certificate_chain_file('/etc/letsencrypt/live/cildir.tk/fullchain.pem')
context.use_certificate_file('/etc/letsencrypt/live/cildir.tk/cert.pem')
'''

try:
  context = ('/etc/letsencrypt/live/cildir.tk/fullchain.pem', '/etc/letsencrypt/live/cildir.tk/privkey.pem')#certificate and key files
  app.run(host='0.0.0.0', port=11000, ssl_context=context)
except:
  pass

print "ENDED!"