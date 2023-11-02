from django.shortcuts import render

from django.http import JsonResponse
# Create your views here.

def receive_url(request):
    if request.method == 'POST':
        # You can access the URL from the request data
        url = request.POST.get('url', '')

        # You can perform any processing on the URL here

        # Return a simple response
        response_data = {'message': 'received'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
