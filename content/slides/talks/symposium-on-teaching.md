+++
title = "Symposium"
nochalk = true
footnote = "Symposium on Teaching, Faculty of Science, 2016"
+++

# Instant gratification 

[!](highlight)


<p style=text-align:right>
<i>Ken Pu</i> <br>

September 1, 2016 <br>

Symposium on teaching
</p>


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

The Equalizer
============================================

[!](highlight)


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
```{sql sm clipboard}
select distinct code, title from schedule where instructor like "Ken Pu";
```

<iframe class=fragment data-src="http://db.science.uoit.ca:8080" style="max-width:1024px; width:100%; height:400px"></iframe>

Example (2)
================================================

> Anything that is early in the morning?
>
```{sql sm clipboard}
select distinct code, title, weekday, starthour || ":" || startmin as t from schedule
where starthour < 9 and instructor like "Ken Pu";
```

<iframe data-src="http://db.science.uoit.ca:8080" style="max-width:1024px; width:100%; height:300px"></iframe>

Example (3)
===============================================

> Can I find an empty room?
>
```{sql sm clipboard}
with R(room, weekday, t) as (
    select distinct room, weekday, min(starthour) from schedule where room like '% A1 %' and weekday = "T" group by room order by room
) select * from R where t >= 10;
```

<iframe data-src="http://db.science.uoit.ca:8080" style="max-width:1024px; width:100%; height:300px"></iframe>








On the distribution of primes
==============================

<iframe class=fragment data-src="http://db.science.uoit.ca:3000/notebooks/HelloWorld.ipynb" style="max-width:1024px; width:100%; height:500px"></iframe>


Data Science & Visualization
============================

<iframe data-src="http://db.science.uoit.ca:3000/notebooks/DataScience.ipynb" style="max-width:1024px; width:100%; height:500px"></iframe>












# The Danger

[!](highlight)



[!](break)

[!](columns 4:)

## Danger of instant gratification

[!](split)

## Claim:

*We just covered the following topics*:

>
> 1. Data analysis using relational query language
> 2. Python list comprehension
> 3. Numerical approximation of the distribution of the primes
> 4. Visualization of potential fields


<div style=height:150px></div>

## Reality: *Zero working knowledge* even after hands on practice!






# Instant gratification <br> for the instructors

[!](highlight)

# Don't discount Google Education App

> UOIT is paying for it.

# Activate your `uoit.net` account **today**.

> https://ssbp.mycampus.ca/apex/f?p=340:101:17205337333607

# The benefit

- Google Drive <br><br>

- Google Plus <br><br>

- 
    ## Google Quiz

    > https://support.google.com/docs/answer/7032287?hl=en


# Test your working knowledge

[!](columns 8:)

<iframe
data-src="https://docs.google.com/forms/d/e/1FAIpQLScAHM9K4G_cZLIbOsjQUvIZJPzUYH33OI7qu-tvWckF45FMWw/viewform?embedded=true"
width="760" height="500" frameborder="0" marginheight="0"
marginwidth="0">Loading...</iframe>


[!](split)

Separate Window

>
> http://goo.gl/lijEIT

Realtime monitoring

>
> http://goo.gl/xKUzKf













# Closing Remarks

[!](highlight)

[!](break)

> *First, I try to dramatically increase a student's self-expectations and, of
> course, their knowledge about the subject. Being a good teacher means
> stretching students without discouraging them or destroying their confidence.*
>
> Terence Parr, Professor of CS, University of San Francisco

[!](break)

Technology is inherently disruptive.  Disruptive technology is **bad** 51% of the time.

<br><br>

... but good 45% of the time.

<br><br>

... and transformational 3.99999% of the time.


# AMA on

[!](highlight)

*Experimental technology*
----

> - Docker
- SSH over HTTPS
- Jupyter Notebook

---

*Rock solid*
---

> - Google Quiz, but still...

---

"In the midst of chaos, there is also opportunity"

危中機 (\ˈwā\ zhü \ˈȯn \ˈjē)

<p style=text-align:right>
<i>Sun Tzu</i>, Art of War
</p>
