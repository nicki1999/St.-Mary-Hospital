const obj = { a: 1, b: 2, c: 3 };
const keys = Object.getOwnPropertyNames(obj);

keys.forEach(key => {
  console.log(key);              // Output: a, b, c
  console.log(obj[key]);         // Output: 1, 2, 3
});
