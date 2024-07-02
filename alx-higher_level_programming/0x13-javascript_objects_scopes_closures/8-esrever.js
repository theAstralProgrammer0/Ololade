#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const last = list.length - 1;
  let i = last;
  while (i >= len / 2) {
    const temp = list[i];
    list[i] = list[len - i - 1];
    list[len - i - 1] = temp;
    i -= 1;
  }

  return (list);
};
