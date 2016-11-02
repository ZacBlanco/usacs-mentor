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

We won't go much deeper into maven than this, but you should understand that this is just the tip of the iceberg in terms of what maven is able to do. Just know that it's capable of much more but this is all we'll do with it for now.

## Unit Testing

Now to the (arguably!) fun part - we're going to go over 1.) What exactly it means to unit test, 2.) How to write and Invoke unit tests, and 3.) Best practices for unit test. 

Basically **unit testing** means breaking down the code into the smallest pieces that we can possibly test, and then individually testing each of these mini blocks of code.

From there it once we test the smallest bits of code, we can move up the tree and test the pieces of code and methods that get combined together. This can make tracking down and finding errors very easy. It can also help find where new features or changes in code behavior are produced as well.

For example, if we [borrow from this Microsoft article on unit testing](https://msdn.microsoft.com/en-us/library/aa292197(v=vs.71).aspx), imagine you have two pieces of code or two methods. Each method is used in conjunction together to perform some kind of task. But when you try to run that task it doesn't completely properly or it terminates improperly. How can you identify what caused the behavior?

- Did the behavior come from method 1?
- Did the behavior come from method 2?
- Did the behavior come from where we combined both methods?
- Was it caused by the interface?
- Was there an error in both methods?

Searching for the cause of these errors and testing manually can actually be a huge time sink and I'm sure most of us have experienced it. When you're writing code, unit tests can end up taking lots of time and/or resources, but in the end and in crucial situations they become incredibly useful for keeping software working in proper order. Especially large pieces of software which are being changed constantly.

Typically when writing unit tests we'll need to write drivers or code stubs in order to set up and tear down data and other pieces. While these stubs and tests can sometimes take time to write, in the end they can end up making the project better, in terms of usability, and much quicker to develop for.

Really it's quite as simple as that.

### Unit Testing Best Practices

This section is going to cover some of the best practices for writing and maintaining unit tests, and how to make them useful in your project. Note that there is no single method that will work best for everyone, nor is there really a "definitive" guide to how to write great unit tests, so most of these are tips I've found through my own experience and my searches of the Internet that I felt were most valuable.

One concept that people sometimes use is called code coverage 

#### 1. Unit Tests Should be Individual

Unit tests should be able to run independently of one another. They shouldn't depend on other tests to run before or after in order to pass.

#### 2. Unit Tests Should Test Conditions Individually

This will lead to more tests, but it will allow you to pinpoint errors more easily than if you included multiple cases within a single test.

#### 3. Unit Tests Should Be Thorough

You should try to write your tests so that at least every line of code is executed at once. But make sure that your tests are meaningful.

#### 4. Unit Tests Should be Stable

Make sure that the unit tests don't depend on random factors. Your tests should be able to pass 99.999% of the time no matter what system you're running. 

#### 5. Every Test Needs a Porpoise (Or Two)

![Porpoise](https://a2ua.com/porpoise/porpoise-003.jpg)

But seriously don't write tests which cover a specific condition twice. Testing the same thing twice will do you no good. Make sure each test has a known purpose. An even better practice is to write a comment or two for each test describing why it's needed.


We could talk some more about TDD (Test Driven Development) but we're not going to get to into that right now. Just know it's a way of building software which is driven by first writing unit tests, and then writing the code to make sure the tests pass. It helps to write good blocks of software. 

### Writing Unit Tests

So now we've learned all about unit tests, but how the heck do we actually write them??

In this section we'll just go over the python API for the unit tests. Its similar to JUnit which is one of the more popular testing frameworks in Java.

We're also going to assume that we're using python3 v3.4+ to run the application and the standard libraries which going along with that distribution.

In order to write a test you need to start with a file to write your tests. A good idea is to name the files with the prefix `test_` and then which ever python you are testing as the postfix.

So something like `test_btree.py`

Inside each test file we'll have something similar to the following:

```python
import unittest, sys
sys.path.append('..') # Used to access python files outside of the test dir

class TestBTree(unittest.TestCase):

    def test_one(self): # A first test case
        # Do some stuff
        # Assert a condition or two.

    def test_two(self): # A second test case
        # More stuff
        # More assertion


    # ....etc....

```

Inside of each test you can use what we call **assertions** in order to check if variables have certain values or not. If an assertion fails, the entire test will fail. The failed test will then be reported. This is how you can find the different errors in your code.

[A list of assertions can be found here in the Python 3 docs](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)

Below is an example set of tests for a simple stack data structure.

```python
import unittest

class TestStack(unittest.TestCase):

    def test_empty_stack(self):
        s1 = []
        self.assertEqual(s1.pop(), None)

    def test_add_one(self):
        s1 = []
        s1.push(5)
        self.assertTrue(len(s1) == 1)
        s1.pop()
        self.assertTrue(len(s1) == 0)
    
    def test_single_pop(self):
        s1 = [5]
        self.assertEqual(len(s1), 1)
        self.assertEqual(s1.pop(), 5)

    def test_add_many(self):
        s1 = []
        for i in range(20):
            s1.push(i)
        self.assertEqual(len(s1), 20)

    def test_add_none(self):
        s1 = []
        s1.push(None)
        self.assertEqual(len(s1), None)

```

You can see in the above example how we use the assertions in order to run our tests. I encourage you to see if you can change a couple of these tests, make them fail, and then try to fix them again.

You can run this test file by `cd`ing into the `python/tests` directory and running

    python3 -m unittest test_stack.py


### Unit Test Exercises

Great! Now we've covered the basics of unit tests. Now we have two exercises on writing some unit tests to cover a couple classes that I've created as exercises in Python and Java. You can choose to do both or either.

The method implementations may or may not have errors. But you should write a test to check every case and make sure each one passes

To run the tests in Python

    cd ./python/tests/
    python3 -m unittest 

To Run the tests in Java:

    cd ./java/
    mvn clean install

