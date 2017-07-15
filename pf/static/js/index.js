import Vue from 'vue';
import VueCookie from 'vue-cookie';
import { mixin as clickaway } from 'vue-clickaway';
import LoginComponent from './components/LoginComponent.vue';
require('jquery-ui');

Vue.use(VueCookie);

var loginComponent = Vue.component('login-form', LoginComponent);

var topbar = new Vue({
    el: '.topbar',

    methods: {
      logout: function() {
        $.get({
          url: "/users/logout",
          success: function(response) {
            window.location = "/";
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

    data: {
        locked: false
    },

    mixins: [clickaway],

    components: {
        'login-form': loginComponent
    },

    methods: {
        toggleLoginForm: function() {
            if(!this.locked) {
                var that = this;
                this.locked = true;

                $("#login").toggle({
                    effect: 'slide',
                    complete: function() {
                        that.locked = false;
                    }
                });
            }
        },

        clickedAway: function() {
            if($('#login').is(":visible")) {
                this.toggleLoginForm();
            }
        }
    }
});
