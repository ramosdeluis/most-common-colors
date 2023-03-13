from django.shortcuts import render


def home_page(request):
    return render(request, 'myapp/index.html')


def upload_image(request):
    global colors
    from colorthief import ColorThief
    if request.method == 'POST':
        user_image = request.FILES['image']
        color_thief = ColorThief(user_image)
        dominant_color = color_thief.get_color(quality=1)
        r = dominant_color[0]
        g = dominant_color[1]
        b = dominant_color[2]
        colors = {'r': r, 'g': g, 'b': b, 'show': True}
    return render(request, 'myapp/index.html', colors)
