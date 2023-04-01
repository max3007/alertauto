import json
import logging
import os

from django.http.response import HttpResponse, HttpResponseBadRequest,\
    HttpResponseNotFound, HttpResponseServerError

from django.views import View
from django.utils.translation import gettext_lazy as _

from django_drf_filepond.api import store_upload, delete_stored_upload
from django_drf_filepond.models import TemporaryUpload, StoredUpload

LOG = logging.getLogger(__name__)


class SubmitFormView(View):

    # Handle POST request
    def post(self, request):
        # Get the post request and extract the IDs of the temporary upload(s)
        # to be permanently stored.
        data = request.POST
        print('data', data)
        try:
            filepond_ids = data.getlist('filepond')
        except KeyError:
            LOG.error('No filepond key found in submitted form.')
            return HttpResponseBadRequest('Missing filepond key in form.')

        if not isinstance(filepond_ids, list):
            LOG.error('Unexpected data type in form.')
            return HttpResponseBadRequest('Unexpected data type in form.')

        # Go through the list of IDs. For each, look up the associated temp
        # upload and call django-drf-filepond's API function store_upload.
        # This stores the file to a local or remote file store depending on
        # how the library is configured.
        stored_uploads = []
        for upload_id in filepond_ids:
            tu = TemporaryUpload.objects.get(upload_id=upload_id)
            LOG.debug('Storing upload: [%s]' % filepond_ids)
            store_upload(upload_id, os.path.join(upload_id, tu.upload_name))
            stored_uploads.append(upload_id)

        # Return the list of uploads that were stored.
        return HttpResponse(json.dumps({'status': 'OK',
                                        'uploads': stored_uploads}),
                            content_type='application/json')

    # Handle request to delete a stored upload
    def delete(self, request):
        # Get the ID of the stored upload to be deleted and look it up in
        # the database.
        upload_id = request.GET.get('id', None)
        try:
            su = StoredUpload.objects.get(upload_id=upload_id)
        except StoredUpload.DoesNotExist:
            return HttpResponseNotFound()

        # If we found the StoredUpload record, call the django-drf-filepond
        # API function delete_stored_upload to delete the record from the
        # database and delete the corresponding file on the local or remote
        # filesystem (delete_file=True).
        try:
            delete_stored_upload(su.upload_id, delete_file=True)
        except Exception as e:
            return HttpResponseServerError(
                json.dumps({'status': 'ERROR', 'errorMsg': str(e)}),
                content_type='application/json')

        return HttpResponse(json.dumps({'status': 'OK', 'deleted': upload_id}),
                            content_type='application/json')


proprieta_manage_foto_view = SubmitFormView.as_view()
