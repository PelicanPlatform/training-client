# HTC25 Pelican Client Tutorial

This branch of the repository contains the materials that will be used for the session ["Use Your Data Anywhere"](https://agenda.hep.wisc.edu/event/2297/contributions/33938/) of [HTC25](https://agenda.hep.wisc.edu/event/2297/), on Jun. 4, 2025.

Clients covered:
* [Pelican CLI](https://docs.pelicanplatform.org/getting-data-with-pelican/client)
* [PelicanFS](https://github.com/PelicanPlatform/pelicanfs)
* [HTCondor Plugin](https://htcondor.readthedocs.io/en/latest/users-manual/file-transfer.html#file-transfer-using-a-url)

**Accompanying Slides**: [link TBD]

## Requirements

An internet connection and a web browser!

## Setup

For this tutorial, we recommend that you use a Guest [OSPool Notebook](https://portal.osg-htc.org/documentation/overview/test-drive-ospool/) as it satisfies the necessary requirements.
Abbreviated instructions are provided below.
Alternatively, follow the instructions in [Appendix: Manual Setup](#appendix-manual-setup) to setup a device of your choice.

### Log in to a Guest OSPool Notebook

Screenshots of this process are included in the Accompanying Slides.

1. Go to [notebook.ospool.osg-htc.org](https://notebook.ospool.osg-htc.org).
2. Click on the "Sign in with CILogon" button.
3. Select your identity provider and click the "Log On" button. *Note: "social" logins are not enabled!*
4. Sign in to your identity provider.
5. If given a choice of "Server Options", select "Guest Account: Explore OSPool Notebooks", then click the "Start" button.
6. Wait for server to start. Your browser should load a JupyterLab instance and display a "Launcher" tab.
7. Under the "Other" category, launch the "Terminal" tab.

## Quickstart

After completing the above setup, you're ready to download data using Pelican! 
First, follow the instructions below; we'll go into more detail later.

1. In a new browser, go to [osg-htc.org/services/osdf/data](http://osg-htc.org/services/osdf/data).
2. Choose an entry from the table of available repositories (a good default choice is the "RouteViews" repository).
3. Click on the row for the desired entry (but not on the button "View Datasets" or "Dataset Catalog" on the far right!).
4. In the pop-up window, look for the "Download a Public Object" section.
5. Copy the example command text shown under "With Pelican Client on the Command Line". The example command for the RouteViews repository is this:

   ```
   pelican object get osdf:///routeviews/chicago/route-views.chicago/bgpdata/2025.03/RIBS/rib.20250319.0400.bz2 ./
   ```
   
7. In the "Terminal" tab of your OSPool Notebook, paste and run the command you copied.
8. Run the command `ls -lh` to confirm the object was downloaded. For the RouteViews example, you should see something like this:

  ```
  (base) jovyan:~$ ls -lh
  total 73M
  -rw-r--r-- 1 jovyan users  73M May 30 20:35 rib.20250319.0400.bz2
  drwxr-sr-x 7 jovyan users  184 May 30 20:30 tutorial-fastqc
  drwxr-sr-x 8 jovyan users 4.0K May 30 20:30 tutorial-osdf-noaa
  drwxr-sr-x 9 jovyan users 4.0K May 30 20:30 tutorial-r-noaa
  drwsrwsr-x 1 jovyan users   60 May 30 20:30 work
  ```

**🎉 Congratulations! You've downloaded data using the Pelican Platform. 🎉**

## What did you do? (An introduction to the Pelican Platform)

### Exploring the OSDF

### Anatomy of a Pelican URL

### Getting an object using a Pelican URL

## Accessing data using the Pelican Clients

### Basic Client actions

### Pelican CLI

#### Advanced CLI options

### PelicanFS

## Accessing data using Pelican and HTCondor

## Concluding remarks

## Appendix: Manual Setup
