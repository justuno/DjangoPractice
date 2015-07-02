/**
 * Created by lvyadong on 15/7/2.
 */

$('#likes').click(function(){
    var catid = $(this).attr('data-catid');
    var username = $(this).attr('data-username');
    $.get('/rango/like_category/', {category_id: catid, likeuser: username}, function(data){
        if(data === 'VOTED'){
            $('#likes').hide();
            var $shit = $('<p>').text = '你已經投過票了！';
            $('#like_status').append($shit);
        }
        else{
            $('#like_count').html(data);
            $('#likes').hide();
        }
    })
});