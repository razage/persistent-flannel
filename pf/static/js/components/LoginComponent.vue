<template>
    <div id="login">
        <form role="form" method="post">
            <input class="form-control" type="text" name="username" placeholder="username" v-model="username">
            <input class="form-control" type="password" name="password" placeholder="password" v-model="password">
            <button class="btn btn-success btn-block btn-login" @click.prevent="login">Login</button>
        </form>
    </div>
</template>

<script>
    import Vue from 'vue';
    import VueLocalStorage from 'vue-ls';

    Vue.use(VueLocalStorage);

    export default {
        data: function() {
            return {
                username: '',
                password: ''
            }
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
                        $('#login').toggle('slide');

                        Vue.ls.set('username', response.username);
                        Vue.ls.set('userId', response.id);

                        // This seems hacky to me. I'd like to move this to a component eventually.
                        $("#profile").html('<a href="#"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> '+ response.username +'</a>');
                        $(".navbar-right").show();
                    },
                    error: function(e) {
                        console.log(e.responseJSON);
                    }
                });
            }
        }
    }
</script>
