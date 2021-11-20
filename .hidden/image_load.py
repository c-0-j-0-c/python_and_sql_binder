import ipywidgets as widgets
from PIL import Image
from sidecar import Sidecar

def load_image(IMG_FILE):
    #read the image
    er = Image.open(IMG_FILE)
    #image size
    w,h = (er.size)
    if h > 300:
        im_height = 300
        im_width = 300/h * (w)

        file = open(IMG_FILE, "rb")
        image = file.read()

        im = Sidecar(title='ER Diagram', anchor='split-bottom')
        im_w = widgets.Image(
                value=image,
                format='png',
                height = im_height,
                width = im_width,
            )


    s = widgets.IntSlider(
        value=im_height,
        min=100,
        max=h,
        step=10,
        description='Zoom +- :',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d'
    )
    mylink = widgets.jslink((s, 'value'), (im_w, 'height'))

    def handle_slider_change(change):
        im_w.height = s.value
        im_w.width = (s.value/h) * w

    s.observe(handle_slider_change, names='value')
    v_b = widgets.VBox([s, im_w], layout=widgets.Layout(height='275px', overflow_y='auto',display='block'))
    with im:
        display(v_b)
        
        
    
