<code>var length = 200;</br></code>
<code>var PI = 3.14159265358979323846;</br></code>
<code>var TWO_PI = PI*2;</br></code>
<code></br></code>
<code>var angle = 0;</br></code>
<code>var slider;</br></code>
<code></br></code>
<code>function setup() {</br></code>
<code>createCanvas(400, 400);</br></code>
<code>slider = createSlider(0, TWO_PI, PI / 4, 0.01);</br></code>
<code>}</br></code>
<code></br></code>
<code>function draw() {</br></code>
<code>background(51);</br></code>
<code>angle = slider.value();</br></code>
<code>stroke(255);</br></code>
<code>translate(200, height);</br></code>
<code>branch(100);</br></code>
<code></br></code>
<code>}</br></code>
<code></br></code>
<code>function branch(len) {</br></code>
<code>line(0, 0, 0, -len);</br></code>
<code>translate(0, -len);</br></code>
<code>if (len > 4) {</br></code>
<code>push();</br></code>
<code>rotate(angle);</br></code>
<code>branch(len * 0.67);</br></code>
<code>pop();</br></code>
<code></br></code>
<code>push();</br></code>
<code>rotate(-angle);</br></code>
<code>branch(len * 0.67);</br></code>
<code>pop();</br></code>
<code>}</br></code>
<code>}</br></code>
