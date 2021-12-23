export default function groceriesList() {
  const map = {
    Apples: 10,
    Tomatoes: 10,
    Pasta: 1,
    Rice: 1,
    Banana: 5,
  };

  let ret = new Map();
  for (const item in map) {
    ret.set(item, map[item]);
  }

  return ret;
}
