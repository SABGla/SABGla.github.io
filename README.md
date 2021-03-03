# Multimodal Interaction Group website

Please use either git command controls to push your changes or use the Web IDE here in Gitlab. This way, we can keep track of changes, and approve merge requests. In case you have questions, email gozel.shakeri@glasgow.ac.uk. 

## *** Attention *** 

Do not add any personal / sensitive / classified information in this GitLab repository! All the information here is public on the MIG server. 

## Adding 

### Members To GitLab

Go to https://git.dcs.gla.ac.uk/mig/website/-/project_members and choose the “invite member” view. Use “Maintainer” as role as maintainers have the most permissions, followed by the owner of the group. 

### People To Website

Go to /people.html and copy paste this entry to the end of the appropriate list (e.g. faculty, post-doc, phd student).

```
<!-- FirstName LastName -->
<div id="person-wrapper">
	<div id="person" class="personbox container">
		<div class="row">
			<div class="col-10 col-12-medium">
			
			<h2>First Last</h2>
			<p>Some blurb about the person. </p>
			<a href="mailto:fist.last@glasgow.ac.uk">first.last@glasgow.ac.uk</a></br>
			<a href="https://personal.website">https://personal.website</a></br>
			<a href="https://twitter.com/name"><i class="fab fa-twitter"></i>&nbsp;<span 				class="label">@name</span></a>
			<a href="https://www.linkedin.com/link"><i class="fab fa-				
			linkedin"></i>&nbsp;<span class="label">First Last</span></a>
			</div>

			<div class="col-2 col-12-medium">
				<a href="#" class="image featured" style="margin: 0 0 0 0;"><img 						src="http://mig.dcs.gla.ac.uk/images/people/name.png" alt="" /></a>
			</div>
		</div>
	</div>
</div>
```

### New Publication

Go to /publications/publications.html and copy paste this entry at the top of the appropriate year. 

```
<li class="mig-papers-entry"><span class="mig-papers-author">Last, F., Last, F., Last, F.</span>: <span class="mig-papers-title">Amazing Paper Title.</span> In <span class="mig-papers-publication">Amazing Venue</span>, 2021.</li>
```

Make sure to update the count on total papers that year after you add your entries. 

### New Thesis

Go to /publications/theses.html and copy paste this entry at the top of the list. 

```
<li class="mig-papers-entry"><i class="fa fa-graduation-cap"></i>&nbsp;<span class="mig-papers-author">Ferguson, J.</span>: <span class="mig-papers-title">Investigating perceptual congruence between information and sensory parameters in auditory and vibrotactile displays..</span> In <span class="mig-papers-publication">PhD Thesis</span>, University of Glasgow, 2020. <a class="papercite_doi" href="http://theses.gla.ac.uk/81675/"><i class="fa fa-external-link papercite_doi"></i>&nbsp;Link.</a></li>
```

Make sure to update it accordingly. 

### New News

Go to /news/news.html and copy paste this entry at the top of the list. 

```
<li>
    <span class="date">YEAR <strong>MON</strong></span>
    <h3><a href="#">TITLE</a></h3>
    <p>Blurb with <a href="#">link</a> </p>
</li>
```

Make sure to update it appropriately. 

### New News Pages

If you want to add a new page, please go to news/ and copy paste the file "news_YEAR_MONTH_TEMPLATE.html" into the folder /news. Rename the file and populate it with your news. 

### New Theme Page

Go to /themes and copy paste "themes_TEMPLATE.html", rename appropriately, and populate with information. Then go to /themes/themes.html and add a link to the newly created theme (see file for examples); finally, go in header.html, and add a new link in the navigation bar to the newly created theme.  

### New Project

Go to /projects and copy paste "projects_TEMPLATE.html", rename appropriately, and populate with information. Then go to /projects/projects.html and add a link to the newly created theme (see file for examples); finally, go in header.html, and add a new link in the navigation bar to the newly created theme.  

## Editing

### Publications

### Thesis

### News Pages

### Themes

### Projects

##Structure of Webpages

The internal structure is based on the website navigation structure. 

Root
    • index.html
    • news
        - news.html
        - … 
        - news_TEMPLATE.html
    • people.html
    • publications
        - publications.html
        - theses.html
    • projects 
        - projects.html 			
        - projects_completed.html 
        - completed
            - projects_abbi.html
            - …
        - projects_viajero.html
        - …
        - projects_TEMPLATE.html
    • themes
        - themes.html
        - themes_sustainable_food_interaction.html
        - …
        - themes_TEMPLATE.html
    • images
        - news
        - people
        - projects
        - themes



Verti by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)


A super simple + modern responsive website template. Took a slightly different direction
on the mobile version's slide out nav (floating button versus a full on titlebar).

Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.

(* = Not included)

Feedback, bug reports, and comments are not only welcome, but strongly encouraged :)

AJ
aj@lkn.io | @ajlkn


Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Responsive Tools (github.com/ajlkn/responsive-tools)
