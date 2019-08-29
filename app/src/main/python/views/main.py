from django.views.generic import TemplateView

class ShowHelloWorld(TemplateView):
    template_name='dummy.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)
