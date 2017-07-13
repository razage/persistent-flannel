import Vue from 'vue';
import { mixin as clickaway } from 'vue-clickaway';
import LoginComponent from './components/LoginComponent.vue';
require('jquery-ui');
require('underscore');

var loginComponent = Vue.component('login-form', LoginComponent);

var sidebar = new Vue({
    el: '.sidebar-wrapper',

    mixins: [clickaway],

    components: {
        'login-form': loginComponent
    },

    methods: {
        toggleLoginForm: function() {
            $("#login").toggle('slide');
        }
    }
});