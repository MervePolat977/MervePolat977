### Hi there 👋

☺️ I am Merve. Welcome to my GitHub profile.  
😄 Pronouns: She/Her  
📚 I am studying at Maltepe University as a 3rd year student.  
👩🏻‍💻 My major is **Software Engineering.**  
✨ Currently, I am learning web development using **HTML-CSS-Javascript and React**  

## Technologies and Tools

<div style="display:flex; justify-content:space-between;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/2048px-HTML5_logo_and_wordmark.svg.png" alt="HTML" width="50" height="50"/>         
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" alt="CSS" width="50" height="50" style="margin-right: 10px;"/>
<img src="https://i0.wp.com/blogs.embarcadero.com/wp-content/uploads/2020/08/JavaScript-logo.png?ssl=1" alt="JavaScript" width="50" height="50" style="margin-right: 10px;"/>
<img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_reactjs_icon_130205.png" alt="React" width="50" height="50" style="margin-right: 10px;"/>
<img src="https://www.kindpng.com/picc/m/403-4039227_c-language-logo-png-transparent-png.png" alt="C" width="50" height="50" style="margin-right
<img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_postgresql_icon_130263.png" alt="PostgreSQL" width="50" height="50" style="margin-right: 10px;"/>
<img src="https://w7.pngwing.com/pngs/173/36/png-transparent-postgresql-logo-computer-software-database-open-source-s-text-head-snout.png" alt="PostgreSQL" width="50" height="50" style="margin-right: 10px;"/>
<img src="https://www.pngmart.com/files/7/Python-Transparent-Background.png" alt="PostgreSQL" width="55" height="50" style="margin-right: 0px;"/>

</div>



---------------------------------------------------------------------------

![Github stats 2](https://github-readme-stats.vercel.app/api?username=MervePolat977&show_icons=true&theme=radical)  
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=MervePolat977&show_icons=true&theme=radical&layout=compact)

------------------------------------------------------------------------------------
⚡ Fun fact: In the future I want to start my own business. But initially need some working experiences🎉 ![coding cat](https://media.giphy.com/media/unQ3IJU2RG7DO/giphy.gif)
  
  
-----------------------------------------------------------------------------------
📫 How to contact me:  
[![Github Badge](https://img.shields.io/badge/-Github-000?style=quare&labelColor=000&logo=Github&logoColor=white&link=link)](https://github.com/MervePolat977) 
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white&link=your-link-here)](https://www.linkedin.com/in/merve-polat-32855619a/)
[![Medium Badge](https://img.shields.io/badge/-Medium-757575?style=flat-quare&labelColor=757575&logo=Medium&logoColor=white&link=link)](https://medium.com/@pmervepolat977) 
[![Instagram Badge](https://img.shields.io/badge/-Instagram-C13584?style=flat-quare&labelColor=C13584&logo=instagram&logoColor=white&link=link)](https://www.instagram.com/mervepolat3790/)   



-----------------

bu kodu readme.md sayfama nasıl ekleyebilirim: # GitHub Action for generating a contribution graph with a snake eating your contributions.
name: Generate Snake

# Controls when the action will run. This action runs every 6 hours.

on:
  schedule:
      # At the end of every day

    - cron: "0 0 * * *"

# This command allows us to run the Action automatically from the Actions tab.
  workflow_dispatch:

# The sequence of runs in this workflow:
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
    
    # Checks repo under $GITHUB_WORKSHOP, so your job can access it
      - uses: actions/checkout@v2
      
    # Generates the snake  
      - uses: Platane/snk@master
        id: snake-gif
        with:
          github_user_name: nurgulsezgin
          # these next 2 lines generate the files on a branch called "output". This keeps the main branch from cluttering up.
          gif_out_path: dist/github-contribution-grid-snake.gif
          svg_out_path: dist/github-contribution-grid-snake.svg
          
     # show the status of the build. Makes it easier for debugging (if there's any issues).
      - run: git status
          
      # Push the changes
      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: master
          force: true
          
      - uses: crazy-max/ghaction-github-pages@v2.1.3
        with:
          # the output branch we mentioned above
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}




                                                                                                                                               

---------------------
<!-- 
  [![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=MervePolat977)](https://github.com/MervePolat977/github-readme-stats)
-->

<!--
  [![Merve's GitHub stats](https://github-readme-stats.vercel.app/api?username=MervePolat977)](https://github.com/MervePolat977/github-readme-stats)
-->

<!--
  ![Github stats 1](https://github-readme-stats.vercel.app/api?username=MervePolat977&show_icons=true&theme=gradient) 
-->






<!--
**MervePolat977/MervePolat977** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
