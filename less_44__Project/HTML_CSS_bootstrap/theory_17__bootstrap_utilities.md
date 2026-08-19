# 9. Utilities (утилитарные классы Bootstrap)

## Краткое описание

Utilities — это **готовые вспомогательные классы Bootstrap**, которые позволяют быстро управлять стилями без CSS.

С их помощью можно:

* задавать отступы;
* включать flex-раскладку;
* управлять размером элементов;
* скрывать/показывать блоки;
* выравнивать контент.

---

# 1. Отступы (Spacing)

## Синтаксис

```
m - margin (внешний отступ)
p - padding (внутренний отступ)
```

Стороны:

* `t` — top (сверху)
* `b` — bottom (снизу)
* `s` — start (слева)
* `e` — end (справа)
* `x` — слева + справа
* `y` — сверху + снизу

---

## Пример

```html
<div class="mt-3">
    Отступ сверху
</div>

<div class="mb-4">
    Отступ снизу
</div>

<div class="p-3">
    Внутренние отступы
</div>
```

---

## Полный пример

```html
<div class="container">

    <div class="p-3 mb-3 bg-light">
        Блок с отступами
    </div>

</div>
```

---

# 2. Flexbox

Bootstrap активно использует flex.

---

## Включение flex

```html id="t8q4lv"
<div class="d-flex">
    <div>1</div>
    <div>2</div>
</div>
```

---

## Выравнивание по горизонтали

```html
<div class="d-flex justify-content-between">
    <div>Лево</div>
    <div>Право</div>
</div>
```

---

## Выравнивание по центру

```html
<div class="d-flex justify-content-center">
    Центр
</div>
```

---

## Вертикальное выравнивание

```html
<div class="d-flex align-items-center" style="height: 100px;">
    Центр по вертикали
</div>
```

---

# 3. Размеры

## Ширина

```html
<div class="w-25 bg-light">25%</div>
<div class="w-50 bg-light">50%</div>
<div class="w-100 bg-light">100%</div>
```

---

## Высота

```html
<div style="height: 100px;">
    <div class="h-100 bg-light">
        100% высоты
    </div>
</div>
```

---

# 4. Отображение (Display)

## Пример

```html
<div class="d-none">
    Скрытый блок
</div>

<div class="d-block">
    Блочный элемент
</div>

<div class="d-inline">
    Inline элемент
</div>
```

---

# 5. Цвета фона

## Классы

* `bg-primary`
* `bg-success`
* `bg-danger`
* `bg-warning`
* `bg-light`
* `bg-dark`

---

## Пример

```html
<div class="bg-primary text-white p-3">
    Синий фон
</div>

<div class="bg-dark text-white p-3">
    Тёмный фон
</div>
```

---

# 6. Границы и скругления

## Границы

```html
<div class="border p-3">
    С рамкой
</div>
```

---

## Скругление

```html
<div class="rounded bg-light p-3">
    Скруглённые углы
</div>
```

---

# 7. Полный пример страницы

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Utilities</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<div class="container mt-4">

    <h1 class="mb-4">
        Utilities Bootstrap
    </h1>

    <div class="p-3 mb-3 bg-light border rounded">
        Блок с отступами, рамкой и скруглением
    </div>

    <div class="d-flex justify-content-between bg-primary text-white p-3">
        <div>Левый блок</div>
        <div>Правый блок</div>
    </div>

    <div class="mt-3 w-50 bg-success text-white p-2">
        Блок 50% ширины
    </div>

</div>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте страницу:

* 3 блока с разными отступами;
* flex-контейнер с 2 элементами;
* блок с фоном и белым текстом;
* блок с рамкой и скруглением.

---

## Пример результата

```html
<div class="container mt-4">

    <div class="p-2 mb-2 bg-light">Block 1</div>
    <div class="p-3 mb-2 bg-light">Block 2</div>
    <div class="p-4 mb-2 bg-light">Block 3</div>

    <div class="d-flex justify-content-between bg-dark text-white p-3">
        <div>Left</div>
        <div>Right</div>
    </div>

</div>
```
