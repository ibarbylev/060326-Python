# 2. Сетка Bootstrap (Grid System)

## Краткое описание

Сетка Bootstrap — это система разметки страницы на **12 колонок**.

Она позволяет:

* строить адаптивные макеты;
* легко выравнивать блоки;
* менять расположение элементов на разных экранах.

Основные принципы:

* `container` — общий контейнер;
* `row` — строка;
* `col` — колонка.

---

# Базовая структура сетки

## `row` + `col`

```html
<div class="container">
    <div class="row">
        <div class="col">
            Колонка 1
        </div>

        <div class="col">
            Колонка 2
        </div>
    </div>
</div>
```

---

## Как это работает

* `row` делит пространство по горизонтали
* `col` автоматически делит ширину поровну

---

# 12-колоночная система

## Пример деления

```html
<div class="container">
    <div class="row">
        <div class="col-4">
            4/12
        </div>

        <div class="col-8">
            8/12
        </div>
    </div>
</div>
```

---

## Важно

* сумма колонок в строке = 12
* если больше 12 → блоки переносятся

---

# Автоматическое распределение

## Равные колонки

```html
<div class="row">
    <div class="col">
        A
    </div>

    <div class="col">
        B
    </div>

    <div class="col">
        C
    </div>
</div>
```

---

# Адаптивная сетка

Bootstrap работает по размерам экранов:

* `sm` — телефоны
* `md` — планшеты
* `lg` — ноутбуки
* `xl` — большие экраны

---

## Пример адаптивности

```html
<div class="container">
    <div class="row">

        <div class="col-12 col-md-6 col-lg-4">
            Блок 1
        </div>

        <div class="col-12 col-md-6 col-lg-4">
            Блок 2
        </div>

        <div class="col-12 col-md-12 col-lg-4">
            Блок 3
        </div>

    </div>
</div>
```

---

## Как это работает:

* на телефоне: 1 колонка (col-12)
* на планшете: 2 колонки (col-md-6)
* на ПК: 3 колонки (col-lg-4)

---

# Центрирование элементов

## По горизонтали

```html
<div class="row justify-content-center">
    <div class="col-6">
        Центрированный блок
    </div>
</div>
```

---

## По вертикали

```html
<div class="row align-items-center" style="height: 200px;">
    <div class="col">
        По центру по вертикали
    </div>
</div>
```

---

# Отступы в сетке

Bootstrap использует:

* `g-0` — без отступов
* `g-3` — стандартные отступы
* `g-5` — большие отступы

---

## Пример

```html
<div class="row g-3">

    <div class="col-6">
        Блок 1
    </div>

    <div class="col-6">
        Блок 2
    </div>

</div>
```

---

# Полный пример страницы

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Grid System</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

<div class="container mt-4">

    <h1>Сетка Bootstrap</h1>

    <div class="row g-3">

        <div class="col-12 col-md-6 col-lg-4 bg-light p-3">
            Колонка 1
        </div>

        <div class="col-12 col-md-6 col-lg-4 bg-light p-3">
            Колонка 2
        </div>

        <div class="col-12 col-md-12 col-lg-4 bg-light p-3">
            Колонка 3
        </div>

    </div>

</div>

</body>
</html>
```

---

# Мини-практика

## Задание

Создайте страницу:

* контейнер;
* строку (`row`);
* 3 колонки;
* адаптивность:

  * 1 колонка на телефоне;
  * 2 на планшете;
  * 3 на ПК.

---

## Пример результата

```html id="k4m7qp"
<div class="container mt-4">

    <div class="row">

        <div class="col-12 col-md-6 col-lg-4">A</div>
        <div class="col-12 col-md-6 col-lg-4">B</div>
        <div class="col-12 col-md-12 col-lg-4">C</div>

    </div>

</div>
```
