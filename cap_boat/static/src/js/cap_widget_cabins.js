odoo.define("cap_boat.cap_widget_cabins", function (require) {

    "use strict";

    var core = require('web.core');

    var ActionManager = require("web.ActionManager");
    var AbstractField = require("web.AbstractField");
    var Registry = require("web.field_registry");

    function invertColor(hex, bw) {
        if (hex.indexOf('#') === 0) {
            hex = hex.slice(1);
        }
        // CONVERT 3-DIGIT HEX TO 6-DIGITS.
        if (hex.length === 3) {
            hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
        }
        if (hex.length !== 6) {
            throw new Error('Invalid HEX color.');
        }
        var r = parseInt(hex.slice(0, 2), 16),
            g = parseInt(hex.slice(2, 4), 16),
            b = parseInt(hex.slice(4, 6), 16);
        if (bw) {
            // http://stackoverflow.com/a/3943023/112731
            return (r * 0.299 + g * 0.587 + b * 0.114) > 150 ? '#000000' : '#FFFFFF';
        }
        // INVERT COLOR COMPONENTS
        r = (255 - r).toString(16);
        g = (255 - g).toString(16);
        b = (255 - b).toString(16);
        // PAD EACH WITH ZEROS AND RETURN
        return "#" + padZero(r) + padZero(g) + padZero(b);
    }

    var Cabins = AbstractField.extend({

        template: "Cabins",
        supportedFieldTypes: ["one2many"],
        fieldsToFetch: {
            color: {type: "char"},
            id: {type: "int"},
            name: {type: "char"},
            is_reserved: {type: "bool"},
            x: {type: "int"},
            y: {type: "int"},
        },

        events: _.extend({}, AbstractField.prototype.events, {
            "click button#mass_editing": "_mass_editing",
        }),

        init: function (parent, name, record, options) {
            this._super.apply(this, arguments);
            this._reset_widget();
        },

        _reset_widget: function () {
            var max_x = -1;
            var max_y = -1;
            var max_label_length = "";
            var elements = [];
            this.value.data.forEach(function (element) {
                if (element.data.x > max_x) {
                    max_x = element.data.x;
                };
                if (element.data.y > max_y) {
                    max_y = element.data.y;
                };
                if (element.data.name.length > max_label_length.length) {
                    max_label_length = element.data.name.length;
                };
                elements.push(element.data);
            });
            this.rows = [];
            for (var i = 0; i < max_x + 1; i++) {
                var row = [];
                for (var j = 0; j < max_y + 1; j++) {
                    var oldLength = row.length;
                    elements.forEach(function (element) {
                        if (element.x == i && element.y == j) {
                            element.font_color = invertColor(element.color, true);
                            element.cabin = true;
                            if (element.is_reserved) {
                                element.title = "Passager 1: Martin DUPONT\nAdresse: 5 Rue de la poste 38000 City";
                            };
                            row.push(element);
                        };
                    });
                    if (row.length != oldLength + 1) {
                        row.push({
                            "cabin": false,
                            "color": "white",
                            "font_color": "white",
                            "name": "",
                            "x": i,
                            "y": j
                        });
                    };
                };
                row.sort(function (A, B) {
                    return A.y - B.y;
                });
                this.rows.push(row)
            };
        },

        _render: function () {
            this._reset_widget();
            this.renderElement();
        },

        _reload_edit_mode: function () {
            this.doAction({
                "type": "ir.actions.client",
                "tag": "reload",
            });
        },

        _mass_editing: function () {
            var ids = [];
            this.$(".cabins:checkbox:checked").each(function (index) {
                ids.push(this.id);
            });
            if (ids.length > 1) {
                this.do_action("cap_boat.ir_actions_act_window_06", {
                    "additional_context": {"active_ids": ids},
//                    "on_close": this._reload_edit_mode,
                });
            };
        },

    });

    Registry.add("cabins", Cabins);

    return Cabins;

});
