#!/usr/bin/node
exports.converter = function (base) {
  function baseConvert (num) {
    return (num.toString(base));
  }
  return (baseConvert);
};
