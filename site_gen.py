import os

begin_str = """
<html>
  <head>
    <meta charset="UTF-8">
    <title>Kyle Kastner's Homepage</title>
  </head>
    <article>
      <header>
        <h3>Around the Web</h3>
      </header>
  <div>You can find me on Twitter at <a href="https://twitter.com/kastnerkyle">https://twitter.com/kastnerkyle</a></div>

  <div><br/>For more code, see my GitHub at <a href="https://github.com/kastnerkyle">https://github.com/kastnerkyle</a></div>

  <div><br/>Papers I've written or helped write can be found on <a href="https://scholar.google.ca/citations?user=0XtGoMUAAAAJ&hl=en">Google Scholar</a></div>
    </article>

  <br/>

  <header>
    <h3>Blog Posts</h3>
  </header>
"""

index_blogpost_fill_str = """
<div><br/><a href="https://kastnerkyle.github.io/{}">{}</div>
"""

end_str = """
</html>
"""

post_index_html = """
<html>
  <header>
    <h3>{}</h3>
  </header>
<div><br/><a href="https://colab.research.google.com/github/kastnerkyle/kastnerkyle.github.io/blob/master/{}">Explore the post in your browser using Colab</div>

<div><br/><a href="https://github.com/kastnerkyle/kastnerkyle.github.io/tree/master/{}">See the pre-rendered post on GitHub</div>

</html>
"""

blog_fill_str = ""

post_dirs = ["posts/" + p for p in sorted(os.listdir("posts"))]
for post_dir in post_dirs:
    title = " ".join([w[0].upper() + w[1:] for w in post_dir.split(os.sep)[-1].split("-")])
    if post_dir[-3:] in [".sh", ".py"]:
        continue
    blog_fill_str += index_blogpost_fill_str.format(post_dir + "/" + "index.html", title)
    with open(post_dir + os.sep + "index.html", "w") as f:
        ipynb_name = [p for p in os.listdir(post_dir) if p.endswith(".ipynb")][0]
        pth = post_dir + os.sep + ipynb_name
        f.write(post_index_html.format(title, pth, pth))

with open("index.html", "w") as f:
    f.write(begin_str + blog_fill_str + end_str)
