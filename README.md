# NetworksFinalProject

Contributors:  Amanda Bris, Alexandria Mullen, Matthew Preston, Matthew Spana






Modelling & Predicting International Migration Trends

Amanda Bris | bris@bc.edu
Alexandria Mullen | mullenad@bc.edu
Matthew Preston | prestomb@bc.edu
Matthew Spana | spanam@bc.edu


Topics in CS: Introduction to Network Science, Boston College




















February 19, 2020
Table of Contents




Abstract	3
Concrete Problem Statement	3
Potential Challenges	4
Timeline & Milestones	5
Works Cited	6




























Abstract
International flows of migration have historically affected the social, political and economic climate of every nation-state.  Recent developments in global trade, transport and technology have connected the world in an unprecedented manner.  As such, it follows that migration and movement of people is becoming an increasingly important phenomenon to understand.  Despite efforts by non-governmental bodies such as the United Nations to provide clear guidelines on how to measure migration, much of the information available is inaccurate, hard-to-understand and scarce.  Our goal is to first: display migration patterns of the past with the best available data, and second: use machine learning algorithms to predict international migration patterns, then display this information through visual and statistical representations.

Our project is based on data from the United Nations’ Department of Economic and Social Affairs, Population Division on international migrant stock.  This dataset provides information on inflows and outflows of migrants by country of origin and destination from 2012 to the present.

Our project will use matplotlib basemap toolkit in order to visualize inflows and outflows of migration by country, including our predictions for future years.  Basemap is a library for plotting 2D data on maps in Python.  It provides the facilities to transform coordinates to one of 25 different map projections (using the PROJ.4 C library).  Matplotlib is then used to plot contours, images, vectors, lines or points in the transformed coordinates.

Furthermore, our project will utilize machine learning algorithms using the data to predict migration patterns every year up to the next ten years.  Using two models, (Multiple) Linear Regression and K-Nearest Neighbor (KNN), we will predict the change in each ‘flow’ from and to each country, or each edge on our graph.  Our code will be written in Python, using the built-in library Scikit-learn (sklearn).  A stretch goal is to utilize our own, modified algorithms of Linear Regression and KNN.

Concrete Problem Statement
Our interest in this project is based on the potential use for our described program and the importance of the topic in the modern world.  For better or for worse, immigration has been a political issue in the past years, even to the extent of being the defining issue of the United States 2016 Presidential Election.  Our project could be used as a resource for informing both governments and citizens on this issue.  Accurate, reliable data and data visualization regarding international flows of migration is needed in order for governments to know the migration patterns of their own citizens, and that of foreigners coming into their country.  This knowledge will enable governments and policymakers to effectively plan integration programs, recruit specialized workers and adopt policies to address internal or external migration.

Migration patterns can tell us about the state of a country.  States experiencing large influxes in migration tend to have a higher quality of life compared to their neighbors and adopt a more open immigration policy.  Conversely, countries experiencing high external migration might be experiencing conflict, disease, natural disaster or overall poor quality of life.  Looking at migration does not only tell us about where people are going to or coming from, it also exposes patterns reflecting the push and pull factors of a country.

Furthermore, our project has the potential to become a product if we allow custom input data into the software, which will be at the basis of the visualization.  This will allow us to create a product for migration data not just for the timeframe we have access to, but for the future as well.  

With all this in mind, an itemized list of our goals would contain the following.  For the construction of our initial demonstration, we would like to implement: generic map data visualization, predictions based on multiple linear regression with the sklearn library, predictions based on KNN with the sklearn library, backend data parsing and data visualization of the predictions.  For the construction of the final project we would like to implement dataset hotswitch, multiple linear regression with tailored algorithms and KNN with tailored algorithms.

Potential Challenges
In constructing our visualization and prediction of migrant flow, we will be confronted with challenges such as determining the best data source to use, obtaining a sufficient amount of data on developing countries, ensuring the data is up to date, learning how to use Python libraries for data visualization, and making the most accurate predictions possible through our machine learning model.  

Additionally, the prediction model will be challenging due to the size of the dataset we have access to.  On one hand, the dataset provides extremely detailed information for every country.  However, this data only extends to 2012, and our goal is to predict migration trends for the next 10 years.  This might present limitations in the accuracy of our model, as well as the complications of working with such a large breadth but relatively smaller depth of the dataset.  

Timeline & Milestones 

Date
Task 
March 13
Construction of initial demo:
Linear Regression with Sklearn Library
KNN with Sklearn Library
Generic Map Data Visualization
Backend Data Parsing
Prediction Data Visualization






March 20 
Midterm Report:
Present Demonstration

April 17
Construction of Final Project:
Dataset Hotswitch
Linear Regression with Modified Algorithms
KNN with Modified Algorithms



April 24
Final Project Presentation and Report
Final Demonstration

Works Cited

United Nations, Department of Economic and Social Affairs, Population Division.  (2017). Trends in International Migrant Stock: The 2017 Revision. United Nations database, POP/DB/MIG/Stock/Rev.2017.  https://www.un.org/en/development/desa/population/migration/data/estimates2017/estimates17.asp 

(Summary: Presents estimated international migrant stock for years 1990, 1995, 2000, 2005, 2010, 2015 and 2017. Will serve as a primary data set for our analysis and visualization.)

United Nations, Department of Economic and Social Affairs. (2017). International Migration Report 2017 Highlights (ST/ESA/SER.A/404). United Nations. https://www.un.org/en/development/desa/population/migration/publications/migrationreport/docs/MigrationReport2017_Highlights.pdf

(Summary: Comprehensive report of current world events and general factors that influence migration patterns and practices, released biennially. Updated for calendar year 2017.)

United Nations, Department of Economic and Social Affairs, Population Division. (2019). International Migration 2019 Report (ST/ESA/SER.A/438). United Nations. https://www.un.org/en/development/desa/population/migration/publications/migrationreport/docs/MigrationReport2019_Highlights.pdf

(Summary: Comprehensive report of current world events and general factors that influence migration patterns and practices, released biennially. Updated for calendar year 2019.)

Migration Policy Institute. (2017). Immigrant and Emigrant Populations by Country of Origin and Destination. Migration Policy Institute (MPI) Data Hub. https://www.migrationpolicy.org/programs/data-hub/charts/immigrant-and-emigrant-populations-country-origin-and-destination?width=1000&height=850&iframe=true

(Summary: Dataset containing immigrant and emigrant populations by country of origin. Will serve as an additional dataset for our visualization and predictions.)



Hawkins, Ed. (2017). Connection Map. The Python Graph Gallery. https://python-graph-gallery.com/connection-map/

(Summary: Provides framework for world-map connections. Will be integral for the development of our visualization component.)

Mode Analytics Inc. (2020). SQL + Python + R.  All in one environment. Mode. https://mode.com/notebooks/?utm_source=google&utm_medium=cpc&utm_campaign=g_nam_dg_search_generic_python&utm_term=python%20data%20visualization&utm_content=python_data_visualization&utm_adgroup=84793374859&device=c&gclid=EAIaIQobChMI--2Q_v3E5wIVx5-zCh3TCQsREAAYAyAAEgKlPvD_BwE

(Summary: Provides a structural framework for a comprehensive integration of our backend and frontend aspects.)

Bijwaard, Govert E. (2008). Modeling Migration Dynamics of Immigrants. Erasmus University Rotterdam, and Tinbergen Institute. https://papers.tinbergen.nl/08070.pdf

(Summary: Provides insight into migration predictions from a demographic point of view.  Emphasizes prediction of individual likelihood to remain in the migrated country, contrasted to our macro-focused approach of flow dynamics.)

Carammia, Marcello & Dumont, Jean-Christophe. (May 2018). Can we anticipate future migration flows? Organisation for Economic Co-operation and Development (OECD). https://www.oecd.org/els/mig/migration-policy-debate-16.pdf

(Summary: Explores the viability of predicting migration flows over time, and general feasibility of current approaches.  Serves as comparison and contrast to our methods.)

OECD.Stat. (2018). International Migration Database. OECD. https://stats.oecd.org/Index.aspx?DataSetCode=MIG

(Summary: A comprehensive dataset for prediction algorithms to run on.  Includes general migration inflow and outflow, asylum-seeker inflow, and current foreign-born populations and labor forces, amongst others.)



Pison, Gilles. (13 March 2019). Which countries have the most immigrants? World Economic Forum. https://www.weforum.org/agenda/2019/03/which-countries-have-the-most-immigrants-51048ff1f9/

(Summary: Provides an understanding of immigrant makeup of various countries, a useful set of complementary information for comparison to immigrant flow.)

Author, de Haas, Hein. Author, Czaika, Mathias. Author, Flahaux, Marie‐Laurence. Author, Mahendra, Edo. Author, Natter, Katharina. Author, Vezzoli, Simona. & Author, Villares‐Varela, María. (8 October 2019). International Migration: Trends, Determinants, and Policy Effects. Population and Development Review, volume 45 (No.  4). https://doi.org/10.1111/padr.12291 

(Summary: A general understanding on current thoughts regarding migration.  Provides context for the predictive work we are accomplishing.)

-----------------------------------------------------------------------------------------------------
