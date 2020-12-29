import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

from mainsite.models import Branch

data_title = list()
data_name = list()
with open("allstores.txt", "r", encoding="utf-8") as fp:
	txtfile = fp.readlines()
for d in txtfile:
	title, name = d.split(",")
	data_title.append(title)
	data_name.append(name.strip())
for i in range(len(data_title)):
	t = Branch(title=data_title[i], name=data_name[i])
	t.save()
print("Done")