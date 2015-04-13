import twitter
import json
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'BeUWGW2Gj1kLViWbnfSPfCcmM'
CONSUMER_SECRET = 'PxSSVaXuZC9eLvsa51sh7cAnNjqxGL9CcPibe34rmSRHWzK4RK'
OAUTH_TOKEN = '292159685-ArSMCKenuBQFMuKSSFpYxCxUYq09IpZ8yexLicrl'
OAUTH_TOKEN_SECRET = 'fQllB9QedpkE5z8MCjsTVv34p2TUUYMkB9Wysqhm0YpYR'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

ES_WOE_ID = 23424950


es_trends = twitter_api.trends.place(_id=ES_WOE_ID)

search = 'UCA'
results = twitter_api.search.tweets(q=search, count = 10000, geocode='40,-3,1000km')

j = json.dumps(results, indent=1)
s = json.loads(j)

lista = []
for i in s['statuses']:
	if i['coordinates'] is not None:
		lista.append([i['coordinates']['coordinates'][1] , i['coordinates']['coordinates'][0]]);
print lista

app = Flask(__name__)
GoogleMaps(app)

@app.route("/")
def mapview():
	mymap = Map(
		identifier="view-side",
		lat=40,
		lng=-4,
		zoom=6,
		markers=lista,
		style="height:600px;width:700px;"
	)
	return render_template('template2.html',mymap=mymap)

if __name__ == "__main__":
	app.run(debug=True)
