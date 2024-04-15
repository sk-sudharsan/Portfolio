//function initMap() {
//    // Latitude and Longitude
//    var myLatLng = {lat: 20.5937, lng: 78.9629};
//
//    var map = new google.maps.Map(document.getElementById('google-maps'), {
//        zoom: 17,
//        center: myLatLng
//    });
//
//    var marker = new google.maps.Marker({
//        position: myLatLng,
//        map: map,
//        title: 'KERALA, INDIA' // Title Location
//    });
//}
        function initMap() {
            // Latitude and Longitude for India
            var indiaLatLng = {lat: 20.5937, lng: 78.9629};

            var map = new google.maps.Map(document.getElementById('google-maps'), {
                zoom: 5,
                center: indiaLatLng
            });

            var marker = new google.maps.Marker({
                position: indiaLatLng,
                map: map,
                title: 'India' // Title Location
            });
        }