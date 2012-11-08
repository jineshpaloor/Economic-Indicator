
$(".econ-indicator").live('click', function(){
    var id = $(this).attr('id');
    var indicator = $("#id_indicator");
    var head = $("#right-col-heading");
    $.ajax({
        url:'/getindicator/',
        type: 'GET',
        data:{'indicator': id},
        success: function (resp){
            $(head).html(resp.short_name+'-'+resp.long_name);
            $(indicator).val(resp.ind_id);
        }
    });
});

