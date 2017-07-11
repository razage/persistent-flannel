var login = new Vue({
    el: '#login',

    data: {
        username: '',
        password: ''
    },

    methods: {
        login: function() {
            console.log(this.username, this.password);
            $.post({
                url: "/users/login",
                data: {
                    username: this.username,
                    password: this.password
                }
            });
        }
    }

});
