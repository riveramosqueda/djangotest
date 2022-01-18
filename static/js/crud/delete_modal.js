$(document).ready(()=>{
  $('a.btn.btn-sm.btn-danger').click((e)=>{
    let delete_url=$('#delete_modal form').attr('action');
    let delete_id=$(e.target).data('delete_id')?($(e.target).data('delete_id')):(0);
    
    delete_url=delete_url.replace(/\d+$/,delete_id);
    $('#delete_modal form').attr('action',delete_url);

    $('#delete_modal #delete_id').val();
    $('#delete_modal').modal('toggle');
  });

  $('#delete_modal [data-dismiss="modal"]').click(()=>{
    $('#delete_modal').modal('hide');
  });
});