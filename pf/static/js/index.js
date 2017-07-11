var login = new Vue({
    el: '#login',

    data: {
        username: '',
        password: ''
    },

    methods: {
        login: function() {
            $.post({
                url: "/users/login",
                data: {
                    username: this.username,
                    password: this.password
                },
                success: function(response) {
                    console.log(response);
                },
                error: function(e) {
                    console.log(e.responseJSON);
                    $("input[name='username'], input[name='password']").addClass("disabled");
                }
            });
        }
    }

});
