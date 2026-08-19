# 5. Ссылки и изображения

## Краткое описание

Ссылки и изображения — это основа навигации и визуального наполнения сайта.

В этом разделе вы научитесь:

* создавать ссылки;
* открывать страницы;
* вставлять изображения;
* работать с атрибутами тегов.

---

# Ссылки

## Тег `<a>`

Используется для перехода на другие страницы или сайты.

Главный атрибут:

* `href` — адрес страницы

---

## Пример

```html id="a7k3mp"
<a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/">
    Перейти на сайт
</a>
```

---

## Открытие в новой вкладке

Атрибут:

* `target="_blank"`

```html
<a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/" target="_blank">
    Открыть в новой вкладке
</a>
```

---

## Внутренние ссылки

Можно ссылаться на другие страницы проекта:

```html
<a href="about.html">
    О нас
</a>
```

---

# Изображения

## Тег `<img>`

Используется для вставки изображений.

Главные атрибуты:

* `src` — путь к изображению;
* `alt` — описание изображения.

---

## Пример

```html
<img src="image.jpg" alt="Описание изображения">
```

---

## Важно

Тег `<img>`:

* не имеет закрывающего тега;
* является самозакрывающимся.

---

# Изображения из интернета

Можно использовать URL.

---

## Пример

```html
<img
    src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
    alt="Пример изображения"
/>
```

---

# Размер изображения (Bootstrap)

Bootstrap позволяет управлять размером изображений.

---

## Пример

```html
<img
    src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
    class="img-fluid"
    alt="Адаптивное изображение"
/>
```

---

# Ссылки + изображения вместе

Изображение может быть кликабельным.

---

## Пример

```html
<a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">
    <img
        src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
        alt="Кликабельное изображение"
    >
</a>
```

Станица откроется в новой вкладке, так как мы указали `target="_blank"`
---

# Bootstrap стили для ссылок

Bootstrap улучшает внешний вид ссылок.

---

## Пример

```html id="q3m6zn"
<a href="https://en.wikipedia.org/wiki/Python_(programming_language)" class="link-primary">
    Ссылка в стиле Bootstrap
</a>
```

# Мини-практика

## Задание

Создайте страницу:

* с ссылкой на внешний сайт;
* с ссылкой, открывающейся в новой вкладке;
* с изображением из интернета;
* с кликабельным изображением.

---

## Пример результата

```html
<!-- Начало страницы -->

<main class="container mt-4">

    <h1>
        Практика ссылок и изображений
    </h1>

    <p>
        <a href="https://example.com" target="_blank">
            Перейти на сайт
        </a>
    </p>

    <p>
        Кликабельное изображение:
    </p>

    <a href="https://example.com">
        <img
            src="https://via.placeholder.com/250"
            class="img-fluid"
            alt="Пример"
        >
    </a>

</main>

<!-- Конец страницы -->
```
