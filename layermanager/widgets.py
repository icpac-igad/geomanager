from django.forms.widgets import Input


class RasterStyleWidget(Input):
    input_type = "hidden"
    template_name = "widgets/raster_style_widget.html"

    class Media:
        js = ('js/vendor/d3-format.min.js', 'js/colorbrewer.js', 'js/widgets/raster_style_widget.js',)


class IconChooserWidget(Input):
    input_type = "hidden"
    template_name = "layermanager/widgets/icon_chooser.html"

    class Media:
        js = ('js/widgets/icon_chooser.js',)
