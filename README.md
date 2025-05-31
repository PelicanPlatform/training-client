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

In practice, by following the above instructions, you:

1. Found a data repository available via the OSDF
2. Found the Pelican URL for that data repository
3. Downloaded the corresponding object using Pelican

We'll go into more detail on each of these points to give you an introduction to the Pelican Platform.

### Exploring the OSDF

The Open Science Data Federation (OSDF) is the flagship instance of the Pelican Platform and 
serves to connect the United State's scientific data repositories to computing infrastructure.
The OSDF itself originated from the need for large-scale data movement to support distributed high throughput computing systems like the OSPool.
This eventually gave rise to the Pelican Platform, a standalone software suite to run systems like the OSDF.

With the development of Pelican, it is now even easier to connect data repositories to the OSDF. 
The webpage you visited ([osg-htc.org/services/osdf/data](http://osg-htc.org/services/osdf/data)) lists the data repositories available via the OSDF,
representing an evergrowing list of "open science" communities.
Any US-based academic, government, or non-profit institution may connect their object store to the OSDF;
this includes non-public data, so long as it is not highly regulated or sensitive (such as PII or HIPAA data).

> [!IMPORTANT]
> For more information on the OSDF, including next steps for connecting your open science data repository to the OSDF, 
> see [osg-htc.org/services/osdf](https://osg-htc.org/services/osdf).

Once a data repository is connected to the OSDF, its contents are easily accessible via the Pelican Clients that are the subject of this tutorial.\*
Every object accessible via the OSDF has a corresponding Pelican URL that exists within the single, overarching namespace of the OSDF.
This enables you, the user, to access any object in the OSDF by providing its Pelican URL, 
**without needing to know anything about the type of storage used to host the data**.
That is, the commands to interact with objects via Pelican are always the same, 
regardless of whether the data lives on POSIX, S3, or some other storage system!

\**This is technically true of any Pelican Federation; the OSDF is simply an established instance of such a Federation.*

### Anatomy of a Pelican URL

In the [Quickstart](#quickstart), the command you ran specified the location of the desired object using a Pelican URL.
The Pelican URL is a unique address to any object within the single namespace provided by a Pelican Federation.

There are four components to a Pelican URL:

* The "protocol"
* The "discovery URL"
* The "namespace prefix"
* The "object name"

These components are combined into a single string to form the Pelican URL:

```html
<protocol>://<federation_URL>/<namespace_prefix>/<object_name>
```

By examining each of these components, we can build up an understanding of how Pelican is structured.

#### The protocol

In the same way that your browser uses the `https://` protocol to interact with a website, 
Pelican uses the `pelican://` protocol to interact with a Pelican Federation.
The `pelican://` protocol is built upon the HTTP protocol and extends it with a set of metadata lookups. 
Among other things, this means Pelican can leverage the ubiquitous internet infrastructure 
- any internet-capable device can theoretically use Pelican!

> [!NOTE]
> A motivated programmer who understands HTTP could develop their own Client to interact with a Pelican Federation,
> much in the same way that they could develop a custom browser to interact with an `https://` website!

The Pelican URL is now

```html
pelican://<federation_URL>/<namespace_prefix>/<object_name>
```

#### The discovery URL

In the same way that a website is uniquely identified by its domain name, 
a Pelican Federation is uniquely identified by its discovery URL. 
To interact with a Pelican Federation, the Client needs to know the web service that it should connect to.

For example, the discovery URL for the OSDF is `osg-htc.org`, which behind-the-scenes corresponds to `https://osg-htc.org`.

> [!INFO]
> But `https://osg-htc.org` is already a website, so how does the OSDF work?
> The answer is that a website for a Pelican Federation needs to provide a specific webpage 
> that Pelican knows to look for, as part of the standards set by the `pelican://` protocol.
> For more information, see the [Core Concepts](https://docs.pelicanplatform.org/about-pelican/core-concepts#central-services) page of the Pelican documentation.

The Pelican URL is now

```html
pelican://osg-htc.org/<namespace_prefix>/<object_name>
```

#### The namespace prefix

Within a Pelican Federation, objects are grouped by a "namespace prefix",
which is often shortened to just a "namespace". 
When a data repository is connected to a Federation, 
the data provider must register a corresponding namespace prefix.
This prefix is then used in the Pelican URL as a way to communicate how to find corresponding objects via the Federation.

The person or organization that registered the namespace prefix has control over who can access the data repository via that namespace.
They also "own" all further namespace prefixes that share a common root.
For example, only the owner of the namespace prefix `ospool` has the ability to register the prefix `ospool/ap40`, `ospool/ap20`, etc.

> [!TIP]
> While the string for a namespace prefix can contain slashes `/`, each namespace prefix is distinct.
> That is, one server may provide the objects in the `ospool` namespace while another server provides the objects in the `ospool/ap40` namespace.
> The server providing `ospool/ap40`, however, must prove that it is owned by the same entity as the server providing `ospool`.

> [!INFO]
> The relationship between the data provider and a namespace prefix within a Pelican Federation is established by registering a public-private keypair. 
> Any service claiming to provide the data repository corresponding to that namespace prefix must repeatedly prove that it holds the provider's half of the keypair.
>
> * For more information on namespace prefixes, see the [Core Concepts](https://docs.pelicanplatform.org/about-pelican/core-concepts#namespace-or-federation-prefixes) page.
> * For more information on registering a namespace prefix, see the [Serving an Origin](https://docs.pelicanplatform.org/federating-your-data/origin#federation-namespace-prefix-registration) page.

For the RouteViews example used in the [Quickstart](#quickstart), the namespace prefix is just `routeviews`.
The Pelican URL is now

```html
pelican://osg-htc.org/routeviews/<object_name>
```

#### The object name

The final component to the Pelican URL is the object name.
The object name corresponds to a location within the data repository corresponding to a particular namespace. 
The object name could map to a location in a filesystem, or an object within a particular S3 bucket.
This mapping is handled by the Pelican service (the Origin) that connects the data repository to the Federation.

> [!WARNING]
> The data provider may require additional authentication to access individual objects within a namespace, 
> beyond that specified to access the namespace in the first place.
> In that case, you should communicate with the data provider to learn of the access model.

For the RouteViews example used in the [Quickstart](#quickstart), the object name is `chicago/route-views.chicago/bgpdata/2025.03/RIBS/rib.20250319.0400.bz2`.
The Pelican URL is now

```html
pelican://osg-htc.org/routeviews/chicago/route-views.chicago/bgpdata/2025.03/RIBS/rib.20250319.0400.bz2
```

> [!TIP]
> For most users, there's no need to identify where the namespace prefix ends and the object name begins.
>
> For the RouteViews example, instead of `routeviews` and `chicago/route-views.chicago/bgpdata/2025.03/RIBS/rib.20250319.0400.bz2`,
> it just as easily could have been `routeviews/chicago/route-views.chicago` and `bgpdata/2025.03/RIBS/rib.20250319.0400.bz2` for the
> namespace prefix and object name!

### Getting an object using a Pelican URL

## Accessing data using the Pelican Clients

### Basic Client actions

### Pelican CLI

#### Advanced CLI options

### PelicanFS

## Accessing data using Pelican and HTCondor

## Concluding remarks

## Appendix: Manual Setup
