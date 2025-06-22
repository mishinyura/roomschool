export const NOTIFICATION_TEMPLATES = {
    forms: {
        title: "Не правильно заполнены данные",
        descriptions: {
            emailInvalid: "Введите корректный Email — он потребуется для подтверждения.",
            passwordShort: "Пароль должен быть не менее {{min}} символов.",
            required: "Поле «{{field}}» обязательно для заполнения.",
        }
    },
    network: {
        title: "Ошибка соединения",
        descriptions: {
            timeout: "Время ожидания истекло. Проверьте интернет-соединение.",
            serverError: "Внутренняя ошибка сервера. Попробуйте позже."
        }
    },
    custom: {
        title: "{{title}}",
        descriptions: {
            customMessage: "{{message}}"
        }
    }
};