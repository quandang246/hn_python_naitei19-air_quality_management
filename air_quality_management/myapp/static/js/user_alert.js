swal({
    title: "Allow us to access to your location?",
    icon: "info",
    allowOutsideClick: false,
    closeOnClickOutside: false,
    allowEscapeKey: false,
    buttons: {
        cancel: "No",
        confirm: {
            text: "Yes",
            value: "yes",
        },
    },
}).then((value) => {
    switch (value) {

        case "yes":
            swal({
                allowOutsideClick: false,
                closeOnClickOutside: false,
                allowEscapeKey: false,
                title: "Thank you!",
                text: "Please choose your location on the map!",
                icon: "success",
            });
            break;

        default :
            swal("Redirecting you back. Please wait a moment!", {
                allowOutsideClick: false,
                closeOnClickOutside: false,
                allowEscapeKey: false,
                button:false,
                timer: 4000,
            }).then(() => {
                window.location.href = "profile";
            })
    }
});