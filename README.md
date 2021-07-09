<!--
	Forty by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Responder</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="css/main.css" />
		<noscript><link rel="stylesheet" href="css/noscript.css" /></noscript>
	</head>
	<style>
		a {
			border-bottom: none !important;
		}
		@media only screen and (max-device-width: 480px) {
		    div.large-menu {
			display: none;
		    }
		}

		@media only screen and (min-device-width: 481px) {
		    div.large-menu {
				display: -moz-flex;
				display: -webkit-flex;
				display: -ms-flex;
				display: flex;
				-moz-justify-content: -moz-flex-end;
				-webkit-justify-content: -webkit-flex-end;
				-ms-justify-content: -ms-flex-end;
				justify-content: flex-end;
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				height: inherit;
				line-height: inherit;
		    }

		    div.large-menu a {
			margin-right: 25px;
		    }

		    div.small-menu {
			display: none;
		    }
		}

		div.input {
		    display: inline-block;
		}
	</style>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header" class="alt">
						<a href="/" class="logo"><strong>Responder</strong> <span>For Seniors</span></a>
						<div class="large-menu">
							<a href="/">Home</a>
							<a href="services">Services</a>
							<a href="education">Education</a>
							<a href="about-us">About Us</a>
						</div>
						<div class="small-menu">
							<nav>
								<a href="#menu">Menu</a>
							</nav>
						</div>
					</header>

				<!-- Menu -->
					<nav id="menu">
						<ul class="links">
							<li><a href="index.html">Home</a></li>
							<li><a href="landing.html">Landing</a></li>
							<li><a href="generic.html">Generic</a></li>
							<li><a href="elements.html">Elements</a></li>
						</ul>
						<ul class="actions stacked">
							<li><a href="#" class="button primary fit">Get Started</a></li>
							<li><a href="#" class="button fit">Log In</a></li>
						</ul>
					</nav>

				<!-- Banner -->

				<!-- Banner -->
					<section id="banner" class="alt">
						<div class="inner">
							<header class="alt">
								<h1>Responder</h1>
							</header>
							<div class="content">
								<ul class="actions">
								<form action="/" method="POST">
									<div class="field half">
									<label for="address">Type in your address to locate hospitals near you</label>
									<div class="input"><input size="50" type="text" name="address" id="address" /></div>
									<div class="input"><input type="submit" value="Let's Go!" /></div>
									</div>
									<div>{{ error_msg }}</div>
								</form>
								</ul>
							</div>
						</div>
					</section>
				<!-- Main -->
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
<!--

					<section id="contact">
						<div class="inner">
							<section>
								<form method="post" action="#">
									<div class="fields">
										<div class="field half">
											<label for="name">Name</label>
											<input type="text" name="name" id="name" />
										</div>
										<div class="field half">
											<label for="email">Email</label>
											<input type="text" name="email" id="email" />
										</div>
										<div class="field">
											<label for="message">Message</label>
											<textarea name="message" id="message" rows="6"></textarea>
										</div>
									</div>
									<ul class="actions">
										<li><input type="submit" value="Send Message" class="primary" /></li>
										<li><input type="reset" value="Clear" /></li>
									</ul>
								</form>
							</section>
							<section class="split">
								<section>
									<div class="contact-method">
										<span class="icon solid alt fa-envelope"></span>
										<h3>Email</h3>
										<a href="#">information@untitled.tld</a>
									</div>
								</section>
								<section>
									<div class="contact-method">
										<span class="icon solid alt fa-phone"></span>
										<h3>Phone</h3>
										<span>(000) 000-0000 x12387</span>
									</div>
								</section>
								<section>
									<div class="contact-method">
										<span class="icon solid alt fa-home"></span>
										<h3>Address</h3>
										<span>1234 Somewhere Road #5432<br />
										Nashville, TN 00000<br />
										United States of America</span>
									</div>
								</section>
							</section>
						</div>
					</section>
-->
				<!-- Footer -->
					<footer id="footer">
						<div class="inner">
							<ul class="icons">
								<li><a href="#" class="icon brands alt fa-github"><span class="label">GitHub</span></a></li>
							</ul>
							<ul class="copyright">
								<li>&copy; Responder</li><li>Design: HTML5</a></li>
							</ul>
						</div>
					</footer>

			</div>
			

		<!-- Scripts -->
			<script src="js/jquery.min.js"></script>
			<script src="js/jquery.scrolly.min.js"></script>
			<script src="js/jquery.scrollex.min.js"></script>
			<script src="js/browser.min.js"></script>
			<script src="js/breakpoints.min.js"></script>
			<script src="js/util.js"></script>
			<script src="js/main.js"></script>

	</body>
</html>
