import urllib.request
import webbrowser
import json
import os
import re

# Make a request to Movies API
connection = urllib.request.urlopen("http://127.0.0.1/api/movies.json")
# Read the response output
json_data = connection.read()
# convert JSON response to a Python Dict
movies = json.loads(json_data)

# Styles, Scripting and the main page layout
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#333">
    <title>iTrailer | the best movie trailers website</title>

    <!-- CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">

  </head>
  <body>

      <!-- Navbar -->
      <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">iTrailer</a>
          </div>
        </div>
      </nav>

      <!-- cover image -->
    <div class="jumbotron">
        <div class="overlay">
            <h2 class="welcome">The best Trailers website!</h2>
            <p class="lead">Enjoy our exclusive trailers and 100,000+ trailers for <b>FREE!</b>. </p>
        </div>
    </div>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>


    <main class="container movies-container">
        <div class="row text-center">

            {movie_tiles}
        </div><!-- ./row -->
    </main>

    <!-- Footer -->
      <footer class="footer navbar navbar-fixed-bottom">
          Copyright &copy; 2017. Marei Morsy
      </footer>

    <!-- Javascript -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/app.js"></script>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
            <!-- Movie column -->
            <div class="movie-box col-xs-12 col-sm-6 col-md-4 col-lg-3" data-trailer-youtube-id="{youtube_id}" data-toggle="modal" data-target="#trailer">
                <div class="movie-wrapper">
                    <img class="img-responsive" src="{poster_url}" alt="{movie_title}">
                    <div class="cover boxcaption">
                        <h3>{movie_title}</h3>
                        <p>{storyline}</p>
                    </div>
                </div>
            </div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    #loop through movies
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie['trailer_url'])
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie['trailer_url'])
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        #Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie['title'],
            poster_url=movie['poster_url'],
            youtube_id=trailer_youtube_id,
            storyline = movie['storyline']
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('iTrailer.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
    
open_movies_page(movies)