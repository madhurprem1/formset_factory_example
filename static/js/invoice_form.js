$(document).ready(function () {

//  $('.item-form').hide();


$("form .table .formset").formset({
    deleteText: '<i class="glyphicon glyphicon-trash"></i>',
    deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
    addText: '<i class="glyphicon glyphicon-plus " ></i> Add nugget',
    addCssClass: 'btn btn-success pull-right add-nugget',
    prefix: 'items'
  });

  $("form .table .formset .formset2").formset({
    deleteText: '<i class="glyphicon glyphicon-trash"></i>',
    deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
    addText: '<i class="glyphicon glyphicon-plus"></i> Add text',
    addCssClass: 'btn btn-success pull-right',
    prefix: 'items'

  });

  $('.add-nugget').on('click', function(){
    $("form .table .formset .formset2").formset({
        deleteText: '<i class="glyphicon glyphicon-trash"></i>',
        deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
        addText: '<i class="glyphicon glyphicon-plus"></i> Add text',
        addCssClass: 'btn btn-success pull-right',
        prefix: 'items'

      });
  });


//
//$(".table .formset3").formset({
//    deleteText: '<i class="glyphicon glyphicon-trash"></i>',
//    deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
//    addText: '<i class="glyphicon glyphicon-plus " ></i> Add nugget',
//    addCssClass: 'btn btn-success pull-right add-nugget1',
//    prefix: 'items'
//  });
//
//  $(".table .formset3 .formset4").formset({
//    deleteText: '<i class="glyphicon glyphicon-trash"></i>',
//    deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
//    addText: '<i class="glyphicon glyphicon-plus"></i> Add text',
//    addCssClass: 'btn btn-success pull-right',
//    prefix: 'items'
//  });
//
//  $('.add-nugget1').on('click', function(){
//    $(".table .formset3 .formset4").formset({
//        deleteText: '<i class="glyphicon glyphicon-trash"></i>',
//        deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
//        addText: '<i class="glyphicon glyphicon-plus"></i> Add text',
//        addCssClass: 'btn btn-success pull-right',
//        prefix: 'items'
//      });
//  });

//
//  $('body').on('select', 'textarea[id^=id_items-][id$=-command_output]', function(){
//    $(this).closest('.formset').find('.item-form').show();
//  });

  // $('form div body tr td').formset({
  //   // deleteText: '<i class="glyphicon glyphicon-trash"></i>',
  //   // deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
  //   addText: '<i class="glyphicon glyphicon-plus"></i> Add new item',
  //   addCssClass: 'btn btn-success',
  //   prefix: 'items'
  // });

});