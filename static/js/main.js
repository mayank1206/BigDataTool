$(document).ready(function(){
    //======================DRIVE=========================
    $('body').on('click' , '.folder',function () {
        console.log($(this).attr('value'));
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
                        $("#files").append('<div class="col-sm-1 m-2 p-2 folder" value="'+file_content["pathSuffix"]+'"><i class="fa fa-folder" aria-hidden="true" style="font-size: 50px; color:rgb(95,99,104);"></i><div class="text-truncate">'+file_content["pathSuffix"]+'</div></div>');
                    } else {
                        $("#files").append('<div class="col-sm-1 m-2 p-2" value="'+file_content["pathSuffix"]+'"><i class="fa fa-file-text" aria-hidden="true" style="font-size: 50px; color: rgb(25,103,210);" ></i><div class="text-truncate">'+file_content["pathSuffix"]+'</div></div>');
                    }
                }
            }
        });
    });

    $('body').on('click' , '.back_folder',function () {
        console.log($(this).attr('value'));
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
                        $("#files").append('<div class="col-sm-1 m-2 p-2 folder" value="'+file_content["pathSuffix"]+'"><i class="fa fa-folder" aria-hidden="true" style="font-size: 50px; color:rgb(95,99,104);"></i><div class="text-truncate">'+file_content["pathSuffix"]+'</div></div>');
                    } else {
                        $("#files").append('<div class="col-sm-1 m-2 p-2" value="'+file_content["pathSuffix"]+'"><i class="fa fa-file-text" aria-hidden="true" style="font-size: 50px; color: rgb(25,103,210);" ></i><div class="text-truncate">'+file_content["pathSuffix"]+'</div></div>');
                    }
                    // text += person[x];
                }
            }
        });
    });


});