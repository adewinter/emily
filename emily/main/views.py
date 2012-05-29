from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from emily.main.forms import ImageUploadForm
from emily.main.models import UploadedImage


def home(request):
    context = {}
    return render_to_response("main/base.html", context, context_instance=RequestContext(request))

def handle_uploaded_image(file):
    iu = UploadedImage()
    iu.file = file
#    name = file.name
    iu.save()
    return '<img src="%s" />' % iu.file.url

@csrf_exempt
def upload_file(request):
    """

    """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resp = handle_uploaded_image(request.FILES['file'])
            return HttpResponse(resp)
    else:
        form = ImageUploadForm()
    c = {'form': form}
    return render_to_response('main/upload.html', c)