<template>
    <div id="login">
        <form role="form" method="post">
            <input class="form-control" type="text" name="username" placeholder="username" v-model="username">
            <input class="form-control" type="password" name="password" placeholder="password" v-model="password">
            <input class="form-control" type="checkbox" id="remember" name="remember" v-model="remember"><label for="remember">Remember Me</label>
            <button class="btn btn-success btn-block btn-login" @click.prevent="login">Login</button>
        </form>
    </div>
</template>

<script>
    import Vue from 'vue';
    import VueCookie from 'vue-cookie';

    Vue.use(VueCookie);

    export default {
        data: function() {
            return {
                username: '',
                password: '',
                remember: false
            }
        },

        methods: {
          login: function() {
            var that = this;

            $.post({
              url: "/users/login",
              data: {
                username: this.username,
                password: this.password,
                remember: this.remember
              },
              success: function(response) {
                $('#login').toggle('slide');

                if(that.remember) {
                  this.$cookie.set('uId', response.id, { expires: 7 });
                  this.$cookie.set('username', response.username, { expires: 7 });
                }

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
