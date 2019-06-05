odoo.define("cap_widget_color", function (require) {
    "use strict";

    var ListRenderer = require('web.ListRenderer');
    var pyUtils = require("web.py_utils");

    ListRenderer.include({

        applyColorizeHelper: function ($td, nodeOptions, node, nodeAttribute, cssAttribute, ctx) {
            if (nodeOptions[nodeAttribute]) {
                var colors = _(nodeOptions[nodeAttribute].split(';'))
                    .chain()
                    .map(this.pairColors)
                    .value()
                    .filter(function CheckUndefined(value, index, ar) {
                        return value !== undefined;
                    });
                for (var i=0, len=colors.length; i<len; ++i) {
                    var pair = colors[i],
                        color = pair[0],
                        expression = pair[1];
// CAP START
                    try {
                        color = py.evaluate(py.parse(py.tokenize(pair[0])), ctx).toJSON();
                    } catch(error) {
                        color = pair[0];
                    }
// CAP END
                    if (py.evaluate(expression, ctx).toJSON()) {
                        $td.css(cssAttribute, color);
                    }
                }
            }
        },

    });
});
