{"filter":false,"title":"settings.py","tooltip":"/Nickauction/settings.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "],"id":295}],[{"start":{"row":91,"column":0},"end":{"row":92,"column":0},"action":"insert","lines":["",""],"id":296}],[{"start":{"row":92,"column":0},"end":{"row":95,"column":57},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")"],"id":297}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":80},"action":"remove","lines":["DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }"],"id":298}],[{"start":{"row":93,"column":4},"end":{"row":93,"column":82},"action":"remove","lines":["DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"],"id":299},{"start":{"row":93,"column":4},"end":{"row":93,"column":84},"action":"insert","lines":["DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }"]}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "],"id":300}],[{"start":{"row":85,"column":0},"end":{"row":90,"column":3},"action":"remove","lines":["# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }"],"id":301}],[{"start":{"row":84,"column":0},"end":{"row":85,"column":0},"action":"remove","lines":["",""],"id":302}],[{"start":{"row":90,"column":4},"end":{"row":95,"column":3},"action":"insert","lines":["# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }"],"id":303}],[{"start":{"row":90,"column":4},"end":{"row":90,"column":6},"action":"remove","lines":["# "],"id":304},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"remove","lines":["# "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":2},"action":"remove","lines":["# "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":2},"action":"remove","lines":["# "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"remove","lines":["# "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "],"id":305},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":96,"column":0},"end":{"row":96,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":12,"state":"start","mode":"ace/mode/python"}},"timestamp":1565729686355,"hash":"ceda02e1693f8cbbacac97baf1b462867fd5781b"}