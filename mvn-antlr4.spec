#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-antlr4
Version  : 4.5.3
Release  : 4
URL      : https://github.com/antlr/antlr4/archive/4.5.3.tar.gz
Source0  : https://github.com/antlr/antlr4/archive/4.5.3.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/antlr/antlr4-master/4.7/antlr4-master-4.7.pom
Source2  : https://repo.maven.apache.org/maven2/org/antlr/antlr4-maven-plugin/4.7/antlr4-maven-plugin-4.7.jar
Source3  : https://repo.maven.apache.org/maven2/org/antlr/antlr4-maven-plugin/4.7/antlr4-maven-plugin-4.7.pom
Source4  : https://repo.maven.apache.org/maven2/org/antlr/antlr4-runtime/4.7/antlr4-runtime-4.7.jar
Source5  : https://repo.maven.apache.org/maven2/org/antlr/antlr4-runtime/4.7/antlr4-runtime-4.7.pom
Source6  : https://repo.maven.apache.org/maven2/org/antlr/antlr4/4.7/antlr4-4.7.jar
Source7  : https://repo.maven.apache.org/maven2/org/antlr/antlr4/4.7/antlr4-4.7.pom
Source8  : https://repo1.maven.org/maven2/org/antlr/antlr4-master/4.5.3/antlr4-master-4.5.3.pom
Source9  : https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.5.1-1/antlr4-runtime-4.5.1-1.jar
Source10  : https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.5.1-1/antlr4-runtime-4.5.1-1.pom
Source11  : https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.5.3/antlr4-runtime-4.5.3.jar
Source12  : https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.5.3/antlr4-runtime-4.5.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-antlr4-data = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# ANTLR v4
**ANTLR** (ANother Tool for Language Recognition) is a powerful parser generator for reading, processing, executing, or translating structured text or binary files. It's widely used to build languages, tools, and frameworks. From a grammar, ANTLR generates a parser that can build parse trees and also generates a listener interface (or visitor) that makes it easy to respond to the recognition of phrases of interest.

%package data
Summary: data components for the mvn-antlr4 package.
Group: Data

%description data
data components for the mvn-antlr4 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-master/4.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-master/4.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-maven-plugin/4.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-maven-plugin/4.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-maven-plugin/4.7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-maven-plugin/4.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.7
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.7
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4/4.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4/4.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4/4.7
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4/4.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-master/4.5.3
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-master/4.5.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.1-1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.1-1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.1-1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.1-1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.3
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.3
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.3


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/antlr/antlr4-master/4.5.3/antlr4-master-4.5.3.pom
/usr/share/java/.m2/repository/org/antlr/antlr4-master/4.7/antlr4-master-4.7.pom
/usr/share/java/.m2/repository/org/antlr/antlr4-maven-plugin/4.7/antlr4-maven-plugin-4.7.jar
/usr/share/java/.m2/repository/org/antlr/antlr4-maven-plugin/4.7/antlr4-maven-plugin-4.7.pom
/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.1-1/antlr4-runtime-4.5.1-1.jar
/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.1-1/antlr4-runtime-4.5.1-1.pom
/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.3/antlr4-runtime-4.5.3.jar
/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.5.3/antlr4-runtime-4.5.3.pom
/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.7/antlr4-runtime-4.7.jar
/usr/share/java/.m2/repository/org/antlr/antlr4-runtime/4.7/antlr4-runtime-4.7.pom
/usr/share/java/.m2/repository/org/antlr/antlr4/4.7/antlr4-4.7.jar
/usr/share/java/.m2/repository/org/antlr/antlr4/4.7/antlr4-4.7.pom
