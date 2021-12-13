export default function appendToEachArrayValue(array, appendString) {
  const ret = [];
  for (const value of array) {
    ret.push(appendString + value);
  }

  return ret;
}
