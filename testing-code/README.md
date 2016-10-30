# Testing Code

Let's face it. No one is perfect. No one person will ever make zero mistakes. The issue arises that we don't actually know if our code is performing correctly until it actually runs.

Especially in large projects this is a problem because sometimes methods that we write in code are embedded in specific classes or files which might need special inputs or other conditions to be run. Testing such small methods by hand is tedious and takes a lot of time.

So, because we programmers and software engineers are lazy and don't want to test are code by hand, others have come up with neat frameworks and software applications that let us test our code individually, method-by-method.

This ensures that the application will exhibit the correct behavior when our code runs together.

So to test all of our code means that we actually need to compile and run everything. This also means, in large projects especially, we need to make sure that all of the required libraries that are needed to compile the application are present as well (including the libraries required as a part of the unit testing framework!). 

So we're first going to do a quick dive into some of the standard package managers that you can find for different languages and how those work.

## Package Managers

Similar to `apt-get` on an Ubuntu-based linux machine, package managers allow you to install and manage differnt software libraries for your projects.

Typically package managers will download and store packages on a by-project basis depending on your settings.

##### Package Managers for Different Languages

- Python: **pip** the python package manager
- Java: [**Apache Maven**: More than just a package manager but a project compiler and test runner as well](http://maven.apache.org)
- Node.js: **npm**: The [package manager for Javascript (Node.js) projects](https://www.npmjs.com/)

There are more package managers and many more languages but these are probably the ones you'll most likely be running into.

In this lesson we're going to be using Java and Python, so we'll be covering **pip** and **maven**

Assuming you're running on an debian-based linux distribution you can run the following commands in order to install the required packages.

**pip**

```sh
sudo apt-get install python-pip
```

Alternatively for python 3 you can use `sudo apt-get install python3-pip`.

Simple as that!

**Apache Maven**

```sh
sudo apt-get install default-jdk maven
```

After running those two commands you should be able to run

```sh
mvn -version # Command for Maven
pip --version # Command for pip, use pip3 for python3 pip
```

Now that we've got that out of the way we'll do a quick intro on each package manager before we get into actual unit testing.

### Dive into Pip

Pip lets you install packages which are placed in a directory so that you can import them using python.

For example if you wanted to write a simple web server with [flask](http://flask.pocoo.org/), you need to first download and install the flask python library to your machine. Pip makes this easy.

    pip install Flask

Then inside of your python files your can write

    from flask import Flask
    app = Flask(__name__)

    ....


Whereas, before if you tried to do `from flask import flask` python would probably run into an error because the `flask` library would not be present.

So basically to install any package by name you can simply type

    pip install 'package_name'

To uninstall or remove package

    pip uninstall 'package_name'


For projects with multiple dependencies, you can install them all in one command by using

    pip install -r requirements.txt

Where `requirements.txt` is a text file with a list of python packages. i.e.

```
flask
websockets
requests
```

And that's just about the basics of pip! Next we'll jump into Maven. Slightly more confusing and complex than pip, but much more powerful.

### Dive into Apache Maven

Apache Maven doesn't just manage library dependencies but is also able to build, report, compile, and help create documentation from a project.

Any project that utilizes maven has what is called POM file. Short for **P**roject **O**bject **M**odel. In short the root POM basically defines the structure of a project based on modules, plugins. Below is a sample of a root POM.

Note the module named `usacs-mentor-util`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>io.blanco.usacsmentor</groupId>
    <artifactId>usacs-mentor</artifactId>
    <version>0.1-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>Usacs Mentor Lessons</name>
    <description>USACS Mentor Lessons</description>
    <url>http://github.com/zacblanco/usacs-mentor</url>

    <modules>
        <module>code-test</module>
    </modules>

    <build>
        <plugins>
            <!-- any other plugins -->
            <plugin>
                <artifactId>maven-assembly-plugin</artifactId>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>usacs-mentor-util</descriptorRef>
                    </descriptorRefs>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

The file might seem complex - and it kind of is - but the XML tags pretty much describe the file. The only issue is knowing exactly which tags you're allowed to use in certain sections.

Notice how we have a single module. Each module will have its own POM file where the module compilation settings are described. See below for example.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>

<groupId>io.blanco.usacsmentor.codetest</groupId>
<artifactId>code-test</artifactId>
<version>0.1-SNAPSHOT</version>


<dependencies>
    <dependency>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-http</artifactId>
        <version>8.1.14.v20131031</version>
    </dependency>
    <dependency>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-server</artifactId>
        <version>8.1.14.v20131031</version>
    </dependency>
    <dependency>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-servlet</artifactId>
        <version>8.1.14.v20131031</version>
    </dependency>
</dependencies>

</project>
```

You can see here in our module POM has a different structure where the library dependencies are defined. By including these dependencies you are able to include the libraries and methods in your modules code. Then when you compile and run the project maven will detect and download any necessary dependencies inside of your POM files so that the project can successfully be compiled.

At the root of the project to compile and run tests (and also download any necessary dependencies) you can run


    mvn clean install

`mvn` is the command to invoke maven, then we specify two _targets_ or actions to complete in order.

`clean` will remove any old compiled files. `install` will compile the code, run all the necessary unit tests and then install the new binaries into the target location.


