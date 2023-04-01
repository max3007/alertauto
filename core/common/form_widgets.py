from django.forms import ClearableFileInput


class CustomFileInput(ClearableFileInput):
    template_name = "forms/widgets/file_document.html"
    clear_checkbox_label = "Rimuovi Documento"

    def clear_name_id(self, name):
        """
        Given the name of the clear input, return the HTML id for it.
        """
        return 'id_' + name

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        name_id = self.clear_name_id(name)
        context['widget']['id'] = name_id
        return context


class CustomPhotoInput(ClearableFileInput):
    template_name = "forms/widgets/file_image.html"
    clear_checkbox_label = "Rimuovi Foto"

    def clear_name_id(self, name):
        """
        Given the name of the clear input, return the HTML id for it.
        """
        return 'id_' + name

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        name_id = self.clear_name_id(name)
        context['widget']['id'] = name_id
        # context['widget']['attrs'] = attrs

        return context


class CustomCarPhotoInput(ClearableFileInput):
    template_name = "forms/widgets/car_image.html"
    clear_checkbox_label = "Rimuovi Foto"

    def clear_name_id(self, name):
        """
        Given the name of the clear input, return the HTML id for it.
        """
        return 'id_' + name

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        name_id = self.clear_name_id(name)
        context['widget']['id'] = name_id
        # context['widget']['attrs'] = attrs

        return context
