from haystack import indexes
from account.models import Pmodel

class ModelIndex (indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True, template_name="search/pmodel.txt")
	first_name=indexes.CharField(model_attr='first_name')
	last_name=indexes.CharField(model_attr='last_name')

	def prepare_name(self, obj):
		return [ first_name ]

	def get_model(self):
		return Pmodel

	def index_queryset(self, using=None):
		return self.get_model().objects.all()