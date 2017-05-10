from django.forms import ModelForm, ChoiceField, CharField, Form
from reduplications.models import Reduplication, ReduplicationType, ReduplicationCategory
from django.forms import modelformset_factory
from django_select2.forms import Select2MultipleWidget, Select2Widget, ModelSelect2Widget
#from better_filter_widget import BetterFilterWidget

def as_choices(queryset):
	choices = []	
	for rtype in queryset.all():
		choices.append((rtype.pk, rtype.token))
	print choices		
	return tuple(choices)


class ReduplicationSearchForm(Form):
	reduplication = ChoiceField(widget = ModelSelect2Widget(model = Reduplication,search_fields = ['token__icontains']))

class ReduplicationForm(ModelForm):

	class Meta:
		model = Reduplication
		fields = ['category', 'types']
		#exclude = ['_id']		
		widgets = {'types' : Select2MultipleWidget}	
	#types = ChoiceField(choices = as_choices(ReduplicationType.objects),
		#widget = Select2MultipleWidget)

	def __init__(self, *args, **kwargs):
	 	super(ReduplicationForm, self).__init__(*args, **kwargs)
	 	self.fields['category'].required = False
	 	self.fields['types'].required = False

ReduplicationFormSet = modelformset_factory(Reduplication, form=ReduplicationForm)
