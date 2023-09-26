from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

import cv2

# Create your views here.
def gen_frames(stream_url, stream_id):
    camera = cv2.VideoCapture(stream_url)
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    yield (b'--frame\r\n'
   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@csrf_exempt
def index(request):
    streams = Stream.objects.all()

    context = {
        'streams': streams,
    }
    return render(request, 'index.html', context)

@csrf_exempt
def video_feed(request, stream_id):
    stream = get_stream(stream_id)
    if stream.name == 'xyz':
        stream_url = f"rtsp://amadeus:4510471@192.168.219.104:554/stream1"

        