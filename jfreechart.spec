# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support 0

%define section   free

Name:             jfreechart
Version:          1.0.11
Release:          %mkrel 0.0.1
Summary:          Charts Generation library
License:          LGPLv2+
URL:              http://www.jfree.org/jfreechart/
Source0:          http://downloads.sourceforge.net/jfreechart/jfreechart-%{version}.tar.gz
Patch0:           jfreechart-1.0.5-build_xml.patch
Group:            Development/Java
Requires:         jcommon >= 0:1.0.9
BuildRequires:    ant >= 0:1.6
BuildRequires:    ant-junit >= 0:1.6
BuildRequires:    jcommon >= 0:1.0.9
BuildRequires:    java-rpmbuild >= 0:1.6
BuildRequires:    junit
BuildRequires:    servlet
BuildRequires:    xml-commons-apis
BuildRequires:    itext
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif

%description
Free Java class library for generating charts.

%package experimental
Summary:        Experimental components for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
%if %{gcj_support}
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description experimental
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:            Development/Java

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q
%remove_java_binaries
%patch0 -b .sav

%build

%{ant} -f ant/build.xml \
   -Djunit.jar=$(build-classpath junit) \
   -Djcommon.jar=$(build-classpath jcommon) \
   -Dservlet.jar=$(build-classpath servlet) \
   -Dgnujaxp.jar=$(build-classpath xml-commons-apis) \
   -Ditext.jar=$(build-classpath itext) \
   -Dbuildstable=true -Dproject.outdir=. -Dbasedir=. \
   compile compile-experimental javadoc maven-bundle

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}-experimental.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-experimental-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%{gcj_compile}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post experimental
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun experimental
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files experimental
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-experimental-%{version}.jar
%{_javadir}/%{name}-experimental.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-experimental-%{version}.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
