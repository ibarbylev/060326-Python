# 1. Введение в Bootstrap

## Краткое описание

Bootstrap — это готовый набор инструментов для создания интерфейсов.

Он позволяет:

* быстро делать красивые страницы;
* не писать много CSS;
* использовать готовые компоненты (кнопки, формы, сетку);
* сразу получать адаптивный дизайн.

---

# Как подключается Bootstrap

## Подключение CSS

Bootstrap подключается через CDN (сеть доставки контента).

```html id="b1k7qp"
<link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
    rel="stylesheet"
/>
```

---

## Подключение JavaScript

Нужно для интерактивных компонентов:

* меню;
* модальные окна;
* слайдеры.

```html
<script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js">
</script>
```

---

# Базовая структура страницы

## Пример шаблона

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Bootstrap demo</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

    <h1>Hello Bootstrap</h1>

    <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js">
    </script>

</body>
</html>
```

---

# Контейнеры (Containers)

## Кратко

Контейнер — это ограничение ширины контента.

Он помогает:

* центрировать сайт;
* делать отступы;
* адаптировать под разные экраны.

---

# Виды контейнеров

## `container`

Фиксированная ширина (адаптируется по брейкпоинтам).

```html
<div class="container">
    Контент внутри контейнера
</div>
```

---

## `container-fluid`

На всю ширину экрана.

```html
<div class="container-fluid">
    Полноширинный контейнер
</div>
```

---

# Сравнение контейнеров

## Пример

```html
<div class="container">
    Обычный контейнер
</div>

<div class="container-fluid">
    Полная ширина
</div>
```

---

# Практический пример страницы

## Контейнер в действии

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Containers</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

    <div class="container mt-4">
        <h1>Контейнер Bootstrap</h1>

        <p>
            Этот контент находится внутри <code>container</code>.
        </p>
    </div>

    <div class="container-fluid bg-light mt-4 p-3">
        <h2>Fluid контейнер</h2>

        <p>
            Этот блок занимает всю ширину экрана.
        </p>
    </div>

</body>
</html>
```

---

# Важное правило

Bootstrap почти всегда начинается с контейнера:

```html
<div class="container">
```

или

```html
<div class="container-fluid">
```

---

# Мини-практика

## Задание

Создайте страницу:

* подключите Bootstrap;
* добавьте `container`;
* добавьте `container-fluid`;
* внутри каждого разместите заголовок и текст.

---

## Пример результата

```html
<div class="container mt-4">
    <h1>Обычный контейнер</h1>
    <p>Этот блок центрирован и ограничен по ширине.</p>
</div>

<div class="container-fluid bg-light p-3">
    <h2>Fluid контейнер</h2>
    <p>Этот блок занимает всю ширину экрана.</p>
</div>
```
