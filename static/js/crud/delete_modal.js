$(document).ready(()=>{
  $('a.btn.btn-sm.btn-danger').click((e)=>{
    $('#delete_modal #delete_id').val($(e.target).data('delete_id')?($(e.target).data('delete_id')):(0));
    $('#delete_modal').modal('toggle');
  });

  $('#delete_modal [data-dismiss="modal"]').click(()=>{
    $('#delete_modal').modal('hide');
  });
});