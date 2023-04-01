var uploaded = {};
var uploadIdFilenames = {};
var uploaded_error = {};
$.fn.filepond.registerPlugin(FilePondPluginImagePreview);
$(function () {
    $('.pond').filepond();
    $('.pond').filepond('allowMultiple', true);
    $('.pond').filepond.setOptions({
        chunkUploads: true,
        chunkSize: 50000,
        server: {
            url: '/fp',
            headers: { 'X-CSRFToken': '{{ csrf_token }}' },
            process: '/process/',
            patch: '/patch/',
            revert: '/revert/',
            fetch: '/fetch/?target=',
            load: '/load/?target='
        },
        onaddfile: function (error, file) {
            console.log('File added: [' + error + ']   file: [' + file.id + ']');
            uploaded[file.id] = file.filename
        },
        onprocessfile: function (error, file) {
            if (error === null) updateButton(true);
        },
        onremovefile: function (error, file) {
            console.log('File removed: [' + error + ']   file: [' + file.id + ']');
            if (file.id in uploaded) delete uploaded[file.id];
            updateButton(false);
        },
        onerror: function (error, file, status) {
            console.log('File error: [' + error + ']   file: [' + file.id + '], status [' + status + ']');
            if (file.id in uploaded) {
                delete uploaded[file.id];
            }
            uploaded_error[file.id] = true;
        }

    });

    $('#filepond-form').on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/submitForm/',
            data: $(this).serialize(),
            success: function (response) {
                if ('status' in response && 'uploads' in response &&
                    response.status == 'OK') {
                    // Remove the uploads that were successfully 
                    // stored from the list.
                    for (var i = 0; i < response.uploads.length; i++) {
                        // Lookup the filepond ID of the successfully
                        // stored upload and remove by filepond ID.
                        // The lookup value we're using uses the serverID
                        // property on the filepond object.
                        var fileList = $('.pond').filepond('getFiles');
                        var fpId = '';
                        for (var j = 0; j < fileList.length; j++) {
                            if (fileList[j].serverId == response.uploads[i]) {
                                fpId = fileList[j].id;
                                break;
                            }
                        }
                        // Before removing the file, store it's name
                        // for use in the uploads table
                        if (fpId !== '') {
                            uploadIdFilenames[response.uploads[i]] = uploaded[fpId];
                            $('.pond').filepond('removeFile', fpId);
                        }
                    }
                    setTimeout(loadStoredUploads(response.uploads));
                }
                else {
                    alert('An error has occurred storing the uploads')
                }
            }
        });
    });

    $('body').on('click', '.del-upload-btn', function (e) {
        var delUploadId = $(e.currentTarget).data('id');
        $.ajax({
            type: 'DELETE',
            url: '/submitForm/?' + $.param({ 'id': delUploadId }),
            success: function (response) {
                if ('status' in response && response.status == 'OK') {
                    $('table.uploads tr[data-upload="' + delUploadId + '"]').remove();
                    if ($('table.uploads tr[data-upload]').length == 0) {
                        // Reset the stored uploads table
                        loadStoredUploads(false);
                    }
                }
                else {
                    alert('An error has occurred deleting the stored upload');
                }
            },
            error: function (jqXHR, status, error) {
                alert('Error deleting stored upload: ' + error);
            }
        });
    });

    function updateButton(state) {
        // If we've been asked to enable the button but there's nothing
        // in the list of uploaded objects, don't enable it.
        if (state && Object.keys(uploaded).length == 0) {
            $('#uploads-submit').attr('disabled', '');
        }
        else {
            if (state) $('#uploads-submit').removeAttr('disabled');
            else $('#uploads-submit').attr('disabled', '');
        }
    }

    function loadStoredUploads(upload_ids) {
        if (!upload_ids) {
            var noUploadsHTML = '<div class="alert alert-primary no-uploads" role="alert" style="width: 100%">' +
                '<b>No stored uploads.</b> There are currently no stored uploads to display.</div>';
            $('#upload-row').html(noUploadsHTML);
            return;
        }
        var tableHeader = '<table class="table table-dark uploads"><thead><tr>' +
            '<th scope="col">Preview</th><th scope="col">Name</th>' +
            '<th scope="col">ID</th><th scope="col"></th>' +
            '</tr></thead><tbody class="upload-rows">';

        var tableRows = '';
        var tableFooter = '</tbody></table>';

        for (var i = 0; i < upload_ids.length; i++) {
            var filename = uploadIdFilenames[upload_ids[i]];
            var img = 'Preview not available';
            if (filename.endsWith('.jpg') || filename.endsWith('.png')) {
                img = '<img src="/fp/load?id=' + upload_ids[i] + '" style="maxWidth: 120px;"/>'
            }
            tableRows += '<tr data-upload="' + upload_ids[i] + '"><td>' + img + '</td><td>' + filename + '</td>' +
                '<td>' + upload_ids[i] + '</td><td><button class="btn btn-sm btn-outline-danger del-upload-btn" data-id="' +
                upload_ids[i] + '">Delete stored upload</button></td></tr>';
        }

        // Populate the content
        if ($('.no-uploads').length == 1) {
            $('.no-uploads').remove()
            $('#upload-row').html(tableHeader + tableRows + tableFooter);
        }
        else {
            $('.upload-rows').append(tableRows);
        }
    }
    loadStoredUploads(false);

});
