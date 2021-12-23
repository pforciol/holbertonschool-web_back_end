export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  } else {
    return [...set]
      .filter((str) => {
        return str.startsWith(startString);
      })
      .map((str) => {
        return str.slice(startString.length);
      })
      .join('-');
  }
}
