(function ($) {

    $.contactVerification = function(options) {
        var settings = $.extend({
            sendButtonSelector: "#id_code_send_button",
            confirmButtonSelector: "#id_confirm_button",
            onSendSuccess: null,
            onSendFail: null,
            onConfirmSuccess: null,
            onConfirmFail: null,
            countrySelector: "#id_country_number",
            phoneNumberSelector: "#id_phone_number",
            codeSelector: "#id_code"
        }, options );

        var $send_button = $(settings.sendButtonSelector);
        var $confirm_button = $(settings.confirmButtonSelector);
        var $input_country;
        if (settings.countrySelector) {
            $input_country = $(settings.countrySelector);

            $.ajax({url: '/verification/countries/'})
                .done(function(data) {
                    $.each(data, function( index, value ) {
                        $input_country.append("<option value='" + value.number + "'>"+ value.name +"</option>")
                    });
                });
        }

        $send_button.click(function(){
            var data = {phone_number: $(settings.phoneNumberSelector).val()};
            var country = $(settings.countrySelector).val();

            if (country) {
                data.country_number = country;
            }

            $.ajax({
                url: '/verification/pins/',
                method: 'post',
                data: data
            }).done(function(response) {
                if (settings.onSendSuccess){
                    settings.onSendSuccess(response);
                }
                else{
                    alert(response.message);
                }
            }).fail(function(response) {
                var message = "";
                $.each(response.responseJSON, function( key, value ) {
                    message += value + "\n";
                });
                alert(message);
            })
        });

        $confirm_button.click(function(){
            var country_number = $(settings.countrySelector).val();
            var phone_number = $(settings.phoneNumberSelector).val();
            var code = $(settings.codeSelector).val();

            $.ajax({
                url: '/verification/contacts/',
                method: 'post',
                data: {
                    country_number : country_number,
                    phone_number: phone_number,
                    code: code
                }
            }).done(function(data) {
                if (settings.onConfirmSuccess){
                    settings.onConfirmSuccess(data);
                }
                else{
                    location.reload(true);
                }
            }).fail(function(data) {
                var message = "";
                $.each(data.responseJSON, function( key, value ) {
                    message += value + "\n";
                });
                alert(message);
            })
        });
    };
}( jQuery ));
