import { API_CONFIG } from './config.js';
import { tokenManager } from './tokenManager.js';

async function refreshToken() {
    const refresh = tokenManager.getRefreshToken();
    if (!refresh) throw new Error('Нет refresh токена');

    const response = await fetch(`${API_CONFIG.BASE_URL}/auth/refresh`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refresh }),
    });

    if (!response.ok) throw new Error('Не удалось обновить токен');

    const data = await response.json();
    tokenManager.setAccessToken(data.access);
    tokenManager.setRefreshToken(data.refresh);
    return data.access;
}

export async function http(endpoint, options = {}, retry = 0) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), API_CONFIG.TIMEOUT);

    try {
        const token = tokenManager.getAccessToken();

        const response = await fetch(`${API_CONFIG.BASE_URL}${endpoint}`, {
            signal: controller.signal,
            headers: {
                'Content-Type': 'application/json',
                ...(token ? { Authorization: `Bearer ${token}` } : {}),
                ...options.headers,
            },
            ...options,
        });

        clearTimeout(timeout);

        if (response.status === 401 && retry < API_CONFIG.RETRY_COUNT) {
            // пробуем обновить токен
            const newToken = await refreshToken();
            return http(endpoint, options, retry + 1);
        }

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || `Ошибка ${response.status}`);
        }

        return response.json();

    } catch (error) {
        clearTimeout(timeout);

        if (error.name === 'AbortError') {
            throw new Error('Превышено время ожидания запроса');
        }

        if (API_CONFIG.LOG_ERRORS) {
            console.error(`[HTTP ERROR]: ${error.message}`, { endpoint, options });
        }

        throw error;
    }
}