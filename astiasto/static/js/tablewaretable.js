

$(() => {
  $(document).on('click', '[data-toggle="lightbox"]', function(event) {
                event.preventDefault();
                $(this).ekkoLightbox();
            });



  $('body').on('change', ".num", update);

  function precisionRound(number, precision) {
    var factor = Math.pow(10, precision);
    return Math.round(number * factor) / factor;
  }

  function calculateSum() {
      var sum = 0;
      console.log(sum);
      $(".total-price").each(function() {
        var value = $(this).text().replace('€', '');
        console.log(value);
        if (!isNaN(value) && value.length != 0 && value >= 0 ) {
          sum += parseFloat(value)
        }
      });
      return precisionRound(sum, 2);
  }

  function update() {
    var amount = parseInt($(this).val());
    var net = parseFloat($(this).parent('div').find(".price").attr('value'));
    var tot;
    if (!isNaN(amount) && amount >= 0) {
      var tot = amount * net;
    } else {
      tot = tot;
    }

    $(this).parent('div').find(".total-price").text(precisionRound(tot, 2) + " €");
    $(".bill-total").text(calculateSum() + " €");
  }


});
