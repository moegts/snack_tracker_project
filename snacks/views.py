from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack
