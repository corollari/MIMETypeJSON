import re, json
text=open("./MimeTypeMap/src/MimeTypes/MimeTypeMap.cs", 'r').read().replace(' ', '')
mimeTypes=dict(re.findall(ur'{".(.+?)","(.+?)"}+?', text))
open("mimeTypes.json", "w+").write(json.dumps(mimeTypes, indent=4))
