import json


def loads(s, **kwargs):
	"""
	Load a sequence of json objects from a stream
	"""
	decoder = json.JSONDecoder(**kwargs)
	offset = 0
	while offset < len(s):
		obj, count = decoder.raw_decode(s[offset:])
		offset += count
		while offset < len(s) and s[offset].isspace():
			offset += 1
		yield obj
