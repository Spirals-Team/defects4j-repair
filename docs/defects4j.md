# Defects4j

## Defects4j require JDK1.7

## Mac OSX usage

Defects4j use GNU readlink function. To use it on mac you need to install the GNU Command Line Tools.

### Install Homebrew

Install the latest XCode and then run the following command to install:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Install the GNU Command Line Tools

```
brew install coreutils
```

### Exports for brew installs

Then add these lines to your .bashrc or .zshrc:

```
export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"
```

and

```
export MANPATH="$(brew --prefix coreutils)/libexec/gnuman:$MANPATH"
```

### Export for defects4j

```
export PATH=$PATH:{path_of_defects4j}/framework/bin
```
