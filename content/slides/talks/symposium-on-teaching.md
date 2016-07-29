+++
title = "Symposium"
+++

[!](columns 7:5)

# Technology to enable instant gratification & evaluation

[!](split)

## TL;TR

> Powerpoint (Keynote, Openoffice) is no longer considered *technology*.

---

## Mycamps - the right way


```sql
SELECT * FROM schedule;
```

[!](columns 8:4)

<iframe src="http://localhost:" style=width:100%;height:400px></iframe>

[!](split)
> Haha.  Tricked you.  <i class="fa fa-smile-o"></i>


---

## Mycamps - the right way


```sql
SELECT distinct semester FROM schedule;
```

[!](columns 8:4)

<iframe src="http://localhost:" style=width:100%;height:500px></iframe>

[!](split)

Try without the `distinct` keyword.

---

## Mycamps - the right way

```sql
SELECT distinct semester, code 
FROM schedule
WHERE instructor like '%Ken%';
```

[!](columns 8:4)

<iframe src="http://localhost:" style=width:100%;height:500px></iframe>

[!](split)

Can you modify the query to suit your own needs?


Can you see what the `LIKE` clause is doing?

---

## Mycamps - the right way

```sql
SELECT distinct semester, code, weekday
FROM schedule WHERE instructor like '%Ken%' ORDER BY semester, weekday;
```

[!](columns 8:4)

<iframe src="http://localhost:" style=width:100%;height:500px></iframe>

[!](split)

How is your teaching assignment?

---

## Mycamps - the right way

```sql
SELECT distinct semester, code, weekday, starthour || ':' || startmin AS time
FROM schedule WHERE instructor like '%Ken%' ORDER BY semester, weekday;
```

[!](columns 8:4)

<iframe src="http://localhost:" style=width:100%;height:400px></iframe>

[!](split)

How is your teaching schedule?

---

# Where are we going with this?


