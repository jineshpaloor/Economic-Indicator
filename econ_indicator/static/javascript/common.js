
var getAjax = function(indicator){
    $.ajax({
        url:'/getindicator',
        type: 'GET',
        data:{'indicator': indicator},
        success: function (resp){
            console.log("response  :",resp);
        }
    });
};

$("#CPI").live('click', function(){
    getAjax("cpi");
});

$("#PPI").live('click', function(){
    getAjax("PPI");
});

$("#GDP").live('click', function(){
    getAjax("GDP");
});

