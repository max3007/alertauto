// custom input file 
(function (global) {

    var imagesPerRow = 3,
        columns,
        previews,
        error;

    function windowLoadHandler() {
        global.removeEventListener("load", windowLoadHandler);
        chooseFiles = document.querySelector('[custom-input-file]');
        maxSize = chooseFiles.getAttribute('max_file_size');
        console.log(maxSize)
        error = document.getElementById("error");

        table = document.getElementById("previewTable");
        columns = document.getElementById("columns");
        previews = document.getElementById("previews");

        var row = columns.insertRow(),
            header,
            i;

        for (i = 0; i < imagesPerRow; i += 1) {
            header = row.insertCell();
            header.style.width = (100 / imagesPerRow) + "%";
        }

        chooseFiles.addEventListener("change", PreviewImages, false);
    }

    function PreviewImages() {
        if (chooseFiles.files.length > 0) {
            const size = (chooseFiles.files[0].size / 1024 / 1024).toFixed(2);
            error.innerHTML = ""
            if (size > maxSize && maxSize !== null) {
                $("#previewTable tr").remove();
                error.innerHTML = '<b class"text-danger ms-2"> File di: ' + size + ' MB' + ' troppo grande, max ' + maxSize + ' MB' + '</b>';

            } else {
                $("#previewTable tr").remove();
                var row;
                console.log(chooseFiles.files)

                Array.prototype.forEach.call(chooseFiles.files, function (file, index) {
                    var cindex = index % imagesPerRow,
                        oFReader = new FileReader(),
                        cell,
                        image;

                    if (cindex === 0) {
                        row = previews.insertRow(Math.ceil(index / imagesPerRow));
                    }
                    spinner = document.getElementById("spinner")
                    console.log(spinner)
                    image = document.createElement("img");
                    image.id = "img_" + index;
                    image.style.height = "150px";
                    image.classList.add("rounded", "border", "shadow", "ms-2", "mb-2");
                    spinner.classList.remove("visually-hidden");
                    setTimeout(() => {
                        cell = row.insertCell(cindex);
                        //cell.innerHTML = '<b class"text-danger"">Nuova</b>';
                        cell.appendChild(image);
                        oFReader.addEventListener("load", function (evt) {
                            console.log("loaded");
                            image.src = evt.target.result;
                            this.removeEventListener("load", windowLoadHandler);
                        }, false);
                        oFReader.readAsDataURL(file);
                        spinner.classList.add("visually-hidden");
                    }, "500")

                });

            }
        } else {
            $("#previewTable tr").remove();
        }
    }

    global.addEventListener("load", windowLoadHandler, false);
}(window));
