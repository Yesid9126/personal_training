from django import forms


class FileContentPreviewWidget(forms.FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs)
        if value:
            output += "<br>"
            output += f'<a href="{value.url}" target="_blank">View File</a>'
        return output
