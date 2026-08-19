# 4. Кнопки (Buttons) в Bootstrap

## Краткое описание

Кнопки — один из самых часто используемых элементов интерфейса.

Bootstrap позволяет:

* быстро создавать красивые кнопки;
* задавать цвета и размеры;
* комбинировать стили;
* делать кнопки адаптивными и единообразными.

---

# Базовая кнопка

## Класс `btn`

Без него кнопка выглядит как обычная HTML-кнопка.

```html
<button class="btn">
    Кнопка
</button>
```

---

# Цвета кнопок

## Основные варианты

Bootstrap даёт готовые цветовые стили:

* `btn-primary` — основная (синяя)
* `btn-success` — зелёная
* `btn-danger` — красная
* `btn-warning` — жёлтая
* `btn-info` — голубая
* `btn-dark` — тёмная
* `btn-light` — светлая

---

## Пример

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
```

---

# Контурные кнопки

## Класс `btn-outline-*`

Кнопка без заливки, только с рамкой.

```html
<button class="btn btn-outline-primary">Primary</button>
<button class="btn btn-outline-success">Success</button>
<button class="btn btn-outline-danger">Danger</button>
```

---

# Размеры кнопок

## Большие и маленькие кнопки

* `btn-lg` — большая
* `btn-sm` — маленькая

---

## Пример

```html
<button class="btn btn-primary btn-lg">Большая</button>
<button class="btn btn-primary">Обычная</button>
<button class="btn btn-primary btn-sm">Маленькая</button>
```

---

# Блочные кнопки

## На всю ширину

Класс:

* `d-grid`
* `w-100`

---

## Пример

```html
<div class="d-grid">
    <button class="btn btn-primary">
        Кнопка на всю ширину
    </button>
</div>
```

---

# Группы кнопок

## Класс `btn-group`

Используется для объединения кнопок.

---

## Пример

```html
<div class="btn-group">
    <button class="btn btn-primary">Левый</button>
    <button class="btn btn-primary">Центр</button>
    <button class="btn btn-primary">Правый</button>
</div>
```

---

# Кнопка-ссылка

## `<a>` как кнопка

```html
<a href="https://example.com" class="btn btn-primary">
    Перейти
</a>
```

---

# Отключённая кнопка

## Класс `disabled`

```html
<button class="btn btn-primary" disabled>
    Недоступно
</button>
```

---

# Комбинирование стилей

```html
<button class="btn btn-success btn-lg">
    Большая зелёная кнопка
</button>
```

---

# Полный пример страницы

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Buttons</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<div class="container mt-4">

    <h1 class="mb-4">
        Кнопки Bootstrap
    </h1>

    <button class="btn btn-primary">Primary</button>
    <button class="btn btn-success">Success</button>
    <button class="btn btn-danger">Danger</button>

    <hr>

    <button class="btn btn-outline-primary">Outline</button>

    <hr>

    <div class="btn-group">
        <button class="btn btn-primary">1</button>
        <button class="btn btn-primary">2</button>
        <button class="btn btn-primary">3</button>
    </div>

</div>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте страницу:

* 3 цветные кнопки;
* 2 outline-кнопки;
* одну большую кнопку;
* одну группу кнопок.

---

## Пример результата

```html
<div class="container mt-4">

    <button class="btn btn-primary">Primary</button>
    <button class="btn btn-success">Success</button>
    <button class="btn btn-danger">Danger</button>

    <hr>

    <button class="btn btn-outline-primary">Outline 1</button>
    <button class="btn btn-outline-success">Outline 2</button>

    <hr>

    <button class="btn btn-primary btn-lg">Большая кнопка</button>

    <hr>

    <div class="btn-group">
        <button class="btn btn-primary">A</button>
        <button class="btn btn-primary">B</button>
        <button class="btn btn-primary">C</button>
    </div>

</div>
```
