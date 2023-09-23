from django.shortcuts import render
from django.http import HttpResponse

import datetime
# Create your views here.

def current_datetime(request):
    offset = datetime.timedelta(hours=3)
    now = datetime.datetime.now()+offset
    html = f"""
    <html>
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-gradient-to-r from-teal-200 to-teal-500">
            <h1 class="text-4xl font-bold text-center text-gray-800 mb-4">Hello from Django and Docker</h1>
            <h2 class="text-2xl font-bold text-center text-gray-600">It is now {now}.</h2>
        </body>
    </html>"""
    return HttpResponse(html)
