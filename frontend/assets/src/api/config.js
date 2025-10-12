export const API_CONFIG = {
    BASE_URL: import.meta.env.VITE_API_URL || 'https://api.roomschool.com',
    TIMEOUT: 10000, // 10 секунд
    RETRY_COUNT: 2,
    LOG_ERRORS: import.meta.env.PROD !== true, // в проде — false
};