export default function hasValuesFromArray(set, array) {
  return array.every((value) => {
    return set.has(value);
  });
}
