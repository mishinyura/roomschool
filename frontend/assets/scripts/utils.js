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

export async function loadData(path) {
  try {
    const res = await fetch(path);
    const data = await res.json();
    return data;
  } catch (err) {
    console.error(err);
    return [];
  }
}

/**
 * Универсальный хелпер для создания DOM-элементов
 * @param {string} tag - Тег элемента (например, 'div')
 * @param {object} [options] - Опции для элемента
 * @param {string} [options.className] - CSS классы
 * @param {string} [options.text] - Текстовое содержимое (textContent)
 * @param {string} [options.html] - HTML содержимое (innerHTML)
 * @param {object} [options.attrs] - Атрибуты { src: "...", href: "..." }
 * @returns {HTMLElement}
 */
export function createElement(tag, { className, text, html, attrs } = {}) {
  const el = document.createElement(tag);
  if (className) el.className = className;
  if (text) el.textContent = text;
  if (html) el.innerHTML = html;
  if (attrs) {
    for (let [key, value] of Object.entries(attrs)) {
      el.setAttribute(key, value);
    }
  }
  return el;
}