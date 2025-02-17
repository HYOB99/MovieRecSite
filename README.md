<h1>Movie Recommendation System</h1>


<h2>Introduction</h2>
The goal of our project is to create a movie recommendation system. With little knowledge in machine learning, the recommendation system will likely not be functioning as we want. To achieve our ultimate goal, we are learning <a href="https://www.coursera.org/professional-certificates/tensorflow-in-practice">TensorFlow</a> course offered by Coursera. As of now, the system only works in localhost address; however, we are planning on hosting it once we complete building the website. <a href="https://flask.palletsprojects.com/en/2.0.x/">Flask Documentation</a> and <a href="https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH">Flask Tutorial Video</a> substantially has helped this project.


<h2>Design Process</h2>
This project is in progress in Python Project Team in <a href="illinois.campuslabs.com/engage/organization/codable">Codable at UIUC</a>. For front end, we used <code>HTML</code>, <code>CSS</code>, and <code>Python</code>. For back end, we used <code>Flask</code>, and for our database, we used <code>SQLAlchemy</code>.  

<h2>Subgoals</h2>
<ol>
  <li>Get the movie data from <a href="https://datasets.imdbws.com/">IMDb</a> and clean the data using <code>Pandas</code>.</li>
  <li>Create a website and redirect the movies users want to watch to the streaming sites such as Netflix.</li>
  <li>Create a login system and secure the user data.</li>
  <li>Structure a movie recommendation system based on individual's watching history.</li>
 </ol>

<h2>How to run the website on localhost</h2>
<p><code>conda activate MovieRecSite</code> to activate the conda environment.</p> 
<p><code>export FLASK_ENV=development</code> to activate debug mode. Debug mode works like a live server on visual studio code.</p>
<p>Now, you are ready to run this website by typing <code>flask run</code>.
