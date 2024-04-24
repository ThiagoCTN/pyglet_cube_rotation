# Pyglet Cube Rotation

## What is this

This is a simple application (like a hello world!) based on the code posted on a [question asked in 2013 on Stack Overflow](https://stackoverflow.com/questions/16263727/3d-cube-didnt-show-correctly-writen-by-pyglet) by [jing](https://stackoverflow.com/users/2304837/jing).

Their code is based on [Jeremiah's](https://www.3dgep.com/author/jeremiah/) article written in 2012 about [Rendering Primitives with OpenGL](https://www.3dgep.com/rendering-primitives-with-opengl/) in C++.

I'm just cleaning the code, making it more updated and clear in order to help others to know how to start writing a pyglet project.

Since Pyglet [is not supporting OpenGL 2.0 anymore after the release of the Pyglet 2.0 version](https://pyglet.readthedocs.io/en/latest/programming_guide/migration.html), this project will not upgrade Pyglet to the most modern versions for legacy reasons. If you are searching for a modern "hello world" example, this is not what you are looking for!

## How to download

### Using git

```bash
git clone https://gitlab.com/ThiagoCamposTN/pyglet_cube_rotation.git
cd pyglet_cube_rotation
```

### Alternative method

You can manually download the project, extract the files then open a bash inside it.

## How to install

### What you'll need

This project is compatible with `Python 3` and it's not tested with earlier versions.

It's recommended to first create a virtual environment:

```bash
virtualenv env
```

You enter the created environment like this:

On Linux

```bash
source env/bin/activate
```

On Windows

```bash
.\env\Scripts\activate
```

Now you can install the project requirements (that's only `pyglet`) using:

```bash
pip install -r requirements.txt
```


## How to run it

```bash
python main.py
```
