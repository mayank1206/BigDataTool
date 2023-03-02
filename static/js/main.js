$(document).ready(function(){
    //======================DRIVE=========================
    $('body').on('click' , '.folder',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                button_text: $(this).attr('value'),
                action: "open"
            },
            success:function(response){
                $("#files").empty();
                const files = response.FileStatuses.FileStatus;
                for (file in files) {
                    const file_content = files[file];
                    if (file_content["type"] == 'DIRECTORY') {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2 folder" value="'+file_content["pathSuffix"]+'"><i class="fa fa-folder" aria-hidden="true" style="font-size: 50px; color:rgb(95,99,104);"></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    } else {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2"><i class="fa fa-file-text" aria-hidden="true" style="font-size: 50px; color: rgb(25,103,210);" ></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    }
                }
            }
        });
    });

    $('body').on('click' , '.back_folder',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "back"
            },
            success:function(response){
                $("#files").empty();
                const files = response.FileStatuses.FileStatus;
                for (file in files) {
                    const file_content = files[file];
                    if (file_content["type"] == 'DIRECTORY') {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2 folder" value="'+file_content["pathSuffix"]+'"><i class="fa fa-folder" aria-hidden="true" style="font-size: 50px; color:rgb(95,99,104);"></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    } else {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2"><i class="fa fa-file-text" aria-hidden="true" style="font-size: 50px; color: rgb(25,103,210);" ></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    }
                }
            }
        });
    });

    $('body').on('click' , '.new_folder',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "new_folder",
                dir_name: $('.dir_name').val()
            },
            success:function(response){
                $("#files").empty();
                const files = response.FileStatuses.FileStatus;
                for (file in files) {
                    const file_content = files[file];
                    if (file_content["type"] == 'DIRECTORY') {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2 folder" value="'+file_content["pathSuffix"]+'"><i class="fa fa-folder" aria-hidden="true" style="font-size: 50px; color:rgb(95,99,104);"></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    } else {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2"><i class="fa fa-file-text" aria-hidden="true" style="font-size: 50px; color: rgb(25,103,210);" ></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    }
                }
            }
        });
    });

    $('body').on('click' , '.delete_folder',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "delete_folder",
                dir_name: $('input[name="folderFileName"]:checked').val(),
            },
            success:function(response){
                $("#files").empty();
                const files = response.FileStatuses.FileStatus;
                for (file in files) {
                    const file_content = files[file];
                    if (file_content["type"] == 'DIRECTORY') {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2 folder" value="'+file_content["pathSuffix"]+'"><i class="fa fa-folder" aria-hidden="true" style="font-size: 50px; color:rgb(95,99,104);"></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    } else {
                        $("#files").append('<div class="d-flex flex-column col-sm-1 m-2 p-2"><div class="d-flex" ><input class="form-check-input" type="radio" value="'+file_content["pathSuffix"]+'" name="folderFileName"><div class="col-sm-1 m-2 p-2"><i class="fa fa-file-text" aria-hidden="true" style="font-size: 50px; color: rgb(25,103,210);" ></i></div></div><div class="text-truncate" >'+file_content["pathSuffix"]+'</div></div>');
                    }
                }
            }
        });
    });

    $('body').on('click' , '.copy_current_path',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "copy_current_path",
            },
            success:function(response){
                var copyText = response[0]; 
                navigator.clipboard.writeText(copyText);
                alert("Copied the text: " + copyText);
            }
        });
    });

//======================================CSV===================================================================
    $('body').on('click' , '.delete_csv_schedule',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "delete_csv_schedule",
                csv_schedule_id: $('input[name="inlineRadioOptions"]:checked').val(),
            },
            success:function(response){
                $("#field_table").empty();
                const csv_list = response;
                for (list in csv_list) {
                    const list_content = csv_list[list];
                    $("#field_table").append('<tr id="'+list_content["id"]+'"><td><div class="form-check"><input class="form-check-input" type="radio" name="inlineRadioOptions" value="'+list_content["id"]+'"><label class="form-check-label" for="inlineRadio1"><a href="/hive_edit/'+list_content["id"]+'">'+list_content["text"]+'</a></label></div></td></tr>');
                }
            }
        });
    });

    // $('body').on('click' , '.edit_csv_details',function () {
    //     var value = $('input[name="inlineRadioOptions"]:checked').val();
    //     if(value != null)
    //     {
    //         window.location.href = "edit/"+value;
    //     }
    // });

//===================================common==========================================
    $('body').on('click' , '.submit_hive_pipline',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: $('.hive_type_file').val(),
                id: $('.pipline_id').val()
            },
            success:function(response){
                window.location.href = "/home";
            }
        });
    });

    $('body').on('click' , '.remove_column',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "remove_column",
                column_id: $(this).attr('value'),
                id: $('.pipline_id').val(),
            },
            success:function(response){
                $("#columns").empty();
                const columns = response;
                for (column in columns) {
                    const column_content = columns[column];
                        $("#columns").append('<div class="mb-3"><div class="row g-3 align-items-center"><div class="col-auto me-2"><input type="hiveColumnName" class="form-control" name="hiveColumnName'+column_content["id"]+'" value="'+column_content["column_name"]+'"></div><div class="col-auto"><input type="csvColumnName" class="form-control" name="csvColumnName" value="'+column_content["file_column_name"]+'" readonly></div><div class="col-auto"><button type="remove" class="btn btn-primary remove_column" value="'+column_content["id"]+'">Remove</button></div><div class="col-auto"><button type="update" class="btn btn-primary update_column" value="'+column_content["id"]+'">Update</button></div></div></div>');
                }
            }
        });
    });

    $('body').on('click' , '.update_column',function () {
        var data = "hiveColumnName".concat($(this).attr('value'));
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "update_column",
                column_id: $(this).attr('value'),
                id: $('.pipline_id').val(),
                new_name: $('input[name="'.concat(data).concat('"]')).val(),
            },
            success:function(response){
                $("#columns").empty();
                const columns = response;
                for (column in columns) {
                    const column_content = columns[column];
                        $("#columns").append('<div class="mb-3"><div class="row g-3 align-items-center"><div class="col-auto me-2"><input type="hiveColumnName" class="form-control" name="hiveColumnName'+column_content["id"]+'" value="'+column_content["column_name"]+'"></div><div class="col-auto"><input type="csvColumnName" class="form-control" name="csvColumnName" value="'+column_content["file_column_name"]+'" readonly></div><div class="col-auto"><button type="remove" class="btn btn-primary remove_column" value="'+column_content["id"]+'">Remove</button></div><div class="col-auto"><button type="update" class="btn btn-primary update_column" value="'+column_content["id"]+'">Update</button></div></div></div>');
                }
            }
        });
    });

    //=================PDF==========================
    $('body').on('click' , '.delete_pdf_schedule',function () {
        $.ajax({
            url: '',
            type: 'get',
            data:{
                action: "delete_pdf_schedule",
                pdf_schedule_id: $('input[name="inlineRadioOptions"]:checked').val(),
            },
            success:function(response){
                $("#field_table").empty();
                const pdf_list = response;
                for (list in pdf_list) {
                    const list_content = pdf_list[list];
                    $("#field_table").append('<tr id="'+list_content["id"]+'"><td><div class="form-check"><input class="form-check-input" type="radio" name="inlineRadioOptions" value="'+list_content["id"]+'"><label class="form-check-label" for="inlineRadio1"><a href="/hive_edit/'+list_content["id"]+'">'+list_content["text"]+'</a></label></div></td></tr>');
                }
            }
        });
    });

});