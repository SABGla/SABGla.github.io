# Multimodal Interaction Group website

Please use either git command controls to push your changes or use the Web IDE here in Gitlab. This way, we can keep track of changes, and approve merge requests. 

In case you have any questions, do not hesitate to reach out to Gözel Shakeri (gozel.shakeri@glasgow.ac.uk).

Please feel free to change ANYTHING you want to. If you think something is not correct, change it. If you think the tips and tricks in this document are rubbish, change them. 

## *** Attention *** 

- Do not add any personal / sensitive / classified information in this GitLab repository! All the information here is public on the MIG server. 
- Use either git command line commands or the Web IDE here on GitLab
- Push your changes to the master branch; I trust everybody has basic git and html knowledge? 

## To do's / Error Log

- http://mig.dcs.gla.ac.uk/open-letter-shedl/
- populate projects completed before 2013
- Paddy: add project 
- 


## Adding 

### Members To GitLab

Go to MIG Website > Members (or navigate to https://git.dcs.gla.ac.uk/mig/website/-/project_members) and choose the “invite member” view, and invite (via email if person does not have a GitLab account yet). Use “Maintainer” as role as maintainers have the most permissions. 

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
			<a href="https://twitter.com/name"><i class="fab fa-twitter"></i>&nbsp;<span class="label">@name</span></a>
			<a href="https://www.linkedin.com/link"><i class="fab fa-				
			linkedin"></i>&nbsp;<span class="label">First Last</span></a>
			</div>

			<div class="col-2 col-12-medium">
				<a href="#" class="image featured" style="margin: 0 0 0 0;"><img src="http://mig.dcs.gla.ac.uk/images/people/name.png" alt="" /></a>
			</div>
		</div>
	</div>
</div>
```

### New Publication

Go to /publications/publications.html and copy paste this entry at the top of the appropriate year. 

```
<li class="mig-papers-entry"><span class="mig-papers-author">Last, F., Last, F., Last, F.</span>: <span class="mig-papers-title">Amazing Paper Title.</span> In <span class="mig-papers-publication">Amazing Venue</span>, 2021. <a class="papercite_doi" href=""><i class="fa fa-external-link papercite_doi"></i>&nbsp;Link.</a></li>
```

Make sure to update the count on total papers that year after you add your entries. 

### New Thesis

Go to /publications/theses.html and copy paste this entry at the top of the list. 

```
<li class="mig-papers-entry"><i class="fa fa-graduation-cap"></i>&nbsp;<span class="mig-papers-author">Ferguson, J.</span>: <span class="mig-papers-title">Investigating perceptual congruence between information and sensory parameters in auditory and vibrotactile displays..</span> In <span class="mig-papers-publication">PhD Thesis</span>, University of Glasgow, 2020. <a class="papercite_doi" href="http://theses.gla.ac.uk/81675/"><i class="fa fa-external-link papercite_doi"></i>&nbsp;Link.</a></li>
```

Make sure to update it accordingly. 

### New News Preview

Go to /news/news.html and copy paste this entry at the top of the list. 

```
<li>
    <span class="date">YEAR <strong>MON</strong></span>
    <h3><a href="#">TITLE</a></h3>
    <p>Blurb with <a href="#">link</a> </p>
</li>
```

Make sure to update it appropriately. If you want the preview news to point towards a dedicated news page, please see next step. 

### New News Pages

If you want to add more content to the above created news preview, please go to /news/ and copy paste the file "news_YEAR_MONTH_TEMPLATE.html" into the folder /news/. Rename the file and populate it with your news. Link the references in the preview inside of /news/news.html to the newly created news hmtl file. 

### New Theme Page

Go to /themes and copy paste "themes_TEMPLATE.html", rename appropriately, and populate with information. Then go to /themes/themes.html and add a link to the newly created theme (see file for examples); finally, go in header.html, and add a new reference to your theme page in the navigation bar. Try and make sure it's alphabetically ordered.

### New Project

Go to /projects and copy paste "projects_TEMPLATE.html", rename appropriately, and populate with information. Then go to /projects/projects.html and add a link to the newly created theme (see file for examples); finally, go in header.html, and add a new link in the navigation bar to the newly created theme.  

## Editing

### Publications

Go to /publications/publications.html and edit the file. Make sure, the count of publications is correct after doing so. If you want to add a new publication, see above. 

### Thesis

Go to /publications/theses.html and edit the file. If you want to add a new thesis, see above. 

### News Pages

Go to /news/news.html and edit the file. 

Moving "old news": if you want to move news previews to the "old news" section, please cut out the section you want to move and paste it at the top of the news list in /news/old_news.html. Make sure, you resolve references to any html files as moving the file might have broken them. 

### Themes

Make sure, the references in the file itself are correctly resolved after you've edited the page, as well as /themes/themes.html and header.html after. Try and make sure things are alphabetically ordered.

### Projects

Make sure, the references in the file itself are correctly resolved after you've edited the page, as well as in /projects/projects.htlm and header.html.

# Web Page Design

Verti by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
