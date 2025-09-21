function interpolate(str, params = {}) {
    return str.replace(/\{\{(\w+)\}\}/g, (_, key) => params[key] ?? '');
}

async function request(path) {
    return ['admin', 'employee', 'parent']
}

export const pluralize = (num, one, few, many) => {
    if (num % 10 === 1 && num % 100 !== 11) return `${num} ${one}`;
    if ([2, 3, 4].includes(num % 10) && ![12, 13, 14].includes(num % 100)) return `${num} ${few}`;
    return `${num} ${many}`;
};


export function timeFormatDuration(minutes) {
  if (minutes < 60) return pluralize(minutes, "минута", "минуты", "минут");

  const hours = Math.floor(minutes / 60);
  const mins = minutes % 60;

  if (mins === 0) return pluralize(hours, "час", "часа", "часов");

  return `${pluralize(hours, "час", "часа", "часов")} ${pluralize(mins, "минута", "минуты", "минут")}`;
}