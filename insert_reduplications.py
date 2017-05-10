
from reduplications.models import Reduplication
from django.utils import timezone
def insertAllReduplications(reduplications_file):
	with open(reduplications_file) as f:
		for index, line in enumerate(f):
			components = line.strip().split("\t")
			token = components[0]
			examples = components[1]
			frequency = components[2]
			r = Reduplication(token = token, frequency = frequency, examples = examples, change_date = timezone.now())
			r.save()
			if index % 1000 == 0:
				print "Inserted ", index, " Rows"
			#print token, examples, frequency
