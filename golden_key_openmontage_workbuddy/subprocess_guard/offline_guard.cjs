"use strict";

if (process.env.GOLDEN_KEY_WORKBUDDY_OFFLINE_GUARD === "1") {
  const message =
    "local-only Tool subprocess network access is blocked by the WorkBuddy runtime";
  const blocked = () => {
    throw new Error(message);
  };

  const net = require("node:net");
  net.connect = blocked;
  net.createConnection = blocked;
  net.Socket.prototype.connect = blocked;

  const tls = require("node:tls");
  tls.connect = blocked;

  for (const moduleName of ["node:http", "node:https"]) {
    const transport = require(moduleName);
    transport.request = blocked;
    transport.get = blocked;
  }

  const dns = require("node:dns");
  for (const name of [
    "lookup",
    "resolve",
    "resolve4",
    "resolve6",
    "resolveAny",
    "reverse",
  ]) {
    dns[name] = blocked;
  }

  const dgram = require("node:dgram");
  dgram.createSocket = blocked;

  globalThis.fetch = blocked;
}
