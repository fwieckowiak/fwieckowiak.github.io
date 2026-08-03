---
title: "My First Bikepacking Trip : Lille - Bergen Op Zoom"
collection: personal
type: "Bikepacking"
permalink: /personal/2014-bikepacking-trip-1
venue: "Bergen Op Zoom, Netherlands"
excerpt: "<img src='/personal/bergen/bergen (2).jpg' width='60%' height='auto'/>"
date: August 2025
---
# ⸻


Here are a few photos from my very first bikepacking trip ! 

I was lucky to be introduced to bikepacking by my good friend François. He is a very experienced bikepacker, so I received great advice for my first trip.

For this adventure, I used my vintage Raymond Poulidor road bike, my first road bike. I fitted it with a small second-hand rear rack and strapped my tent and sleeping mat to it. Unfortunately, I also carried a backpack, which is something I would not recommend for any kind of cycling!!

<div align="center">

<table>
  <tr>
    <td><img src="bergen\bergen (2).jpg" width="100%"></td>
    <td><img src="bergen\bergen%20(5).jpg" width="100%"></td>
  </tr>
  <tr>
    <td><img src="bergen\bergen%20(18).jpg" width="100%"></td>
    <td><img src="bergen\bergen%20(19).jpg" width="100%"></td>
  </tr>
</table>

<div align="center">
  <img
    id="planImage"
    src="bergen/plan.png"
    style="width:80%; cursor: zoom-in;"
    alt="Map">
</div>

<!-- Panzoom -->
<script src="https://cdn.jsdelivr.net/npm/@panzoom/panzoom/dist/panzoom.min.js"></script>

<script>
document.addEventListener("DOMContentLoaded", () => {
    const img = document.getElementById("planImage");

    img.addEventListener("click", () => {

        const overlay = document.createElement("div");
        overlay.style.cssText = `
            position:fixed;
            inset:0;
            background:rgba(0,0,0,0.9);
            display:flex;
            align-items:center;
            justify-content:center;
            z-index:9999;
            overflow:hidden;
        `;

        const clone = img.cloneNode(true);

        clone.style.cssText = `
            max-width:none;
            max-height:none;
            width:auto;
            height:auto;
            cursor:grab;
        `;

        overlay.appendChild(clone);
        document.body.appendChild(overlay);

        const panzoom = Panzoom(clone, {
            maxScale: 10,
            minScale: 0.2
        });

        // Active le zoom molette sur l'image
        clone.addEventListener("wheel", panzoom.zoomWithWheel, {
            passive: false
        });

        // Ferme en cliquant sur le fond
        overlay.addEventListener("click", (e) => {
            if (e.target === overlay) {
                overlay.remove();
            }
        });

    });
});
</script>
Our route started in Lille, crossed Belgium, and ended in bergen\Bergen op Zoom, a seaside town in the Netherlands.

The trip covered about 230 km over three and a half days.

<div align="center">

<img src="bergen\bergen%20(27).jpg" width="100%"> | <img src="bergen\bergen%20(32).jpg" width="100%">

</div>

It was an amazing adventure, and I am very grateful to François for introducing me to bikepacking. That first trip got me hooked, and it was only the beginning !

<div align="center">

<table>
  <tr>
    <td><img src="bergen\bergen%20(31).jpg" width="100%"></td>
    <td><img src="bergen\bergen%20(35).jpg" width="100%"></td>
  </tr>
</table>

</div>