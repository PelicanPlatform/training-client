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

In principle, you can install the necessary programs on your own device to complete the exercises.
If you are interested in doing that, we recommend that you first go through the tutorial using the OSPool Notebook as recommended,
then repeat the tutorial after installing the necessary programs on the device of your choice.

### Log in to a Guest OSPool Notebook

Screenshots of this process are included in the Accompanying Slides.

1. Go to [notebook.ospool.osg-htc.org](https://notebook.ospool.osg-htc.org).
2. Click on the "Sign in with CILogon" button.
3. Select your identity provider and click the "Log On" button. *Note: "social" logins are not enabled!*
4. Sign in to your identity provider.
5. If given a choice of "Server Options", select "Guest Account: Explore OSPool Notebooks", then click the "Start" button.
6. Wait for server to start. Your browser should load a JupyterLab instance and display a "Launcher" tab.
7. In the file navigation pane on the left-hand side, double click on the `training-client` directory to navigate to it.
8. In the "Launcher" tab, under the "Other" category, double click the "Terminal" box to launch a shell console.

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

> [!NOTE]
> But `https://osg-htc.org` is already a website, so how does the OSDF work?
> The answer is that a website for a Pelican Federation needs to provide a specific webpage 
> that Pelican knows to look for, as part of the standards set by the `pelican://` protocol.
> For more information, see the [Core Concepts](https://docs.pelicanplatform.org/about-pelican/core-concepts#central-services) page of the Pelican documentation.

The Pelican URL is now

```html
pelican://osg-htc.org/<namespace_prefix>/<object_name>
```

> [!TIP]
> Because `osg-htc.org` is the discovery URL for Pelican's flagship instance, the OSDF,
> most Pelican URLs begin with `pelican://osg-htc.org/`.
> To make the URL faster to type, Pelican has a built-in shortcut for this phrase:
> `osdf:///`.
> That is, the following are equivalent:
> 
> ```html
> pelican://osg-htc.org/<namespace_prefix>/<object_name>
> osdf:///<namespace_prefix>/<object_name>
> ```
>

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

> [!NOTE]
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

Before we discuss the details of how to use the Pelican Clients to interact with an object via its Pelican URL, 
we need to discuss the mechanics of how Pelican transfers an object via a Federation.
We'll focus on the "get" operation, as that is the most frequently used operation by Pelican Clients.
To do so, we need to introduce a couple more components of a Pelican Federation.

* **Origin**: The Origin service connects a data repository to a Pelican Federation.
  Controlled by the data provider, the Origin maps the objects into a corresponding namespace prefix
  and defines the necessary permissions required to access the objects.

* **Central Services**: These services keep track of the namespaces and the corresponding Origins available
  within a Pelican Federation. When a Pelican component wants to interact with a namespace, 
  it asks the Central Services for the Origin that it should connect to.

* **Cache**: The Cache server is used as the middle-man for most object transfers within a Federation.
  It keeps temporary copies of the most recently transferred objects and those objects can be downloaded
  by other Pelican components.
  Importantly, the Cache respects the access permissions as defined by the namespace for that Origin.
  ***Only an entity with permission to access an object at the Origin can access the object at the Cache!***
  
#### Connecting to a Cache

When a Client wants to get an object, it must first connect to a Cache.

1. The Client asks the Central Services which Cache it should connect to.
2. The Central Services gives the Client a list of three Caches that are capable of obtaining objects from the corresponding namespace.
3. The Client then requests the object from one of the Caches on the list.
4. If that Cache cannot provide the object, the Client continues through the list until it obtains the object.
5. If the Client does not obtain the object, it errors out.

When the Client requests an object from a Cache, then either a) the Cache has the object, or b) the Cache does not have the object.

#### a) The Cache has the object

If the Cache has a copy of an object requested by a Client, then

1. The Cache first checks to make sure that the Client satisfies the requirements for interacting with that object.
   (These requirements are copied from the Origin through which the Cache originally copied said object.)
2. If the Client satisfies the requirements, the Cache grants the Client's request to download the object.
3. If not, the Cache rejects the Client's request.

#### b) The Cache does not have the object

If the Cache does not have a copy of an object requested by a Client, then

1. The Cache asks the Central Services for the Origin corresponding to the requested object's namespace.
2. The Central Services redirects the Cache to the proper Origin.
3. The Cache requests the object via the Origin, on behalf of the Client.
4. If the Client satisfies the Origin's requirements, the Cache downloads a copy of the object and subsequently the Client downloads the object from the cache.
5. If the Client does not satisfy the Origin's requirements, the Cache's request is rejected and in turn the Cache rejects the Client's request.

#### The importance of caching

At this point, you may be wondering "why should I care about any of this?".
And for most users of the Pelican Clients, you don't really need to know the implementation of how Pelican delivers an object.

What you *do* need to know, however, are the consequences of the implementation.

* **Pelican assumes that objects *do not change*!**

  For the caching system described above to work properly, the object must be the same at the Cache as it is in data repository connected to the Origin.
  Consider if the object accessible via the Origin changes: 
  a Client requesting that object may get an old copy from the Cache,
  or it may get the new version via the Origin.

> [!CAUTION]
> Because of some technical details, the Client may even get a Frankenstein mix of the old and new version. 😬
> If you make a change to an object in the repository connected to an Origin, you should also change its name!

* **Requirements for accessing objects are respected *everywhere* in the Federation**

  When a Cache downloads an object via an Origin, it also gets a copy of the Origin's requirements for accessing that object.
  That way, if the Origin would reject a Client's request, so to will the Cache reject that same Client's request.
  *The data provider does not lose control over their data!*

* **Caches help prevent the data repository from being overwhelmed**

  Because it is expensive to store open science data repositories on high-performance hardware,
  most open science storage systems can be overwhelmed by large transfers, many transfers, and especially by many large transfers.
  Often the data provider sets limits on the amount and frequency of data transfers from their system.
  By using Caches, transfers via a Pelican Federation reduce the amount and frequency of data transfers from the original repository,
  making it easier for researchers to access the data, especially for high throughput workflows.

> [!IMPORTANT]
> The OSDF maintains over 30 Caches geographically distributed across North America and Europe, 
> most of which are high-performance servers located on the Internet2 backbone.
> This extensive caching is a major incentive for data providers to connect their open science data repositories to the OSDF.
> For more information on connecting data to the OSDF, see [osg-htc.org/services/osdf](https://osg-htc.org/services/osdf).

## Accessing data using the Pelican Clients

The primary way of interacting with data via a Pelican Federation is via a Pelican Client.
A Pelican Client is simply a program that understands how to make requests of a Pelican Federation via the `pelican://` protocol.
Currently, Pelican provides three Clients, which we will discuss today:

* Pelican CLI Client (shell-based)
* PelicanFS Client (Python-based)
* Pelican Plugin (HTCondor integration)

Additional Clients are targeted for development by the Pelican team.
And, in principle, anyone can develop their own Pelican Client based on the `pelican://` protocol.

### Basic Client requests

There are commands common to every Client.
Each command corresponds to a request that the Client makes to the Federation, usually tied to a specific Pelican URL.
The most common request by far is the `get` request.

| Command | Request |
| ------- | ------ |
| `ls` | List the objects accessible via a Pelican URL |
| `get` | Download object(s) via a Pelican URL |
| `put` | Upload object(s) via a Pelican URL |

A request may be granted or rejected, depending on the access rules defined for the corresponding namespace.
The data provider for a namespace decides which "capabilities" are enabled for their namespace.

Most "publicly accessible" namespaces enable the "Listings" and "PublicReads" capabilities, 
which means that the Federation will grant an `ls` or `get` request made by *any* Pelican Client.
Some namespaces may require that `get` requests provide a valid authorization token to be granted and in that case, the same applies to `ls` requests.

> [!IMPORTANT]
> All `put` requests *must* provide a valid authorization token, regardless of the namespace.
> As such, we will not be covering `put` requests in today's training.
> For more information on authorizing Client requests, including `put`, see the [Pelican documentation](https://docs.pelicanplatform.org/getting-data-with-pelican/client#get-a-protected-object-from-your-federation).

### Pelican CLI

The Pelican Command Line Interface, or Pelican CLI, is the general purpose Client for interacting with Pelican Federations.
The Pelican CLI is available as a standalone binary that does not require admin permissions to install.
Together with its support for Linux, macOS, and Windows operating systems, the Pelican CLI is widely accessible.

To install the Pelican CLI on your own device, follow the instructions at [docs.pelicanplatform.org/install](https://docs.pelicanplatform.org/install) for your operating system.
If you are using a Linux operating system, you can quickly install the Pelican CLI following the [instructions here](https://docs.pelicanplatform.org/install/linux-binary).

> [!TIP]
> During today's tutorial, we recommend that you continue to use the OSPool Notebook, which comes with the Pelican CLI pre-installed.
> In principle, however, the following exercises should work wherever the Pelican CLI is installed.

Once installed, you can use the Pelican CLI by using the `pelican` noun-verb commands.
For the requests listed above, you need to use the `object` noun.
That is, the commands you'll be entering will take the form

```
pelican object <request> <additonal arguments>
```

where the `additional arguments` usually involves a Pelican URL.

> [!NOTE]
> There are other nouns besides the `object` noun for the `pelican` command, 
> which in principle can be used to interact with specific components of a Pelican Federation, and even launch your own Pelican Federation,
> but those are beyond the scope of today's training!

#### Listing objects with the Pelican CLI

To list the objects accessible via a particular namespace, use the `ls` verb and provide the Pelican URL for the desired namespace:

```
pelican object ls <Pelican URL>
```

Pelican maintains a test namespace within the OSDF under the namespace `pelicanplatform/test`.
Since the Federation URL for the OSDF is `osg-htc.org`, that leads to the Pelican URL `pelican://osg-htc.org/pelicanplatform/test`.

The command to list the objects accessible via this Pelican URL is

```
pelican object ls pelican://osg-htc.org/pelicanplatform/test
```

The output of running this command should look like this:

```
$ pelican object ls pelican://osg-htc.org/pelicanplatform/test
hello-world.txt.md5          hello-world.txt
```

> [!TIP]
> Instead of using the full OSDF Pelican URL, you can use the `osdf://` shorthand, like this:
> 
> ```
> pelican object ls osdf:///pelicanplatform/test
> ```
>
> This is exactly equivalent to the command used above.

For additional information, you include the `-l`/`--long` flag:

```
pelican object ls --long pelican://osg-htc.org/pelicanplatform/test
```

which should show something like

```
/pelicanplatform/test/hello-world.txt.md5          50          2025-01-21 20:59:49
/pelicanplatform/test/hello-world.txt              76          2025-01-21 20:57:01
```

> [!TIP]
> Again, you can use the `osdf://` shorthand for specifying the Pelican URL:
>
> ```
> pelican object ls --long osdf:///pelicanplatform/test
> ```
>
> In general, anywhere you see `pelican://osg-htc.org/` you can replace it with `osdf:///`!

#### Getting objects with the Pelican CLI

To get an object using the Pelican CLI, you need to provide the Pelican URL for the desired object and the location/name of where to store the object locally:

```
pelican object get <Pelican URL> <local destination>
```

In the listing of the Pelican test namespace, we saw the object `hello-world.txt`. 
Let's download that object to the current directory:

```
pelican object get pelican://osg-htc.org/pelicanplatform/test/hello-world.txt ./hello-world.txt
```

If the request to download the object is granted, the Client will start downloading the object.
If that download takes more than a few seconds, you may see a progress bar displayed.

If the command runs successfully, there will be a new file in your current directory called `hello-world.txt`.
If you look at the contents of the file, you should see the following:

```
$ cat hello-world.txt
If you are seeing this message, getting an object from OSDF was successful.
```

#### Getting objects recursively with the Pelican CLI

What if you wanted to download all of the objects in the `/pelicanplatform/test` namespace? 
If there are only a couple of objects, you could use the `pelican object ls` command to list the object names, 
then run the corresponding `pelican object get` commands.
But for more than a few items, this becomes tedious.

Pelican utilizes the URL query syntax in Pelican URLs to modify its behavior.
For this case, you can use the `?recursive` query to tell Pelican to act recursively on the provided Pelican URL.
For example,

```
pelican object get pelican://osg-htc.org/pelicanplatform/test?recursive ./
```

will download the objects of the `/pelicanplatform/test` namespace into a local directory named `test` (the basename of the Pelican URL).
If you look in that directory, you should see the two files corresponding to the two objects accessible from that namespace.

```
$ ls test
hello-world.txt  hello-world.txt.md5
```

> [!TIP]
> Another frequently used query is `?pack=auto`.
> When getting a compressed object, this query tells the Pelican Client to automatically decompress the object during download.
> Similarly, when uploading an object, the query tells the Pelican Client to automatically compress the object during upload.
>
> For more information on the queries that Pelican employs, see [this documentation page](https://docs.pelicanplatform.org/getting-data-with-pelican/client#utilizing-queries-with-your-url).

#### [Optional] A peak behind the curtain..

In the [What did you do?](#what-did-you-do-an-introduction-to-the-pelican-platform) section, 
we described how Pelican and the `pelican://` protocol are based on the HTTP protocol.
If you want to see what that looks like in practice, you can run any of the above CLI commands with the `-d` or `--debug` flag.
For example:

```
pelican object get --debug pelican://osg-htc.org/pelicanplatform/test/hello-world.txt ./
```

The output of this command will include details about the information that the Client is requesting, 
and to what components of the Pelican Federation the Client is talking to.

> [!TIP]
> For insight into the HTTP queries being made by the Client, see [the FAQ page](https://docs.pelicanplatform.org/faq#how-can-i-tell-what-services-my-pelican-client-will-talk-to-before-i-try-to-getput-objects). 

### PelicanFS

Pelican provides the Python package `pelicanfs`, which enables the transfer of objects via the `pelican://` protocol from inside of Python.

> [!NOTE]
> The `pelicanfs` package is an implementation of the [`fsspec` package](https://filesystem-spec.readthedocs.io/en/latest/), which provides a Pythonic interface to filesystems.
> Since Pelican is not a filesystem, however, not all features of the `fsspec` package are available in the `pelicanfs` package.

The `pelicanfs` package can be installed via `pip`, i.e.,

```bash
python3 -m pip install pelicanfs
```

> [!TIP]
> During today's tutorial, we recommend that you continue to use the OSPool Notebook, which comes with the `pelicanfs` package pre-installed.
> In principle, however, the following exercises should work wherever the Pelican CLI is installed.

Once installed, you can use the package within a Python script or in a Python console.
For the following exercises, launch a Python console by entering

```bash
python3
```

or by launching the Python console via the Jupyter launcher in the OSPool Notebook.

#### Manual import and setup of `pelicanfs`

The main method for using `pelicanfs` is to use the `PelicanFileSystem` class.
First, import this from `pelicanfs` as follows:

```python
from pelicanfs.core import PelicanFileSystem
```

Next, instantiate the an object of the class for a particular Federation.
For this example, we'll continue using the OSDF Federation, which has the Federation URL of `osg-htc.org`:

```python
pelfs = PelicanFileSystem('pelican://osg-htc.org')
```

The `pelfs` object has methods for interacting with objects via the Federation.
Usage typically looks like

```python
pelfs.<method>('<namespace_prefix>/<object_name>')
```

#### Listing objects with PelicanFS

Again, we'll be working with the Pelican test namespace in the OSDF at `/pelicanplatform/test`.
To list the objects associated with this namespace using `pelicanfs`, use the `ls` method of the `pelfs` object we instantiated above:

```python
ls_results = pelfs.ls('/pelicanplatform/test')
```

This command returns a list of dictionaries with the details of the objects that are connected via the `/pelicanplatform/test` namespace.

```python
>>> print(ls_results)
[{'name': '/pelicanplatform/test/hello-world.txt.md5', 'size': None, 'type': 'file'}, {'name': '/pelicanplatform/test/hello-world.txt', 'size': None, 'type': 'file'}]
```

If you just want the names of the objects:

```python
>>> print([i['name'] for i in ls_results])
['/pelicanplatform/test/hello-world.txt.md5', '/pelicanplatform/test/hello-world.txt']
```

> [!NOTE]
> The `pelicanfs` package is still relatively new and not all features available in the Pelican CLI are available in the `pelicanfs` package.
> In this case, the object `size` is not currently available.

#### Getting objects with PelicanFS

Let's download the `hello-world.txt` object using PelicanFS.
To do so, you'll use the `get_file` method:

```python
pelfs.get_file('/pelicanplatform/test/hello-world.txt', 'hello-world.txt')
```

This will download the object and save it as the file `hello-world.txt` in the local directory.

> [!TIP]
> Normally, the method you would use is the `get` method, not the `get_file` method,
> but there is currently a bug that prevents the `get` method from working correctly.

Once the object is downloaded, you can open it as usual:

```python
with open('hello-world.txt', 'r') as f:
    my_file = f.read()

print(my_file)
```

BUT, an advantage of the `fsspec` implementation is that you don't need a discrete download step!
You can combine the above steps using the `open` method of the `PelicanFileSystem` object:

```python
with pelfs.open('/pelicanplatform/test/hello-world.txt', 'r') as f:
    direct_read = f.read()

print(direct_read)
```

Behind the scenes, `pelicanfs` will download the object as needed, and `fsspec` will choose an appropriate method for storing it locally.

#### Automated use of `pelicanfs`

Many Python packages work with `fsspec` automatically, which in turn means that they can work with `pelicanfs` automatically.
That means that you don't necessarily have to manually invoke `pelicanfs` to use it!

As an example, let's read in a csv file from a NOAA dataset available via the OSDF from the AWS OpenData repository.
(More on this dataset in the [Accessing data using Pelican and HTCondor](#accessing-data-using-pelican-and-htcondor).)

To see how this works, **first exit and restart your Python console**.
Then import the Pandas package:

```python
import pandas as pd
```

Next, you'll need the Pelican URL. 
The Pelican URL for this csv file is

```python
station_URL='osdf:///aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/USW00014837.csv'
```

Now, you can load this data file into a Pandas dataframe using this URL and the usual Pandas method:

```python
station_df = pd.read_csv(station_URL, low_memory=False)
```

The data is automatically downloaded using the `pelicanfs` package, even though you didn't import it!
To confirm the data is there, use the `head` method on the new dataframe:

```python
station_df.head()
```

You should see the following:

```python
>>> station_df.head()
            ID      DATE ELEMENT  DATA_VALUE M_FLAG Q_FLAG S_FLAG  OBS_TIME
0  USW00014837  19391001    TMAX         194    NaN    NaN      X       NaN
1  USW00014837  19391002    TMAX         211    NaN    NaN      X       NaN
2  USW00014837  19391003    TMAX         233    NaN    NaN      X       NaN
3  USW00014837  19391004    TMAX         272    NaN    NaN      X       NaN
4  USW00014837  19391005    TMAX         211    NaN    NaN      X       NaN
```

## Accessing data using Pelican and HTCondor

The real power of Pelican is the ability to provide data to high throughput computing.
To demonstrate this, we'll use HTCondor to do a rudimentary analysis of multiple objects of the [NOAA Global Historical Climatology Network](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html) dataset.

Before proceeding, move into the `htcondor-plugin` directory.
If you still have your terminal window open, you will need to enter

```bash
cd htcondor-plugin
```

### About the data

From the [README](https://docs.opendata.aws/noaa-ghcn-pds/readme.html):

> GHCN-Daily is a dataset that contains daily observations over global land areas.
> It contains station-based measurements from land-based stations worldwide, about two thirds of which are for precipitation measurements only (Menne et al., 2012).
> GHCN-Daily is a composite of climate records from numerous sources that were merged together and subjected to a common suite of quality assurance reviews (Durre et al., 2010).

The GHCN data set is available via Amazon's OpenData repository, at [https://noaa-ghcn-pds.s3.amazonaws.com/](https://noaa-ghcn-pds.s3.amazonaws.com/).
The OpenData repository is already connected to the OSDF under the namespace `aws-opendata`. 
With a little digging, we find that the NOAA dataset is accessible via `us-east-1/noaa-ghcn-pds`.
Altogether, our starting Pelican URL is `pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds`.

Next, we need an object to work with. 
Normally, we would use the `ls` functionality discussed above to see the objects accessible via this namespace, but listings are not enabled for this namespace.
Instead, you can browse the [AWS index link](https://noaa-ghcn-pds.s3.amazonaws.com/) to see the files available.

In the top level of the namespace is a `ghcnd-stations.txt` file that serves as an index of the station names, locations, and identifiers.
We can use this file to identify the stations of interest.
The Pelican URL for this object is `pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/ghcnd-stations.txt`.

Further exploration of the AWS index shows that the data for individual stations follow the naming of `csv/by_station/<stationID>.csv`,
so the Pelican URLs for indvidual csv files are `pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/<stationID>.csv`.

### Exploring the data

For this portion, we'll use the Pelican CLI to explore the data, but in principle you can use the PelicanFS Client to accomplish the same thing.

First, download a copy of the index file:

```
pelican object get pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/ghcnd-stations.txt ./ghcnd-stations.txt
```

Take a peak at the contents of the file:

```bash
head ghcnd-stations.txt
```

You should see something like this:

```
$ head ghcnd-stations.txt
ACW00011604  17.1167  -61.7833   10.1    ST JOHNS COOLIDGE FLD
ACW00011647  17.1333  -61.7833   19.2    ST JOHNS
AE000041196  25.3330   55.5170   34.0    SHARJAH INTER. AIRP            GSN     41196
AEM00041194  25.2550   55.3640   10.4    DUBAI INTL                             41194
AEM00041217  24.4330   54.6510   26.8    ABU DHABI INTL                         41217
AEM00041218  24.2620   55.6090  264.9    AL AIN INTL                            41218
AF000040930  35.3170   69.0170 3366.0    NORTH-SALANG                   GSN     40930
AFM00040938  34.2100   62.2280  977.2    HERAT                                  40938
AFM00040948  34.5660   69.2120 1791.3    KABUL INTL                             40948
AFM00040990  31.5000   65.8500 1010.0    KANDAHAR AIRPORT                       40990
```

The first column of this file is the station ID that is used as the name of the csv file. 
For example, if the station ID is `USW00014837`, the name of the csv file is `USW00014837.csv`.
In turn, that leads to a Pelican URL of `pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/USW00014837.csv`.

Next, download one of these files. 
What is the command you should use?

### A rudimentary climate analysis

In the `htcondor-plugin` directory is the python script `example.py`. 
This script takes a station ID as an argument and, assuming the corresponding csv file is present in the directory,
will generate an image of the distribution of high and low temperatures across the meteorological seasons for that station.

Download the csv file for a station using Pelican, for example:

```
pelican object get pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/USW00014837.csv ./
```

Then run the script using this command:

```bash
./example.py USW00014837
```

A `.png` file named with the station ID will be created.
Use the Jupyter interface to view the image.

### Scaling out

Suppose that you want to run this analysis on **all** of the stations in the NOAA dataset.
How many times would you need to run the `example.py` script?

You can count the number of lines in the `ghcnd-stations.txt` file with

```bash
wc -l ghcnd-stations.txt
```

That's a lot of stations!
Assuming you had already downloaded the entire dataset, and that each execution of `example.py` takes only 1 second to execute.
Altogether, that amounts to 36 hours to get process the entire dataset.

Imagine that you want to do a more complex analysis, where the execution of `example.py` for each station takes 1 hour to run.
Now instead of only 36 hours to process the dataset, it will take almost *15 years*!!

The power of HTCondor and high throughput computing is the ability to place many individual calculations across many computers.
Users of the OSPool and similar high throughput computing systems regularly run *thousands* of jobs at time. 
That means after 1 hour of "real time", you could process 1,000 stations.
At that rate, the more complex analysis would only take 5 **days**

Let's assume that you have access to such a computing system.
How do you get the data you need to process to each of those computers?

Here is where the Pelican integration with HTCondor comes into play.

### Scaling out with HTCondor and Pelican

HTCondor comes with built-in Pelican integration in the form of the Pelican Plugin. 
That allows for Pelican URLs to be declared as part of HTCondor's file transfer mechanisms.

Let's start by considering a single job that needs the `USW00014837.csv` file as an input.
If the file is in the same directory as the submit file, you can declare that transfer using

```
transfer_input_files = USW00014837.csv
```

If you want HTCondor to transfer the file via Pelican directly from the OpenData repository, 
you replace the filename with it's full Pelican URL:

```
transfer_input_files = pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/USW00014837.csv
```

The component responsible for doing this transfer behind the scene is the Pelican Plugin.

To make things easier to read, you can pull out the bulk of the Pelican URL into a separate variable, like so:

```
PELICAN_PREFIX = pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/
transfer_input_files = $(PELICAN_PREFIX)/USW00014837.csv
```

You can also pull out the unique station ID as it's own variable:

```
PELICAN_PREFIX = pelican://osg-htc.org/aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/
STATION_ID = USW00014837
transfer_input_files = $(PELICAN_PREFIX)/$(STATION_ID).csv
```

This is particularly useful since there are other files (the output image, standard output and standard error) where it is useful to have the station ID in the name.

The last step needed is to make the station ID change for each job.
To do so, the value of `STATION_ID` needs to loop over a list of values.
This is accomplished with HTCondor by the following `queue` statement:

```
queue STATION_ID from station_list.txt
```

The values of STATION_ID are stored in the file `station_list.txt` and one job will be created for each value.

Take a look at the example submit file provided, `example.sub`, by opening it in the Jupyter interface or running

```bash
cat example.sub
```

There are additional aspects to the submit file not covered here, 
but the important thing to understand is that each job will transfer its unique station data file and run the rudimentary analysis covered above.

### Submitting a list of jobs

All we need to do at this point is make the list of station IDs to analyze.
To keep things simple, we'll only do 10 stations, instead of all 120,000.

Run the following command to generate such a list:

```bash
 grep "USW00014837" -A 9 ghcnd-stations.txt | cut -d " " -f 1 > station_list.txt
```

The station list should look like this:

```
$ cat station_list.txt
USW00014837
USW00014838
USW00014839
USW00014840
USW00014841
USW00014842
USW00014843
USW00014844
USW00014845
USW00014846
```

Now submit these jobs to HTCondor using the command

```
condor_submit example.sub
```

This will submit ten jobs in total, one for each of the station IDs in the list.

Monitor the progress of the jobs with

```
condor_watch_q
```

If everything goes well, the progress bar will eventually turn completely to green `#` symbols,
and you should see the 10 image files in the `results` directory.

> [!TIP]
> The Plugin works with the query parameters, e.g., `?recursive` and `?pack`, discussed in an [earlier section](#getting-objects-recursively-with-the-pelican-cli).

> [!IMPORTANT]
> If you really do want run all 120,000 analyses, please don't use the OSPool Notebook to do so!
> The OSPool Notebook can only run a handful of jobs at a time, which means you'll be waiting a **long** time for them to run.
> If you are interested in running a workflow at that scale, we recommend that you request a full OSPool account,
> as described here: [portal.osg-htc.org/application](https://portal.osg-htc.org/application)

## Concluding remarks

