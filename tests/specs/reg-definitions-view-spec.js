define(["definition-view", "regs-data", 'sample-json'], function(DefinitionView, RegsData, testjson) {
  describe("Definitions views", function() {
    RegsData.parse(testjson);

    it("test", function() {
      expect(true).toBeTruthy();
    });

  });
});
