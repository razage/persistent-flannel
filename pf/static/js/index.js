var sidebar = new Vue({
    el: '.sidebar',

    methods: {
        toggleLoginForm: function() {
            $("#login").toggle('slide');
        }
    }

});

var login = new Vue({
    el: '#login',

    data: {
        username: '',
        password: ''
    },

    methods: {
        login: function(el) {
            var that = this;
            console.log(el);

            $.post({
                url: "/users/login",
                data: {
                    username: this.username,
                    password: this.password
                },
                success: function(response) {
                    $(that.$el).toggle('slide');
                    // This seems hacky to me. I'd like to move this to a component eventually.
                    $("#profile").html('<a href="#"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> '+ response.username +'</a>');
                },
                error: function(e) {
                    console.log(e.responseJSON);
                }
            });
        }
    }
})
