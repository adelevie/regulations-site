define("toc-view",["jquery","underscore","backbone","regs-fixed-el-view","regs-dispatch"],function(e,t,n,r,i){var s=r.extend({events:{"click a":"sendClickEvent"},initialize:function(){i.on("activeSection:change",this.setActive,this)},setActive:function(e){return this.$el.find(".current").removeClass("current"),this.$el.find("a[href=#"+e+"]").addClass("current"),this},sendClickEvent:function(t){i.trigger("toc:click",e(t.target).attr("href"))}});return s});