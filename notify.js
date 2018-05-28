var googlehome = require("google-home-notifier");
var language = "ja";

message = process.argv[2] + "samagairassyaimashita";

googlehome.device("Google-Home-Mini-XXXXXXXXXXXXXX", language);
googlehome.notify(message, function(res) {
  console.log(res);
});
