$(document).ready(function() {
    var form = $('#form_buying_product')
    console.log(form)

    form.on('submit', function(event) {
        event.preventDefault()
        console.log('ПОКУПКА:')

        var nmb = Math.abs($('#number').val())
        console.log('Количество: ', nmb, 'шт')

        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data("product_id")
        var product_name = submit_btn.data("name")
        var product_price = submit_btn.data("price")

        var data={}
        data.product_id = product_id
        data.nmb = nmb
            var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val()
            data["csrfmiddlewaretoken"] = csrf_token

            var url = form.attr("action")

        console.log(data);
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cashe: true,
                success: function(data) {
                    console.log('ajax OK');
                    console.log(data.products_total_nmb)
                    if (data.products_total_nmb) {
                        $("#basket_total_nmb").text("("+data.products_total_nmb+")")
                         console.log(data.products)
                         $('.basket-items ul').html("")
                         $.each(data.products, function(k, v) { //key, value
                             $('.basket-items ul').append(
                                 '<li>'+v.name+', '+v.nmb+'шт. '+' по '+v.pricePerItem+' руб '+
                                 '<a href="" class="delete_item">x</a>'+'</li>')

                             $('.basket-items ul').append(
                                 '<li>'+'('+v.nmb+'x) '+v.name+', '+' по '+v.pricePerItem+' руб '+
                                 '<a href="" class="delete_item">x</a>'+'</li>')
                         })
                    }
                },
                error: function() {
                    console.log('ajax ERROR');
                }
            })

        // $('.basket-items ul').append(
        //     '<li>'+product_name+', '+nmb+'шт. '+' по '+product_price+' руб '+
        //     '<a href="" class="delete_item">x</a>'+'</li>')

        console.log('Название товара: ', product_name)
        console.log("id товара: ", product_id)
        console.log("Цена за штуку: ", product_price, "руб.")
        console.log("Общая стоимость: ", product_price*nmb, "руб.");
    })

    function shovingBasket() {
        $('.basket-items').removeClass('hidden')
    }
    $('.basket-container').on('click', function(e) {
        e.preventDefault()
        shovingBasket()
    })
    $('.basket-container').mouseover(function() {
        shovingBasket()
    })
    // $('.basket-container').mouseout(function() {
    //     $('.basket-items').addClass('hidden')
    // })

    $(document).on('click', '.delete_item', function(e) {
        e.preventDefault()
        $(this).closest('li').remove()
    })
})
