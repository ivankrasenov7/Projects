from django.shortcuts import render
from django.views import generic
from django.http import Http404

from .models import Contacts


class IndexView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'contact_list'
    model = Contacts
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Contacts.objects.filter(contact_title=query)
        else:
            return Contacts.objects.all()


class ContactDetailView(generic.DetailView):

    def get(self, request, *args, **kwargs):
        try:
            contact =  Contacts.objects.get(pk=kwargs['pk'])
        except Contacts.DoesNotExist:
            raise Http404('Този контакт не беше намерен! Опитайте отново!')

        return render(request, 'contact_detail.html', {'contact': contact})