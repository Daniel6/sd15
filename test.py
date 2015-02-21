import urllib2
print urllib2.urlopen("http://api.eve-central.com/api/marketstat?typeid=34&usesystem=30000142&hours=1").read()