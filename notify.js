var googlehome = require("google-home-notifier");
var language = "ja";

message = process.argv[2] + "様がいらっしゃいました";

googlehome.device(process.env.GOOGLEHOME, language);
googlehome.notify(message, function(res) {
  console.log(res);
});
