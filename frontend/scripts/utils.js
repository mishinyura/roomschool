function interpolate(str, params = {}) {
    return str.replace(/\{\{(\w+)\}\}/g, (_, key) => params[key] ?? '');
}

async function request(path) {
    return ['admin', 'employee', 'parent']
}