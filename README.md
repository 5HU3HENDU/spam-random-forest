# spam-random-forest
Spam Detection using Random Forest Machine Learning Algorithm

<h2>Before you start</h2>
<ul>
  <li>Install Python (google it for your OS... I'm using Linux Mint)</li>
  <li><a href="https://conda.io/miniconda.html">Install Miniconda</a>, it's lighter version of Anaconda, a library used for machine learning in python. Anaconda consists of packages like numpy, scipy, pandas and many others. But in miniconda we have to install packages which we need (installing packages in miniconda is simple af, I have described it below)</li>
  <li>Head over to <a href = "https://docs.anaconda.com/anaconda/packages/pkg-docs.html">package list</a> and check out the name of package you want to install.</li>
  <li>Type <code>conda install ****</code> to install the package ****</li>
  <li>For example if you want to install numpy, scipy and sklearn then type in your command line 
    <code>$ conda install numpy</code><br>
    <code>$ conda install scipy</code><br>
    <code>$ conda install scikit-learn</code><br>
    one by one and you are good to go :)

  </li>
  
  
</ul>

<h2>Run this code using:-</h2>

<code>
$ python spamRF.py  
</code>
<p>
english.txt and english_big.txt are spam dataset.
Using these two datasets and spam.py, I've made a new dataset spam.csv which consists of 9 columns.

spamRF.py is used to apply machine learning on spam.csv.
</p>
