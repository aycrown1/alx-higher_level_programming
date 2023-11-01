// adds a LI element to UL.my_list when the user clicks the DIV#add_item tag
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
