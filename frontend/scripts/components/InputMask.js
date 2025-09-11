export class InputMask {
    constructor(objName) {
        this.input = document.querySelector(objName);
        this.input.maxLength = 18;
        this.onlyDigits = v => (v.match(/\d/g) || []).join('');
        // инициализируем значение текущего поля (если там есть цифры)
        this.eventsInit()
        this.input.value = this.formatPhone(this.onlyDigits(this.input.value));
    }

    formatPhone(digits) {
        if (!digits) return '';
        let d = digits;

        // максимум 15 цифр (международный стандарт E.164)
        if (d.length > 15) d = d.slice(0, 15);

        // определяем код страны (1–3 цифры)
        let c = d[0];
        let rest = d.slice(1);

        // если код начинается с 3, 4, 7 и т.д. — часто бывает 2–3 цифры код
        // тут можно доработать под конкретные правила, но пока делаем 1 цифру
        // если захочешь — можно сделать детектор по справочнику кодов стран

        // теперь форматируем оставшуюся часть условно 3-3-2-2
        const p1 = rest.slice(0, 3);
        const p2 = rest.slice(3, 6);
        const p3 = rest.slice(6, 8);
        const p4 = rest.slice(8, 10);
        const p5 = rest.slice(10); // хвост (если код длинный)

        let res = '+' + c;
        if (p1) res += ' (' + p1 + (p1.length === 3 ? ')' : '');
        if (p2) res += ' ' + p2;
        if (p3) res += '-' + p3;
        if (p4) res += '-' + p4;
        if (p5) res += ' ' + p5; // остаток, если вдруг длиннее
        return res;
    }


    // сколько цифр находится до позиции index в отформатированной строке
    digitIndexFromFormattedIndex(formatted, index) {
        const sub = formatted.slice(0, index);
        const m = sub.match(/\d/g);
        return m ? m.length : 0;
    }

    // позиция в отформатированной строке, где должно стоять caret чтобы до него было digitIndex цифр
    formattedIndexFromDigitIndex(formatted, digitIndex) {
        for (let i = 0; i <= formatted.length; i++) {
            const m = formatted.slice(0, i).match(/\d/g);
            const count = m ? m.length : 0;
            if (count === digitIndex) return i;
        }
        return formatted.length;
    }

    eventsInit() {
        // Обработка Backspace / Delete вручную — чтобы корректно удалять цифры, даже если caret стоит у скобки
        this.input.addEventListener('keydown', this.eventKeydown.bind(this));

        // Основная обработка input: очищаем всё кроме цифр и форматируем
        this.input.addEventListener('input', this.eventInput.bind(this));

        // Обработка вставки: вставляем только цифры
        this.input.addEventListener('paste', this.eventPaste.bind(this));
    }

    eventKeydown(input) {
        if (input.target.key !== 'Backspace' && input.target.key !== 'Delete') return;
        input.target.preventDefault();

        const selStart = this.input.selectionStart;
        const selEnd = this.input.selectionEnd;
        const formatted = this.input.value;
        const digits = this.onlyDigits(formatted);
        const dStart = this.digitIndexFromFormattedIndex(formatted, selStart);
        const dEnd = this.digitIndexFromFormattedIndex(formatted, selEnd);

        let newDigits, newCaretDigitIndex;

        if (selStart !== selEnd) {
            // удаляем выделение (удаляем цифры в диапазоне)
            newDigits = digits.slice(0, dStart) + digits.slice(dEnd);
            newCaretDigitIndex = dStart;
        } else {
            if (input.target.key === 'Backspace') {
                if (dStart === 0) {
                    newDigits = digits;
                    newCaretDigitIndex = 0;
                } else {
                    newDigits = digits.slice(0, dStart - 1) + digits.slice(dStart);
                    newCaretDigitIndex = dStart - 1;
                }
            } else { // Delete
                if (dStart >= digits.length) {
                    newDigits = digits;
                    newCaretDigitIndex = digits.length;
                } else {
                    newDigits = digits.slice(0, dStart) + digits.slice(dStart + 1);
                    newCaretDigitIndex = dStart;
                }
            }
        }

        const newFormatted = formatPhone(newDigits);
        this.input.value = newFormatted;
        const caretPos = this.formattedIndexFromDigitIndex(newFormatted, newCaretDigitIndex);
        this.input.setSelectionRange(caretPos, caretPos);
        // опционально: уведомим обработчики, что значение изменилось
        this.input.dispatchEvent(new Event('input', { bubbles: true }));
    }

    eventInput() {
        const oldFormatted = this.input.value;
        const oldCaret = this.input.selectionStart;
        const digits = this.onlyDigits(oldFormatted);
        const digitBefore = this.digitIndexFromFormattedIndex(oldFormatted, oldCaret);

        const newFormatted = this.formatPhone(digits);
        this.input.value = newFormatted;

        const newCaret = this.formattedIndexFromDigitIndex(newFormatted, digitBefore);
        this.input.setSelectionRange(newCaret, newCaret);
    }

    eventPaste(input) {
        input.target.preventDefault();
        const paste = (input.target.clipboardData || window.clipboardData).getData('text');
        const pastedDigits = (paste.match(/\d/g) || []).join('');

        const formatted = this.input.value;
        const selStart = this.input.selectionStart;
        const selEnd = this.input.selectionEnd;
        const digits = this.onlyDigits(formatted);
        const dStart = this.digitIndexFromFormattedIndex(formatted, selStart);
        const dEnd = this.digitIndexFromFormattedIndex(formatted, selEnd);

        const newDigits = digits.slice(0, dStart) + pastedDigits + digits.slice(dEnd);
        const newFormatted = formatPhone(newDigits);
        this.input.value = newFormatted;

        const caretPos = this.formattedIndexFromDigitIndex(newFormatted, dStart + pastedDigits.length);
        this.input.setSelectionRange(caretPos, caretPos);
        this.input.dispatchEvent(new Event('input', { bubbles: true }));
    }
}