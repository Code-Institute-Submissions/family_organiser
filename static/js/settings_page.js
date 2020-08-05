
    $(document).ready(function() {
        bioCountLength = $('#users-bio').val().length
        bioLimit = 150
        remainingLetters = bioLimit - bioCountLength
        $('#remaining-letters').html(remainingLetters)
    })

    function bioCount() {
            bioCountLength = $('#users-bio').val().length
            bioLimit = 150
            remainingLetters = bioLimit - bioCountLength
            $('#remaining-letters').html(remainingLetters)
        }
