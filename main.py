from flask import Flask, render_template, url_for, git

app = Flask(__name__)

@app.route('/', methods=['POST'])
  def first():
    if request.method == 'POST'
      repo = git.Repo('path/to/git_repo')
      origin = repo.remotes.origin

      origin.pull()

       return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400 

