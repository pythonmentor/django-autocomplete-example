function setAutocomplete() {
    $(".book-input").autocomplete({
        source: autocomplete_url,
        minLength: 3
    });
}

setAutocomplete();
