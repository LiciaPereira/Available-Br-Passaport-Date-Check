<h1>Passport Appointment Checker 🛂</h1>

<h2>Overview</h2>
<p>A Python application that monitors a government website for passport appointment availability and alerts you if an earlier slot than your specified date appears.</p>

<h2>Features</h2>
<ul>
    <li>Checks the website every minute for available dates.</li>
    <li>Uses cookies to maintain session authentication.</li>
    <li>Notifies the user on their computer when a date earlier than the threshold is found.</li>
</ul>

<h2>Installation & Dependencies</h2>
<p>This script requires Python and the following packages:</p>
<pre><code>pip install requests-html plyer</code></pre>

<h2>How It Works</h2>
<ol>
    <li>Set your desired threshold date in the script (March 21, 2025, in this example).</li>
    <li>Update your authentication cookies in the program file.</li>
    <li>The script checks the appointment webpage every minute.</li>
    <li>If it finds an earlier date, a notification pops up, and details print to the terminal.</li>
</ol>

<h2>Usage</h2>
<p>Run the script in a terminal:</p>
<pre><code>python passport_checker.py</code></pre>
<p>Make sure to periodically update your cookies for continued access.</p>

<h2>Limitations</h2>
<ul>
    <li>Works for a specific government website (<a href="https://ec-toronto.itamaraty.gov.br/availability">Passport Availability Page</a>).</li>
    <li>Requires manual cookie updates when the session expires.</li>
    <li>Respect website terms of use—automated scraping might be restricted.</li>
</ul>

<h2>License</h2>
<p>This project is free to use but ensure compliance with website policies.</p>
