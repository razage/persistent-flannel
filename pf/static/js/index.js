import Vue from 'vue';
import VueClickaway from 'vue-clickaway'
require('jquery-ui');
//import { mixin as clickaway } from 'vue-clickaway';

var loginComponent = Vue.component('login-form', {
    template: '    <div id="login"><form role="form" method="post"><input class="form-control" type="text" name="username" placeholder="username" v-model="username"><input class="form-control" type="password" name="password" placeholder="password" v-model="password"><button class="btn btn-success btn-block" @click.prevent="login">Login</button></form></div>',

    data: function() {
        return {
            username: '',
            password: ''
        }
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
                    $('#login').toggle('slide');
                    // This seems hacky to me. I'd like to move this to a component eventually.
                    $("#profile").html('<a href="#"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> '+ response.username +'</a>');
                },
                error: function(e) {
                    console.log(e.responseJSON);
                }
            });
        }
    }
});

var sidebar = new Vue({
    el: '.sidebar-wrapper',

    mixins: [ VueClickaway.mixin ],

    components: {
        'login-form': loginComponent
    },

    methods: {
        toggleLoginForm: function() {
            $("#login").toggle('slide');
        }
    }
});