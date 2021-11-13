<h1>Movie Recommendation System</h1>


<h2>Introduction</h2>
The goal of our project is to create a movie recommendation system. With little knowledge in machine learning, the recommendation system will likely not be functioning as we want. To achieve our ultimate goal, we are learning <a href="https://www.coursera.org/professional-certificates/tensorflow-in-practice">TensorFlow</a> course offered by Coursera. As of now, the system only works in localhost address; however, we are planning on hosting it once we complete building the website.


<h2>Design Process</h2>
This project is in progress in Python Project Team in <a href="illinois.campuslabs.com/engage/organization/codable">Codable at UIUC</a>. For front end, we used <code>HTML</code>, <code>CSS</code>, and <code>Python</code>. For back end, we used <code>Flask</code>, and for our database, we used <code>SQLAlchemy</code>.  

<h2>Subgoals</h2>
<ol>
  <li>Get the movie data from <a href="https://datasets.imdbws.com/">IMDb</a> and clean the data using <code>SQL</code>.</li>
  <li>Create a website and redirect the movies users want to watch to the streaming sites such as Netflix.</li>
  <li>Create a login system and secure the user data.</li>
  <li>Structure a movie recommendation system based on individual's watching history.</li>
 </ol>

<h2>How to run on the website localhost</h2>
<p>To run the website on localhost, after cloning the repository to your local machine, you must activate conda environment first. You do not have to change your working directory to MovieRecSite directory; you can activate conda environment wherever you want. To do so, simply type <code>conda activate MovieRecSite</code>. If you succesfully activated conda environment, you should see <code>(conda)</code> popping up. After changing your working directory to MovieRecSite directory, type <code>export FLASK_ENV=development</code> to activate debug mode. Debug mode works like a live server on visual studio code; if you change your source code and refresh the website, it will apply changes you have made without making you run the program again. If you do not see any errors so far, you are ready to run this website. You can run it by simply typing <code>flask run</code>.
