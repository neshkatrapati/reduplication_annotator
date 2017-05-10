# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from reduplications.forms import * 
from django.utils import timezone
# Create your views here.
example_limit = 10
import requests
import json
import struct

#def get_line(line_nums):
#    return json.loads(requests.get('http://0.0.0.0:8080/m/'+line_nums).text)


index_file = '/storage/work/research/corpora/hindi/charles.pruned.idx'
source_file = '/storage/work/research/corpora/hindi/charles.pruned'

BYTESIZE = 8
COUNTSIZE = 3
PAGER  = 15
def get_lines(line_numbers):
	lines = []
	with open(index_file,'rb') as i, open(source_file) as s:    
		for line_number in line_numbers:
			lines.append(get_line(s, i, int(line_number)))
		return lines

def get_line(s, i, line_number):
    start = BYTESIZE*COUNTSIZE*(line_number)
    i.seek(start)
    index_line = i.read(BYTESIZE*COUNTSIZE)
    index = struct.unpack('lll', index_line)
    s.seek(index[1])
    return s.read(index[2] - index[1])
        

def process_lines(lines, redup):
	word = redup.split('_')[0]
	new_lines = []
	for line in lines:
		new_lines.append(process_line(line, word))
	return new_lines

def process_line(line, redup):
	words = line.decode('utf-8').strip().split(' ')
	new_words = []
	flag = False
	indices = []
	for index, word in enumerate(words):
		if index + 1 < len(words) and (words[index + 1] == word) and (word == redup):
			#new_words.append("<span class=\"label label-default\">")
			new_words.append("@" + word + "_" + word)
			flag = True
			indices.append(index)
		elif not flag:
			new_words.append(word)
		else:
			flag = False
	#return " ".join(new_words)
	return new_words
			

def index(request, page_id = 0):
	
	lt = int(page_id) * PAGER
	gt = lt + PAGER

	if request.method == "POST":
		formset = ReduplicationFormSet(request.POST)
		status  = formset.is_valid()
		#if formset.is_valid():
		print formset.errors
		for f in formset:
			if 'id' in f.cleaned_data:
				r = f.cleaned_data['id']
				r.category = f.cleaned_data['category']
				r.types = f.cleaned_data['types']
				r.change_date = timezone.now()
				r.save()
		#else:
		

	some_objects = Reduplication.objects.order_by('-frequency')[lt : gt]
	reduplication_examples = []
	for reduplication in some_objects:
		#examples = ";".join(reduplication.examples.split(";")[:example_limit])
		examples = reduplication.examples.split(";")[:example_limit]
		sentences = get_lines(examples)
		sentences = process_lines(sentences, reduplication.token)
		reduplication.example_docs = sentences

		#reduplication_examples.append(examples)
	formset = ReduplicationFormSet(queryset = some_objects)
	searchform = ReduplicationSearchForm()
	return render(request, 'home.html', {'formset' : formset
		, 'searchform' : searchform		
		, 'page_id'  : int(page_id) + 1
		, 'prev_id'  : int(page_id) - 1})


def single_redup(request, redup_id = 0):
	redup = Reduplication.objects.get(pk = redup_id)
	page_id = 1
	print request.GET
	if 'page_id' in request.GET:
		page_id = request.GET['page_id']

	if request.method == "POST":
		form = ReduplicationForm(request.POST)
		status  = form.is_valid()
		redup.category = form.cleaned_data['category']
		redup.types = form.cleaned_data['types']
		redup.change_date = timezone.now()
		redup.save()

	examples = redup.examples.split(";")[:100]
	sentences = get_lines(examples)
	sentences = process_lines(sentences, redup.token)
	redup.example_docs = sentences
	form  = ReduplicationForm(instance=redup) 
	return render(request, 'single.html', {'form' : form, 'redup_id' : redup_id, 'page_id' : int(page_id) - 1})


def search(request):
	if request.method == "POST":
		form = ReduplicationSearchForm(request.POST)
		status = form.is_valid()
		print form.cleaned_data
		r = form.cleaned_data['reduplication']
		print r