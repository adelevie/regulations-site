define("definition-view", ["jquery", "underscore", "backbone", "regs-view", "regs-data", "regs-dispatch"], function($, _, Backbone, RegsView, RegsData, Dispatch) {
    "use strict";
    var DefinitionView = RegsView.extend({
        className: "open-definition",
        events: {},

        render: function() {
            this.$el.find('.inline-interpretation').remove();
            Dispatch.trigger('definition:render', this.$el);

            return this;
        },

        remove: function() {
            this.stopListening();
            this.$el.remove();
            Dispatch.trigger('definition:remove');

            return this;
        }
    });

    return DefinitionView;
});