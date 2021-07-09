{% extends 'base.html' %}

{% block body %}

<!-- Banner -->
	<section id="banner" class="major">
		<div class="inner">
			<header class="major">
				<h1>Responder</h1>
			</header>
			<div class="content">
				<ul class="actions">
    				<form action="/" method="POST">
					<div class="field half">
					<label for="address">Type in your address to locate hospitals near you</label>
					<input type="text" name="address" id="address" />
        			<input type="submit" value="Let's Go!" />
					</form>
				</ul>
			</div>
		</div>
	</section>

		<div id="main">

		<!-- One -->
			<section id="one" class="tiles">
				<article>
					<span class="image">
						<img src="images/maps.jpg" alt="" />
					</span>
					<header class="major">
						<h3><a href="https://maps.google.com/" class="link">Google Maps</a></h3>
						<p>Click here to go to Google Maps</p>
					</header>
				</article>
				<article>
					<span class="image">
						<img src="images/hand.jpg" alt="" />
					</span>
					<header class="major">
						<h3><a href="services.html" class="link">Services</a></h3>
						<p>Learn about health information near you</p>
					</header>
				</article>
				<article>
					<span class="image">
						<img src="images/education.jpg" alt="" />
					</span>
					<header class="major">
						<h3><a href="education.html" class="link">Education</a></h3>
						<p>Learn more about staying safe</p>
					</header>
				</article>
				<article>
					<span class="image">
						<img src="images/team.jpg" alt="" />
					</span>
					<header class="major">
						<h3><a href="about.html" class="link">About Us</a></h3>
						<p>Learn more about who we are</p>
					</header>
				</article>
				</article>
			</section>

		<!-- Two -->
			<section id="two">
				<div class="inner">
					<header class="major">
						<h2>Helping the Community</h2>
					</header>
					<p>Responder is a free service that helps seniors get medical attention as soon as possible. With the help of google maps API, Plotly, and other amazing software, we bring to you Responder. Our grandparents and other seniors are the most vulnerable, especially after the pandemic. Keeping them safe is our first priority. Thanks, for helping us keep everyone safe! </p>
					<ul class="actions">
						<li><a href="about.html" class="button next">Learn more about our team</a></li>
					</ul>
				</div>
			</section>

	</div>

{% endblock %}
