export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';

  return [...set]
    .filter((str) => typeof str === 'string' && str.startsWith(startString))
    .map((str) => str.slice(startString.length))
    .join('-');
}
