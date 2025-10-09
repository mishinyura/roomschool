export class Header {
    constructor(options) {
        this.options = options;
        this.elements = {};
        this._boundHandlers = [];
        this._init();
    }

    _init() {
        this._bindElements();
        this._bindEvents();
        this.onScroll();
    }

    _bindElements() {
        const els = this.options.elements || {};
        Object.entries(els).forEach(([key, selOrEl]) => {
            if (!selOrEl) {
                this.elements[key] = null;
            } else if (typeof selOrEl === 'string') {
                this.elements[key] = document.querySelector(selOrEl);
            } else if (selOrEl instanceof Element || selOrEl === window || selOrEl === document) {
                this.elements[key] = selOrEl;
            } else {
                this.elements[key] = null;
            }
        });
    }

    _resolveTarget(cfg, key) {
        // явная цель в конфиге: 'window' / 'document' / элемент
        if (cfg && cfg.target === 'window') return window;
        if (cfg && cfg.target === 'document') return document;
        if (cfg && cfg.target instanceof Element) return cfg.target;

        return this.elements[key] || null;
    }

    _bindEvents() {
        const handlers = this.options.handlers || {};
        Object.entries(handlers).forEach(([key, handler]) => {
            const target = this._resolveTarget(handler, key);
            if (!target) return;

            // поддержка debounce/опций в конфиге
            let callback = (handler.callback || function () { }).bind(this);

            if (handler.debounce && typeof handler.debounce === 'number') {
                callback = debounce(callback, handler.debounce);
            }

            const options = handler.options || false;
            target.addEventListener(handler.event, callback, options);
            this._boundHandlers.push({ target, event: handler.event, callback, options });
        });
    }

    toggleMenu() {
        this.menu.classList.toggle("active");
        this.burger.classList.toggle("open");
        document.body.classList.toggle("lock");
    }

    onScroll() {
        if (window.scrollY > 50) {
            this.elements.header.classList.add("scrolled");
        } else {
            this.elements.header.classList.remove("scrolled");
        }
    }

    toggleSearch() {
        this.elements.searchBtn.classList.toggle("active");
        this.elements.searchInput.classList.toggle("active");
    }

    searchData(query) {
        console.log('searchData', query);
        // fetch(...)
    }

    destroy() {
        this._boundHandlers.forEach(({ target, event, callback, options }) => {
            target.removeEventListener(event, callback, options);
        });
        this._boundHandlers = [];
    }
}