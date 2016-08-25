+++
title = "Symposium"
nochalk = true
footnote = "Symposium on Teaching, Faculty of Science, 2016"
+++

Instant gratification 
==========================================

<div style=height:400px></div>

## Ken Pu


TL;TR
===========================================

> - Instant gratification is a powerful equalizer
>   <br><br>
>
> - Instant gratification is dangerous
>   <br><br>
>
> - Technology is almost there
>   <br><br>
>
> - Yes, you can use it now


The equalizer (1)
============================================

[!](columns 5:2:5)

<img class="fragment" src="degrasse.jpg"></img>

[!](split)

<div style=margin-top:200px;font-size:500%>=</div>

[!](split)

<img class="fragment" src="Instant-Gratification.jpg"></img>



The equalizer (2)
============================================

[!](columns 10:)

<img src="engineer.jpg"></img>

> Google Engineer

[!](split)

<div style=font-size:500%>=</div>







The equalizer (2)
============================================

<img style=height:500px src="women-in-cs.jpg"></img>












Example (1)
==============================================

> Finding the courses I teach.
>
```sql
select distinct code, title from schedule where instructor like "Ken Pu";
```

<iframe class=fragment data-src="http://db.science.uoit.ca:8080" style="max-width:1024px; width:100%; height:400px"></iframe>

Example (2)
================================================

> Anything that is early in the morning?
>
```{sql sm}
select distinct code, title, weekday, starthour || ":" || startmin as t from schedule
where starthour < 9 and instructor like "Ken Pu";
```

<iframe data-src="http://db.science.uoit.ca:8080" style="max-width:1024px; width:100%; height:300px"></iframe>

Example (3)
===============================================

> Can I find an empty room?
>
```{sql sm}
with R(room, weekday, t) as (
    select distinct room, weekday, min(starthour) from schedule where room like '% A1 %' and weekday = "T" group by room order by room
) select * from R where t >= 10;
```

<iframe data-src="http://db.science.uoit.ca:8080" style="max-width:1024px; width:100%; height:300px"></iframe>



