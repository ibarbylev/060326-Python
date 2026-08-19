# 3. Типографика и текст в Bootstrap

## Краткое описание

Bootstrap даёт готовые классы для оформления текста без CSS.

С их помощью можно:

* менять размер и стиль текста;
* управлять цветом;
* выравнивать текст;
* быстро оформлять заголовки и абзацы.

---

# Заголовки

Bootstrap поддерживает стандартные HTML-заголовки:

```html
<h1>Заголовок 1</h1>
<h2>Заголовок 2</h2>
<h3>Заголовок 3</h3>
```

---

## Альтернатива через классы

Можно стилизовать любой текст как заголовок:

```html
<p class="h1">Это как H1</p>
<p class="h2">Это как H2</p>
<p class="h3">Это как H3</p>
```

---

# Размеры текста

## Классы display

Используются для больших заголовков:

```html
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
```

---

# Выравнивание текста

## По центру, слева, справа

```html
<p class="text-start">Слева</p>
<p class="text-center">По центру</p>
<p class="text-end">Справа</p>
```

---

# Цвет текста

Bootstrap имеет готовые цветовые классы:

* `text-primary`
* `text-secondary`
* `text-success`
* `text-danger`
* `text-warning`
* `text-info`
* `text-muted`

---

## Пример

```html
<p class="text-primary">Синий текст</p>
<p class="text-success">Зелёный текст</p>
<p class="text-danger">Красный текст</p>
<p class="text-muted">Приглушённый текст</p>
```

---

# Жирный и курсив

## Жирный текст

```html
<p class="fw-bold">Жирный текст</p>
```

---

## Лёгкий текст

```html
<p class="fw-light">Лёгкий текст</p>
```

---

## Курсив

```html id="x7n4kp"
<p class="fst-italic">Курсив</p>
```

---

# Линия и оформление

## Подчёркивание и декорации

```html
<p class="text-decoration-underline">Подчёркнутый</p>
<p class="text-decoration-line-through">Зачёркнутый</p>
```

---

# Отступы для текста

Bootstrap использует систему spacing:

* `mt-*` — margin top
* `mb-*` — margin bottom
* `p-*` — padding

---

## Пример

```html
<p class="mt-3 mb-3">
    Текст с отступами
</p>
```

---

# Комбинирование стилей

## Пример

```html
<p class="text-center text-primary fw-bold">
    Центрированный синий жирный текст
</p>
```

---

# Полный пример страницы

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Typography</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<div class="container mt-4">

    <h1 class="text-center text-primary">
        Типографика Bootstrap
    </h1>

    <p class="lead text-muted text-center">
        Это пример оформления текста
    </p>

    <p class="fw-bold">
        Жирный текст
    </p>

    <p class="fst-italic">
        Курсив
    </p>

    <p class="text-danger">
        Ошибка или важное сообщение
    </p>

</div>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте страницу:

* заголовок по центру;
* текст разных цветов;
* жирный и курсивный текст;
* один большой заголовок (`display-1`).

---

## Пример результата

```html
<div class="container mt-4">

    <h1 class="display-1 text-center">
        Bootstrap Text
    </h1>

    <p class="text-primary fw-bold">
        Синий жирный текст
    </p>

    <p class="text-success fst-italic">
        Зелёный курсив
    </p>

    <p class="text-danger">
        Красный текст
    </p>

</div>
```
